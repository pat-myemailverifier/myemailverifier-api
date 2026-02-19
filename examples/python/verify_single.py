#!/usr/bin/env python3
"""
Verify a single email address using MyEmailVerifier API
Run: python verify_single.py
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv('MYEMAILVERIFIER_API_KEY', 'YOUR_API_KEY')


def verify_email_fast_api(email):
    """Option 1: Fast API (Recommended for AI/Automation)"""
    try:
        print(f'Verifying email (Fast API): {email}')

        response = requests.get(
            'https://api.myemailverifier.com/api/validate_single.php',
            params={
                'apikey': API_KEY,
                'email': email
            },
            timeout=10
        )

        if response.status_code == 429:
            print('✗ Rate limit exceeded')
            return None
        elif response.status_code == 401:
            print('✗ Invalid API key')
            return None
        elif response.status_code != 200:
            print(f'✗ HTTP Error: {response.status_code}')
            return None

        result = response.json()

        # Display results
        print('\n=== Verification Result ===')
        print(f"Email: {result.get('Address')}")
        print(f"Status: {result.get('Status')}")
        print(f"Diagnosis: {result.get('Diagnosis')}")
        print(f"Catch-all: {result.get('catch_all')}")
        print(f"Role-based: {result.get('Role_Based')}")
        print(f"Disposable: {result.get('Disposable_Domain')}")
        print(f"Free Domain: {result.get('Free_Domain')}")
        print(f"Greylisted: {result.get('Greylisted')}")

        return result

    except requests.exceptions.Timeout:
        print('✗ Request timeout')
        return None
    except requests.exceptions.RequestException as e:
        print(f'✗ Error verifying email: {e}')
        return None


def verify_email_client_api(email):
    """Option 2: Client API (Comprehensive)"""
    try:
        print(f'Verifying email (Client API): {email}')

        response = requests.get(
            f'https://client.myemailverifier.com/verifier/validate_single/{email}/{API_KEY}',
            timeout=10
        )

        if response.status_code != 200:
            print(f'✗ HTTP Error: {response.status_code}')
            return None

        result = response.json()

        # Display results (same format)
        print('\n=== Verification Result ===')
        print(f"Email: {result.get('Address')}")
        print(f"Status: {result.get('Status')}")
        print(f"Diagnosis: {result.get('Diagnosis')}")

        return result

    except requests.exceptions.RequestException as e:
        print(f'✗ Error verifying email: {e}')
        return None


def get_credits():
    """Get remaining API credits"""
    try:
        response = requests.get(
            f'https://client.myemailverifier.com/verifier/getcredits/{API_KEY}',
            timeout=5
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"Remaining Credits: {result.get('credits')}\n")
            return result.get('credits')
        else:
            print(f'✗ Failed to get credits: HTTP {response.status_code}')
            return None
            
    except requests.exceptions.RequestException as e:
        print(f'✗ Error getting credits: {e}')
        return None


def main():
    """Test with different emails"""
    
    # Check credits first
    get_credits()
    
    test_emails = [
        'valid@example.com',
        'support@myemailverifier.com'
    ]

    for email in test_emails:
        # Use Fast API (recommended)
        verify_email_fast_api(email)
        
        # Or use Client API
        # verify_email_client_api(email)
        
        print('\n')


if __name__ == '__main__':
    main()
