# Breach Notifier

A Python GUI tool to check if your email or password has appeared in known breach data.

## How it works

- Loads emails from:
  - `/home/senuri/Downloads/linkedin_data.csv`
  - `/home/senuri/seclists_valid_emails.txt`
- Loads passwords from:
  - `/usr/share/seclists/Passwords/Common-Credentials/500-worst-passwords.txt`

## How to run

1. Make sure Python 3 is installed.
2. Run the script:
   ```bash
   python3 breach_checker_gui.py
