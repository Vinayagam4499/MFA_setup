# Two-Factor Authentication Django Project

This repository contains a sample Django project demonstrating a two-factor authentication (2FA) system. The project includes a user login system, 2FA setup and verification, and protected pages (profile/home). The user interface is built using Bootstrap for a modern and responsive design.

## Features

- **User Login:** Secure login with error handling.
- **2FA Setup:** Allows users to set up two-factor authentication by scanning a QR code with an authenticator app (e.g., Google Authenticator or Authy) and displays a secret key if needed.
- **2FA Verification:** Verifies the 6-digit token provided by the user's authenticator app.
- **Protected Pages:** Home and profile pages are accessible only after a successful 2FA verification.
- **Responsive UI:** Uses Bootstrap 5 for a clean, professional design and responsive layout.

## Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

- **Python 3.8+**
- **Django 3.x or higher** (adjust based on your project's needs)
- **Virtual Environment** (recommended)

### Installation

1. **Clone the Repository:**

   ```bash
   https://github.com/Vinayagam4499/MFA_setup.git

 
python3 -m venv env
source env/bin/activate

