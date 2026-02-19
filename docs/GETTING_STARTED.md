# Getting Started with MyEmailVerifier API

This guide will help you get up and running with the MyEmailVerifier API in minutes.

## Prerequisites

- An active MyEmailVerifier account
- Your API key (get one at [https://client.myemailverifier.com](https://client.myemailverifier.com))
- Basic knowledge of HTTP requests
- A programming language or tool to make HTTP calls

## Step 1: Sign Up and Get Your API Key

1. Visit [client.myemailverifier.com](https://client.myemailverifier.com)
2. Click "Sign Up" or "Get Started"
3. Create your account and verify your email
4. Navigate to Dashboard → API Settings
5. Copy your API key (keep it secure!)

## Step 2: Choose Your Endpoint

MyEmailVerifier offers two API base URLs:

1. **api.myemailverifier.com** - Fast single email validation (recommended for AI/automation)
2. **client.myemailverifier.com** - Comprehensive API suite (all features including bulk)

## Step 3: Your First API Call

### Option 1: Fast Single Email Validation

**Request:**
```bash
curl "https://api.myemailverifier.com/api/validate_single.php?apikey=YOUR_API_KEY&email=test@example.com"
```

**Response:**
```json
{
  "Address": "test@example.com",
  "catch_all": "false",
  "Status": "Valid",
  "Disposable_Domain": "false",
  "Role_Based": "false",
  "Free_Domain": "false",
  "Greylisted": "false",
  "Diagnosis": "Mailbox Exists and Active"
}
```

### Option 2: Comprehensive Validation

**Request:**
```bash
curl "https://client.myemailverifier.com/verifier/validate_single/test@example.com/YOUR_API_KEY"
```

**Response:** Same as Option 1

## Step 4: Understand the Response

### Email Status Values

| Status | Description |
|--------|-------------|
| Valid | Email is valid and deliverable |
| Invalid | Email doesn't exist or is invalid |
| Catch-all | Domain accepts all emails (risky) |
| Unknown | Verification could not be completed |

### Key Response Fields

- **Status**: Overall validation result
- **catch_all**: "true" if domain uses catch-all
- **Disposable_Domain**: "true" for temporary email services
- **Role_Based**: "true" for role emails (support@, info@, etc)
- **Free_Domain**: "true" for Gmail, Yahoo, Hotmail, etc
- **Greylisted**: "true" if server uses greylisting (may need retry)
- **Diagnosis**: Detailed explanation of the result

## Step 5: Choose Your Integration Method

Select the appropriate guide for your technology:

- [Node.js Integration](../examples/nodejs/README.md)
- [Python Integration](../examples/python/README.md)
- [PHP Integration](../examples/php/README.md)
- [JavaScript Integration](../examples/javascript/README.md)
- [cURL / REST Integration](../examples/curl/README.md)

## Step 6: Implement Error Handling

```python
# Example error handling
response = verify_email("test@example.com")

if response['error_code'] == 0:
    print("Email is valid!")
elif response['error_code'] == 1:
    print("Email is invalid")
elif response['error_code'] == 2:
    print("Email is a catch-all address")
else:
    print(f"Verification failed: {response.get('message')}")
```

## Step 6: Implement Error Handling

```python
# Python example
import requests

def verify_email(email, api_key):
    try:
        response = requests.get(
            'https://api.myemailverifier.com/api/validate_single.php',
            params={'apikey': api_key, 'email': email},
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            
            if result['Status'] == 'Valid':
                print(f"✓ {email} is valid")
                return True
            elif result['Status'] == 'Invalid':
                print(f"✗ {email} is invalid: {result['Diagnosis']}")
                return False
            elif result['Status'] == 'Catch-all':
                print(f"⚠ {email} is catch-all (risky)")
                return None
            else:
                print(f"? {email} status unknown")
                return None
                
        elif response.status_code == 429:
            print("Rate limit exceeded. Please wait.")
            return None
        elif response.status_code == 401:
            print("Invalid API key")
            return None
        else:
            print(f"Error: HTTP {response.status_code}")
            return None
            
    except requests.Timeout:
        print("Request timeout")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Usage
verify_email("test@example.com", "YOUR_API_KEY")
```

## Step 7: Bulk Verification (Advanced)

For verifying large lists of emails:

```python
import requests

# 1. Upload file
files = {'filename': open('emails.txt', 'rb')}
data = {'api_key': 'YOUR_API_KEY'}

response = requests.post(
    'https://client.myemailverifier.com/verifier/upload_file',
    files=files,
    data=data
)

upload_result = response.json()
file_id = upload_result['file_id']
print(f"File uploaded. ID: {file_id}")

# 2. Check status (poll until finished)
import time

while True:
    response = requests.get(
        f'https://client.myemailverifier.com/verifier/file_info/YOUR_API_KEY/{file_id}'
    )
    
    info = response.json()
    
    if info['status'] == 'finished':
        print(f"Verification complete!")
        print(f"Valid: {info['valid']}")
        print(f"Invalid: {info['invalid']}")
        print(f"Download CSV: {info['file_path']}")
        print(f"Download Excel: {info['xls_file_path']}")
        break
    elif info['status'] == 'processing':
        print("Still processing...")
        time.sleep(5)  # Wait 5 seconds before checking again
    else:
        print(f"Status: {info['status']}")
        break
```

## Step 8: Check Your Credits

Monitor your remaining credits:

```bash
curl "https://client.myemailverifier.com/verifier/getcredits/YOUR_API_KEY"
```

```python
# Python example
response = requests.get(
    f'https://client.myemailverifier.com/verifier/getcredits/YOUR_API_KEY'
)
credits = response.json()['credits']
print(f"Remaining credits: {credits}")
```

## Step 9: Optimize Your Usage

### Tips for Best Results

1. **Use async calls** - Don't block your application
2. **Implement caching** - Store recent results
3. **Batch verification** - Verify multiple emails at once for efficiency
4. **Handle rate limits** - Implement retry logic with exponential backoff
5. **Monitor usage** - Check your dashboard regularly

### Rate Limiting

- **Free Plan**: 10 requests/minute
- **Paid Plans**: Higher limits based on your plan
- **Enterprise**: Custom limits available

## Step 7: Next Steps

- Explore the [API Reference](API_REFERENCE.md)
- Check out [Integration Examples](../examples/)
- Review [Error Codes](ERROR_CODES.md)
- Read the [FAQ](FAQ.md)
- Implement in your application

## Common Questions

**Q: How long does verification take?**
A: Usually 1-3 seconds per email depending on domain responsiveness.

**Q: What's included in verification?**
A: Domain validation, MX record check, and SMTP-level verification.

**Q: Can I verify batches of emails?**
A: Yes! Use our bulk verification endpoint for multiple emails.

**Q: Do you offer webhooks?**
A: Yes! See integration docs for webhook setup.

## Need Help?

- 📖 Full documentation in the [docs](.) folder
- 💬 Live chat support on our website
- 📧 Email us at support@myemailverifier.com
- 🐛 Report issues on GitHub

---

You're ready to start verifying emails! Check out the examples directory for code in your preferred language.
