from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os
from dotenv import load_dotenv
import requests
import base64
import json
from datetime import datetime
from django.conf import settings
from .forms import ContractForm
from .models import Contract

load_dotenv()

@login_required
def send_request(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            user_email = request.user.email
            recipient_email = form.cleaned_data['recipient_email']
            contract_text = form.cleaned_data['contract_text']
            full_name = request.user.username
            signing_date = datetime.now().strftime('%Y-%m-%d')

            contract_content = contract_text.replace('[Full Name: ______]', full_name)
            contract_content = contract_content.replace('[Date: ______]', signing_date)

            api_token = os.getenv('DROPBOX_SIGN_API_KEY')
            client_id = os.getenv('DROPBOX_SIGN_CLIENT_ID')

            if not api_token or not client_id or not user_email:
                return HttpResponse("API key, Client ID, or user email not found")

            file_path = os.path.join(settings.MEDIA_ROOT, 'contracts', 'test_contract.txt')
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(contract_content + "\n[Signature: ______]")
            file = open(file_path, 'rb')

            redirect_url = "https://76d9v8dq-8000.euw.devtunnels.ms/contracts/success"
            url = "https://api.hellosign.com/v3/signature_request/send"
            auth_string = f"{api_token}:"
            auth_header = base64.b64encode(auth_string.encode()).decode()
            headers = {
                "Authorization": f"Basic {auth_header}",
                "Accept": "application/json"
            }
            files = {'file': file}
            data = {
                "client_id": client_id,
                "title": f"Dynamic Test Contract - {full_name}",
                "subject": f"Contract for {full_name} and {recipient_email}",
                "message": f"Dear {full_name}, please sign this contract. An invite has been sent to {recipient_email}.",
                "signers[0][email_address]": user_email,
                "signers[0][name]": full_name,
                "signers[0][order]": "0",
                "signers[1][email_address]": recipient_email,
                "signers[1][name]": "Invited Signer",
                "signers[1][order]": "1",
                "test_mode": "1",
                "signing_redirect_url": redirect_url
            }
            print("Request Data:", data)

            try:
                response = requests.post(url, headers=headers, files=files, data=data, verify=False)
                print("Raw API Response:", response.text)
                try:
                    response_data = response.json()
                    print("Parsed Response Data:", json.dumps(response_data, indent=2))
                except json.JSONDecodeError:
                    print("Failed to parse JSON:", response.text)
                    file.close()
                    return HttpResponse(f"Invalid JSON response: {response.text}")

                if response.status_code == 200:
                    if "signature_request" in response_data and "signature_request_id" in response_data["signature_request"]:
                        sign_url = response_data["signature_request"]["signing_url"]
                        print("Sign URL:", sign_url)
                        file.close()
                        return redirect(sign_url)
                    else:
                        file.close()
                        return HttpResponse("No signature_request_id or signing_url in response")
                else:
                    file.close()
                    return HttpResponse(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                file.close()
                return HttpResponse(f"Request Error: {str(e)}")
    else:
        form = ContractForm()
    return render(request, 'contracts/send_request.html', {'form': form})

@login_required
def success(request):
    user = request.user
    full_name = user.username
    title = f"Contract Signed - {datetime.now().strftime('%Y-%m-%d')}"
    date = datetime.now().date()
    file_path = os.path.join(settings.MEDIA_ROOT, 'contracts', 'test_contract.txt')
    if os.path.exists(file_path):
        contract = Contract.objects.create(
            user=user,
            title=title,
            full_name=full_name,
            date=date,
            contract_file=file_path
        )
        return render(request, 'contracts/success.html', {'message': 'The contract has been successfully signed!', 'contract': contract})
    else:
        return HttpResponse("Contract file not found.")