#!/usr/bin/env python3
"""
Bulk verify emails using file upload
Run: python verify_batch.py
"""

import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv('MYEMAILVERIFIER_API_KEY', 'YOUR_API_KEY')
BASE_URL = 'https://client.myemailverifier.com'


def upload_file(filename):
    """Upload a file for bulk verification"""
    try:
        print(f'Uploading file: {filename}')

        with open(filename, 'rb') as f:
            files = {'filename': f}
            data = {'api_key': API_KEY}
            
            response = requests.post(
                f'{BASE_URL}/verifier/upload_file',
                files=files,
                data=data,
                timeout=30
            )

        result = response.json()

        if result.get('status'):
            print(f"✓ File uploaded successfully!")
            print(f"  File ID: {result.get('file_id')}")
            print(f"  File Name: {result.get('file_name')}")
            return result.get('file_id')
        else:
            print(f"✗ Upload failed: {result.get('msg')}")
            return None

    except requests.exceptions.RequestException as e:
        print(f'Error uploading file: {e}')
        return None
    except FileNotFoundError:
        print(f'File not found: {filename}')
        return None


def get_file_info(file_id):
    """Get file verification status and results"""
    try:
        response = requests.get(
            f'{BASE_URL}/verifier/file_info/{API_KEY}/{file_id}',
            timeout=10
        )

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f'Error getting file info: {e}')
        return None


def wait_for_completion(file_id, check_interval=5, max_wait=600):
    """Wait for file verification to complete"""
    print(f'\nWaiting for verification to complete...')
    
    start_time = time.time()
    
    while (time.time() - start_time) < max_wait:
        info = get_file_info(file_id)
        
        if not info:
            print('✗ Failed to get file info')
            return None
            
        status = info.get('status')
        
        if status == 'finished':
            print('\n✓ Verification complete!\n')
            return info
        elif status == 'processing':
            elapsed = int(time.time() - start_time)
            print(f'  Still processing... ({elapsed}s elapsed)', end='\r')
            time.sleep(check_interval)
        elif status == 'failed':
            print(f'\n✗ Verification failed')
            return info
        else:
            print(f'\n  Status: {status}')
            time.sleep(check_interval)
    
    print(f'\n✗ Timeout: Verification took longer than {max_wait}s')
    return None


def display_results(info):
    """Display verification results"""
    print('=== Verification Results ===')
    print(f"File Name: {info.get('file_name')}")
    print(f"Created: {info.get('created_at')}")
    print(f"\nTotal Emails: {info.get('total')}")
    print(f"Valid: {info.get('valid')}")
    print(f"Invalid: {info.get('invalid')}")
    print(f"Catch-all: {info.get('catchall')}")
    print(f"Unknown: {info.get('unknown')}")
    print(f"Duplicates: {info.get('duplicates')}")
    print(f"Spam Traps: {info.get('spam_trap')}")
    print(f"Toxic Domains: {info.get('toxic_domains')}")
    print(f"\nCredits Used: {info.get('credit_used')}")
    
    print(f"\n=== Download Links ===")
    print(f"CSV: {info.get('file_path')}")
    print(f"Excel: {info.get('xls_file_path')}")


def create_sample_file():
    """Create a sample emails.txt file"""
    sample_emails = [
        'john.doe@example.com',
        'jane.smith@gmail.com',
        'support@myemailverifier.com',
        'invalid@invalid-domain-xyz.com',
        'admin@company.org'
    ]
    
    filename = 'sample_emails.txt'
    with open(filename, 'w') as f:
        for email in sample_emails:
            f.write(email + '\n')
    
    print(f'Created sample file: {filename}')
    return filename


def main():
    """Main execution"""
    
    # Create sample file or use your own
    filename = 'emails.txt'  # Change to your file
    
    if not os.path.exists(filename):
        print(f'File not found: {filename}')
        print('Creating sample file instead...\n')
        filename = create_sample_file()
    
    # Step 1: Upload file
    file_id = upload_file(filename)
    
    if not file_id:
        print('Upload failed. Exiting.')
        return
    
    # Step 2: Wait for completion
    info = wait_for_completion(file_id, check_interval=5)
    
    if not info:
        print('Verification did not complete. Exiting.')
        return
    
    # Step 3: Display results
    display_results(info)
    
    print('\nYou can download the results using the links above.')


if __name__ == '__main__':
    main()
