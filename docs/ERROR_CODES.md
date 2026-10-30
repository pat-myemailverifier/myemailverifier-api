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
- Demo key used on the Deep Catch-All or Lead Generation API (`DEMO_KEY_NOT_ALLOWED`)
- Account suspended (`ACCOUNT_BLOCKED` on the Deep Catch-All and Lead Generation APIs)
- Account on hold until a payment is verified (`PAYMENT_VERIFICATION_REQUIRED`)
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
