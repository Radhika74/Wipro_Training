# Extract the user id, domain name and suffix from the following email addresses.
# emails = """zuck@facebook.com
# sunder33@google.com
# jeff42@amazon.com"""

import re

def separate_emails(email):
    match = re.match(r'(\w+)@(\w+)\.(\w+)', email)
    if match:
        return match.groups()
    else:
        return None

emails = input("Enter email addresses (comma separated): ").split(',')

for email in emails:
    email = email.strip()
    parts = separate_emails(email)
    if parts:
        user, domain, suffix = parts
        print(f"\nEmail: {email}")
        print(f"User ID: {user}")
        print(f"Domain Name: {domain}")
        print(f"Suffix: {suffix}")
    else:
        print(f"\nInvalid email: {email}")
