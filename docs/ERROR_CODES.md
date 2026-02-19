# Error Codes Reference

Complete list of error codes and their meanings.

## Verification Status Codes

### ✅ Success (Code: 0)

**Status:** Email Verified
**Meaning:** Email address is valid and verified successfully
**Action:** Safe to add to mailing list

```json
{
  "error_code": 0,
  "message": "Email is valid and safe to send",
  "deliverability": "safe"
}
```

---

### ❌ Invalid Email (Code: 1)

**Status:** Invalid Email
**Meaning:** Email address format is invalid or doesn't exist
**Causes:**
- Malformed email syntax
- Domain doesn't exist
- Invalid characters
- Email doesn't exist on domain

**Action:** Remove from list or prompt user to correct

```json
{
  "error_code": 1,
  "message": "Email address is invalid",
  "deliverability": "invalid"
}
```

---

### 🔄 Catch-all Domain (Code: 2)

**Status:** Catch-all Address
**Meaning:** Domain accepts all emails (catch-all configuration)
**Causes:**
- Domain is configured to accept any email
- Can't verify if specific email exists
- Generic catch-all servers

**Action:** Accept with caution or follow up verification

```json
{
  "error_code": 2,
  "message": "Email is a catch-all address",
  "is_catchall": true,
  "deliverability": "risky"
}
```

---

### 👔 Role-Based Email (Code: 3)

**Status:** Role-Based Address
**Meaning:** Email is a generic role address (support@, info@, admin@, etc.)
**Causes:**
- Generic inbox shared by multiple people
- Department-wide email
- No specific person assigned

**Action:** Can send but may be less targeted

```json
{
  "error_code": 3,
  "message": "Email is role-based (support@, info@, etc)",
  "is_role_based": true,
  "deliverability": "safe"
}
```

---

### 🌐 Domain Validation Error (Code: 4)

**Status:** Domain Error
**Meaning:** Domain is invalid or doesn't exist
**Causes:**
- Domain doesn't exist
- Domain is suspended
- Domain has no MX records
- DNS lookup failed

**Action:** Invalid domain - remove email

```json
{
  "error_code": 4,
  "message": "Domain validation failed",
  "domain_valid": false,
  "deliverability": "invalid"
}
```

---

### 📧 SMTP Verification Error (Code: 5)

**Status:** SMTP Error
**Meaning:** SMTP verification failed
**Causes:**
- Mail server rejected connection
- Temporary server error
- Timeout during verification
- Server blocked our IP

**Action:** Retry later or mark as unverifiable

```json
{
  "error_code": 5,
  "message": "SMTP verification failed",
  "smtp_check": false,
  "deliverability": "risky"
}
```

---

## API Error Codes

### API Error (Code: 100)

**Status:** API Error
**Meaning:** General API error
**Causes:**
- Server error
- Request processing failed
- Internal error

**Response:**
```json
{
  "error_code": 100,
  "message": "API error",
  "status": "error"
}
```

---

### Authentication Error (Code: 101)

**Status:** Authentication Failed
**Meaning:** API key is invalid, expired, or missing
**Causes:**
- Invalid API key
- API key revoked
- API key expired
- Missing API key

**Solution:**
1. Check API key format
2. Verify key is active in dashboard
3. Generate new key if needed
4. Never commit keys to version control

**Response:**
```json
{
  "error_code": 101,
  "message": "Invalid API key",
  "status": "error"
}
```

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
