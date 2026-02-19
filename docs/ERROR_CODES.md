# Error Codes Reference

Complete reference for MyEmailVerifier API responses and status codes.

## Email Validation Status

The API returns a `Status` field with one of these values:

### ✅ Valid

**Meaning:** Email address exists and is deliverable
**Response Example:**
```json
{
  "Address": "user@example.com",
  "Status": "Valid",
  "Diagnosis": "Mailbox Exists and Active",
  "catch_all": "false",
  "Role_Based": "false",
  "Disposable_Domain": "false",
  "Free_Domain": "false",
  "Greylisted": "false"
}
```
**Action:** Safe to send emails to this address

---

### ❌ Invalid

**Meaning:** Email address doesn't exist or is not deliverable
**Causes:**
- Mailbox doesn't exist on the domain
- Domain doesn't exist
- Invalid email format
- SMTP verification failed

**Response Example:**
```json
{
  "Address": "invalid@example.com",
  "Status": "Invalid",
  "Diagnosis": "Mailbox Does Not Exist",
  "catch_all": "false"
}
```
**Action:** Remove from mailing list or ask user to correct

---

### 🔄 Catch-all

**Meaning:** Domain accepts all emails (can't verify specific mailbox)
**Causes:**
- Domain configured with catch-all
- Server accepts any email to the domain
- Cannot confirm specific mailbox existence

**Response Example:**
```json
{
  "Address": "anything@example.com",
  "Status": "Catch-all",
  "Diagnosis": "Domain uses catch-all configuration",
  "catch_all": "true"
}
```
**Action:** Accept with caution - may or may not be deliverable

---

### ❓ Unknown

**Meaning:** Verification could not be completed
**Causes:**
- Server timeout
- Greylisting (temporary rejection)
- Server temporarily unavailable
- Network issues

**Response Example:**
```json
{
  "Address": "user@example.com",
  "Status": "Unknown",
  "Diagnosis": "Server temporarily unavailable",
  "Greylisted": "true"
}
```
**Action:** Retry verification later or accept with caution

---

## Response Field Details

### catch_all
- **"true"** - Domain accepts all emails
- **"false"** - Normal domain configuration

### Role_Based
- **"true"** - Generic role email (support@, info@, admin@, sales@, etc.)
- **"false"** - Personal email address

### Disposable_Domain
- **"true"** - Temporary/disposable email service
- **"false"** - Legitimate email domain

### Free_Domain
- **"true"** - Free email provider (Gmail, Yahoo, Hotmail, etc.)
- **"false"** - Business/custom domain

### Greylisted
- **"true"** - Server uses greylisting (may need retry)
- **"false"** - Normal server response

---

## HTTP Status Codes

---

## HTTP Status Codes

### 200 - OK
**Meaning:** Request successful
**Response:** Contains verification result

### 400 - Bad Request
**Meaning:** Invalid request parameters
**Causes:**
- Missing email parameter
- Invalid email format
- Malformed request

**Response Example:**
```json
{
  "status": false,
  "message": "Email parameter is required",
  "error": "INVALID_REQUEST"
}
```

---

### 401 - Unauthorized
**Meaning:** Invalid or missing API key
**Causes:**
- API key not provided
- Invalid API key
- API key revoked

**Response Example:**
```json
{
  "status": false,
  "message": "Invalid API key",
  "error": "INVALID_API_KEY"
}
```

**Solution:**
1. Check API key in your dashboard
2. Ensure API key is included in request
3. Generate new key if needed

---

### 403 - Forbidden
**Meaning:** API key doesn't have permission
**Causes:**
- Referer restriction (demo keys)
- Account suspended
- Feature not available on plan

**Response Example:**
```json
{
  "status": false,
  "message": "This API key can only be used from myemailverifier.com website",
  "error": "UNAUTHORIZED_REFERER"
}
```

---

### 429 - Too Many Requests
**Meaning:** Rate limit exceeded
**Causes:**
- Too many requests in time window
- Default: 30 requests per minute exceeded
- Restricted key daily limit reached

**Response Example:**
```json
{
  "status": false,
  "message": "Rate limit exceeded. You can make 30 requests per minute.",
  "error": "RATE_LIMIT_EXCEEDED"
}
```

**Solution:**
1. Implement rate limiting in your code
2. Add delays between requests
3. Upgrade plan for higher limits
4. Use bulk verification for multiple emails

---

### 500 - Internal Server Error
**Meaning:** Server-side error
**Causes:**
- Temporary server issue
- Service maintenance
- Unexpected error

**Response Example:**
```json
{
  "status": false,
  "message": "Internal server error. Please try again.",
  "error": "SERVER_ERROR"
}
```

**Action:** Retry request after a short delay

---

## Common Error Scenarios

### Insufficient Credits
```json
{
  "status": false,
  "message": "Insufficient credits. Please purchase more credits.",
  "error": "INSUFFICIENT_CREDITS"
}
```
**Solution:** Add credits to your account or upgrade plan

---

### Invalid File Format (Bulk Upload)
```json
{
  "status": false,
  "msg": "Invalid file format. Please upload TXT or CSV file."
}
```
**Solution:** Use only .txt or .csv files for bulk verification

---

### File Upload Error
```json
{
  "status": false,
  "msg": "File upload failed. Please try again."
}
```
**Solution:** 
- Check file size (max 10MB)
- Ensure file is properly formatted
- Retry upload

---

## Best Practices

### Error Handling
```python
try:
    response = verify_email(email)
    
    if response.status_code == 200:
        result = response.json()
        
        if result['Status'] == 'Valid':
            # Email is valid
            pass
        elif result['Status'] == 'Invalid':
            # Email is invalid
            pass
        elif result['Status'] == 'Catch-all':
            # Handle catch-all
            pass
            
    elif response.status_code == 429:
        # Rate limit - wait and retry
        time.sleep(60)
        
    elif response.status_code == 401:
        # Invalid API key
        raise Exception('API key invalid')
        
except Exception as e:
    # Handle error
    log_error(e)
```

### Retry Logic
```python
import time

def verify_with_retry(email, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = verify_email(email)
            
            if response.status_code == 429:
                # Rate limited - wait exponentially
                wait_time = (2 ** attempt) * 60
                time.sleep(wait_time)
                continue
                
            return response
            
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(5)
    
    return None
```

---

## Support

If you encounter errors not listed here:
- 📧 Email: support@myemailverifier.com
- 💬 Live chat on our website
- 📖 Check API logs in your dashboard
- 🐛 Report on GitHub Issues

---

### Rate Limit Error (Code: 102)

**Status:** Rate Limit Exceeded
**Meaning:** Too many requests in short time period
**Causes:**
- Exceeded requests per minute
- Exceeded daily quota
- Plan limit reached

**Solution:**
1. Wait before making more requests
2. Implement exponential backoff
3. Batch requests efficiently
4. Upgrade plan if needed

**Response:**
```json
{
  "error_code": 102,
  "message": "Rate limit exceeded",
  "status": "error",
  "retry_after": 60
}
```

---

### Invalid Request (Code: 103)

**Status:** Invalid Request Format
**Meaning:** Request format is invalid
**Causes:**
- Invalid JSON format
- Wrong headers
- Invalid URL parameters
- Wrong HTTP method

**Solution:**
1. Check request format
2. Verify Content-Type header
3. Check parameter names
4. See [API Reference](API_REFERENCE.md)

**Response:**
```json
{
  "error_code": 103,
  "message": "Invalid request format",
  "status": "error"
}
```

---

### Missing Parameter (Code: 104)

**Status:** Missing Required Parameter
**Meaning:** Required request parameter is missing
**Causes:**
- Missing email address
- Missing API key
- Missing required field

**Solution:**
1. Check required parameters
2. Verify all fields are included
3. See endpoint documentation

**Response:**
```json
{
  "error_code": 104,
  "message": "Missing required parameter: email",
  "status": "error"
}
```

---

### Request Timeout (Code: 105)

**Status:** Request Timeout
**Meaning:** Request took too long to process
**Causes:**
- Slow network connection
- Mail server timeout
- Service overload

**Solution:**
1. Retry the request
2. Increase timeout value
3. Contact support if persistent

**Response:**
```json
{
  "error_code": 105,
  "message": "Request timeout",
  "status": "error"
}
```

---

### Batch Limit Exceeded (Code: 106)

**Status:** Batch Size Exceeded
**Meaning:** Batch request has too many emails
**Causes:**
- More than 100 emails in batch
- Exceeds batch size limit

**Solution:**
1. Split into smaller batches
2. Use maximum 100 emails per request
3. Process multiple batches

**Response:**
```json
{
  "error_code": 106,
  "message": "Batch size exceeded (max 100)",
  "status": "error"
}
```

---

### Account Limit Exceeded (Code: 107)

**Status:** Monthly Quota Exceeded
**Meaning:** Monthly verification limit reached
**Causes:**
- Used all monthly verifications
- Upgrade needed for more usage

**Solution:**
1. Upgrade your plan
2. Wait for monthly reset
3. Contact support for enterprise

**Response:**
```json
{
  "error_code": 107,
  "message": "Monthly quota exceeded",
  "status": "error"
}
```

---

## Deliverability Statuses

| Status | Color | Meaning | Action |
|--------|-------|---------|--------|
| `safe` | Green | Email is valid and safe | ✅ Send |
| `risky` | Yellow | Email exists but has issues | ⚠️ Verify or require confirmation |
| `invalid` | Red | Email is invalid | ❌ Remove |
| `unknown` | Gray | Could not verify | ⏳ Retry later |

---

## Common Error Scenarios

### Scenario 1: "Invalid API Key"

**Cause:** API key configuration issue

**Solution:**
```javascript
// Wrong
const apiKey = "your API key here"; // ❌ Not secure

// Right
import dotenv from 'dotenv';
dotenv.config();
const apiKey = process.env.MYEMAILVERIFIER_API_KEY; // ✅ Secure
```

---

### Scenario 2: "Rate Limit Exceeded"

**Cause:** Too many requests in short time

**Solution:**
```python
import time
import requests

def verify_with_retry(email, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.post(
                'https://api.myemailverifier.com/verify',
                json={'email': email, 'api_key': API_KEY}
            )
            
            if response.status_code == 429:  # Rate limit
                wait_time = 2 ** attempt  # Exponential backoff
                time.sleep(wait_time)
                continue
            
            return response.json()
        except Exception as e:
            print(f"Error: {e}")
    
    return None
```

---

### Scenario 3: "Domain Validation Failed"

**Cause:** Invalid domain or DNS issues

**Solution:**
```javascript
// Validate domain first
async function verifyWithDomainCheck(email) {
    const domain = email.split('@')[1];
    
    // Check domain validity
    const domainCheck = await fetch(
        `https://api.myemailverifier.com/validate-domain`,
        {
            method: 'POST',
            body: JSON.stringify({
                domain: domain,
                api_key: API_KEY
            })
        }
    );
    
    const domainData = await domainCheck.json();
    
    if (!domainData.is_valid) {
        return { is_valid: false, error_code: 4 };
    }
    
    // Proceed with email verification
    // ...
}
```

---

## Debug Mode

Enable debug mode to get detailed error information:

```bash
# In API request
curl -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -H "X-Debug: true" \
  -d '{
    "email": "user@example.com",
    "api_key": "your_api_key"
  }'
```

**Debug Response:**
```json
{
  "error_code": 5,
  "message": "SMTP verification failed",
  "debug": {
    "domain": "example.com",
    "mx_servers": ["mail.example.com"],
    "smtp_response": "550 User not found",
    "timestamp": "2024-02-19T10:30:00Z"
  }
}
```

---

## Getting Help

- 📖 [API Reference](API_REFERENCE.md)
- 📚 [Getting Started](GETTING_STARTED.md)
- 💬 Live Support: support@myemailverifier.com
- 🐛 [Report Bugs](https://github.com/myemailverifier/api/issues)

---

**Last Updated:** February 2024
**API Version:** 1.0
