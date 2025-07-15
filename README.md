# Contract Signing Application

A simple Django-based web application for creating and signing contracts using the HelloSign API.

## Overview
This project allows users to create dynamic contract templates, send them for signing via the HelloSign API, and store signed contract details in a database. It provides a basic admin panel for managing contracts and supports testing with a local development environment.

## Technologies Used
- **Python**: Core programming language.
- **Django**: Web framework for building the application.
- **HelloSign API**: For electronic signature requests and management.
- **VSCode**: Development environment with port forwarding for testing.
- **SQLite**: Default database (can be replaced with PostgreSQL for production).
- **HTML/CSS**: Basic templates for user interface.

## Installation

### Prerequisites
- Python 3.8 or higher
- Git (for cloning the repository)
- A HelloSign account (for API key and Client ID)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/contract-signing-app.git
   cd contract-signing-app
Set Up a Virtual Environment
bash

Collapse

Wrap

Run

Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies
bash

Collapse

Wrap

Run

Copy
pip install -r requirements.txt
Configure Environment Variables
Create a .env file in the project root:
text

Collapse

Wrap

Copy
DROPBOX_SIGN_API_KEY=your_hellosign_api_key
DROPBOX_SIGN_CLIENT_ID=your_hellosign_client_id
REDIRECT_URL=http://127.0.0.1:8000/contracts/success/  # For local testing
Replace your_hellosign_api_key and your_hellosign_client_id with your HelloSign credentials.
Apply Migrations
bash

Collapse

Wrap

Run

Copy
python manage.py migrate
Create a Superuser
bash

Collapse

Wrap

Run

Copy
python manage.py createsuperuser
Follow the prompts to set a username, email, and password.
Run the Development Server
bash

Collapse

Wrap

Run

Copy
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/.
Usage
Register/Login: Sign up or log in at /accounts/register/ or /accounts/login/.
Create a Contract: Go to /contracts/send_request/, fill out the form with your email, a recipient email, and contract text, then click "Send for Signing".
Sign the Contract: Follow the HelloSign link sent to your email to sign the contract.
View Success: After signing, you’ll be redirected to /contracts/success/.
Manage Contracts: Access the admin panel at /admin/ with your superuser credentials to view and manage signed contracts.
Testing Notes
Email Matching: During testing, ensure the email of the registered account matches the recipient email in the contract form. This is a temporary limitation for local testing with HelloSign.
Local Environment: Use port forwarding (e.g., VSCode dev tunnels) to test with a public URL if needed. Update the REDIRECT_URL in .env and HelloSign dashboard accordingly.
Debug Mode: Keep DEBUG = True in settings.py for development to see detailed error messages.
Contributing
Feel free to fork this repository, make improvements, and submit pull requests. For issues or suggestions, please open an issue on GitHub.