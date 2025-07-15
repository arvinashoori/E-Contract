from django import forms

class ContractForm(forms.Form):
    recipient_email = forms.EmailField(label="Email of Second Signatory")
    contract_text = forms.CharField(widget=forms.Textarea, initial="""
    This is a formal contract agreement entered into on [Date: ______] between [Full Name: ______] (Party A) and [Invited Signer] (Party B).

    1. Purpose: This agreement outlines the terms for a mutual business partnership aimed at delivering high-quality services.
    2. Responsibilities: Party A agrees to provide technical expertise, while Party B will handle marketing efforts.
    3. Duration: This contract shall commence on the signing date and remain valid for one year unless terminated earlier.
    4. Termination: Either party may terminate this agreement with 30 days' written notice.
    5. Signatures: Both parties must sign below to acknowledge their acceptance of these terms.

    [Signature: ______]
    """)