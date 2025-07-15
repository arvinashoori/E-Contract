# Contract Signing Application

## Introduction
This project is an **e-signature web application** built with **Django** for portfolio and learning purposes. The main goal is to provide a fully functional platform for creating, sending, and managing electronic contracts using the **HelloSign API**. The application features secure user authentication, contract management, and a user-friendly admin panel for overseeing signed contracts, with a responsive front-end styled with basic **HTML/CSS**.

---

## Features
- **User Authentication**:
  - Registration, login, and logout with Django’s built-in authentication.
  - Restricted access to contract creation for authenticated users only.
- **Contract Management**:
  - Create and send contracts with dynamic fields (e.g., full name, date).
  - Store signed contracts in the database with details like title and signature ID.
- **Electronic Signing**:
  - Secure e-signatures via **HelloSign API**.
  - Redirect to a success page after signing.
- **Admin Panel**:
  - Comprehensive interface to manage users and signed contracts.
  - Display contract details (title, signature ID) in the admin panel.
- **Security**:
  - Environment variables for sensitive data (e.g., HelloSign API keys) using `python-decouple`.
  - Protection against secret exposure with `.gitignore`.
- **Testing Support**:
  - Local testing with VSCode port forwarding for public URL access.

---

## Technologies Used
- **Programming Language**: Python 3
- **Web Framework**: Django 4.2+
- **E-Signature Service**: HelloSign API
- **Front-end Styling**: HTML/CSS
- **Database**: SQLite (for development)
- **Environment Variables**: python-decouple
- **Version Control**: Git with GitHub integration

---

## Project Structure
- `contracts/`: Contract creation, signing, and success views (`send_request`, `success`).
- `templates/contracts/`: HTML templates (e.g., `send_request.html`, `success.html`).
- `media/contracts/`: Storage for contract files.
- `contract_signing_app/`: Main project settings and URLs.

---

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/contract-signing-app.git
   cd contract-signing-app
   ```
2.  Create and activate a virtual environment:
   ```bash 
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3.  Install dependencies:
   ```bash 
   pip install -r requirements.txt
   ```
4.  Set up environment variables in .env:
   ```bash 
   DROPBOX_SIGN_API_KEY=your_hellosign_api_key
   DROPBOX_SIGN_CLIENT_ID=your_hellosign_client_id
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```


5. Apply migrations :
   ```bash
   python manage.py makemigrations
   python manage.py migrat
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

Access the application at http://127.0.0.1:8000.
---
## Usage
- **Admin Panel**: Admin Panel: Manage users and signed contracts at http://127.0.0.1:8000/admin/
- **User Actions**:
  - Register: `/accounts/signup/`
  - Login: `/accounts/signin/`
  - Logout: `/accounts/logout/`
  - Send Contract: Create and send a contract at /contracts/send_request/ (requires login).
- Signing: Complete the signing process via the HelloSign link sent to your email, with contract details saved in the database.
---

## Example Workflow
1. **Register a User**:
   - Navigate to /accounts/register/ and create an account.
   - Example: Username: yourname, Email: yourname@example.com, Password: A12345678a@ `A12345678a@`.
2. **Login**:
   - Go to /accounts/login/ and log in with your credentials.
3. **Send a Contract**:
   - Visit /contracts/send_request/, enter your email, a recipient email (same for testing), and contract text (e.g., "Agreement between [Full Name: ______] on [Date: ______]")
   - Click "Send for Signing".
4. **Sign the Contract**:
   - Open the HelloSign link from your email and sign the contract.
5. **View Success**:
   - After signing, you’ll be redirected to /contracts/success/ to confirm the signature.

---



## Author
**Arvin Ashoori**

## Contact
- **GitHub**: [arvinashoori](https://github.com/arvinashoori)
- **Email**: [arvin.ashoori@gmail.com]
- **Tg**: [arvinashoori]