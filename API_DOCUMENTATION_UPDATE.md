# MyEmailVerifier API Documentation Update

## Summary

This documentation has been completely updated to reflect the **actual production API endpoints** used by MyEmailVerifier, based on the live client implementation at `client.myemailverifier.com`.

## Key Changes

### 1. Base URLs Clarification

**PREVIOUS (Incorrect):**
- Single base URL: `https://api.myemailverifier.com`
- All endpoints used POST with JSON body

**UPDATED (Correct):**
- **Fast API**: `https://api.myemailverifier.com` - Single email validation only
- **Client API**: `https://client.myemailverifier.com` - Full API suite (validation, bulk, credits, downloads)

### 2. API Endpoint Updates

#### Single Email Validation

**Old (Incorrect):**
```bash
POST https://api.myemailverifier.com/verify
Content-Type: application/json
{
  "email": "test@example.com",
  "api_key": "YOUR_API_KEY"
}
```

**New (Correct) - Option 1:**
```bash
GET https://api.myemailverifier.com/api/validate_single.php?apikey=YOUR_API_KEY&email=test@example.com
```

**New (Correct) - Option 2:**
```bash
GET https://client.myemailverifier.com/verifier/validate_single/test@example.com/YOUR_API_KEY
```

### 3. Response Format Changes

**Old Response Format:**
```json
{
  "email": "test@example.com",
  "is_valid": true,
  "is_catchall": false,
  "is_role_based": false,
  "domain_valid": true,
  "mx_records": true,
  "smtp_check": true,
  "deliverability": "safe",
  "verification_time": 2.5,
  "error_code": 0,
  "message": "Email is valid"
}
```

**New Response Format:**
```json
{
  "Address": "test@example.com",
  "catch_all": "false",
  "Status": "Valid",
  "Disposable_Domain": "false",
  "Role_Based": "true",
  "Free_Domain": "false",
  "Greylisted": "false",
  "Diagnosis": "Mailbox Exists and Active"
}
```

### 4. New Endpoints Added

#### Get Credits
```bash
GET https://client.myemailverifier.com/verifier/getcredits/YOUR_API_KEY
```

Response:
```json
{
  "credits": "7800"
}
```

#### Upload File for Bulk Verification
```bash
POST https://client.myemailverifier.com/verifier/upload_file
Content-Type: multipart/form-data

filename=@emails.txt
api_key=YOUR_API_KEY
```

Response:
```json
{
  "status": true,
  "file_name": "emails.txt",
  "file_id": 1670,
  "msg": "File uploaded successfully."
}
```

#### Get File Info and Results
```bash
GET https://client.myemailverifier.com/verifier/file_info/YOUR_API_KEY/FILE_ID
```

Response:
```json
{
  "upload_id": "1670",
  "file_name": "emails.txt",
  "file_path": "https://client.myemailverifier.com/download/csv/1670?expires=1795845308&signature=…",
  "xls_file_path": "https://client.myemailverifier.com/download/xls/1670?expires=1795845308&signature=…",
  "ready_for_download": "1",
  "valid": "850",
  "invalid": "120",
  "catchall": "30",
  "unknown": "10",
  "duplicates": "50",
  "spam_trap": "5",
  "toxic_domains": "2",
  "credit_used": "1017",
  "total": "1067",
  "status": "finished"
}
```

## Files Updated

### Documentation Files
- ✅ `README.md` - Updated with correct endpoints and examples
- ✅ `docs/API_REFERENCE.md` - Complete API reference with all 5 endpoints
- ✅ `docs/GETTING_STARTED.md` - Updated quickstart guide with real examples

### Code Examples
- ✅ `examples/php/verify_single.php` - Updated to use actual API
- ✅ `examples/nodejs/verify-single.js` - Updated to use actual API
- ✅ `examples/python/verify_single.py` - Updated to use actual API
- ✅ `examples/python/verify_batch.py` - Complete bulk verification example
- ✅ `examples/javascript/verify_single.html` - Updated HTML/JavaScript example

## Key Features Documented

### 1. Intelligent Caching
- **Millions of verified emails** cached for instant results
- **< 100ms response time** for cached emails
- **70-90% cache hit rate** for typical use cases
- Automatic cache population on new verifications

### 2. Rate Limiting
- **Default**: 30 requests per minute per API key
- **Restricted Keys**: 3-5 requests per day (demo/testing)
- **Bypass Keys**: Unlimited requests (enterprise)
- **Custom Limits**: Available based on credit plan

### 3. Response Fields
- **Status**: `Valid`, `Invalid`, `Catch-all`, `Unknown`
- **Disposable_Domain**: Detect temporary email services
- **Role_Based**: Detect role emails (support@, info@, etc)
- **Free_Domain**: Detect free providers (Gmail, Yahoo, etc)
- **Greylisted**: Server uses greylisting (may need retry)
- **Diagnosis**: Detailed explanation of validation result

### 4. Bulk Verification Workflow
1. Upload TXT/CSV file → Get `file_id`
2. Poll `file_info` endpoint until `status = "finished"`
3. Download CSV or Excel from provided URLs

## Authentication Methods

### Method 1: Query Parameter (Recommended for Fast API)
```
?apikey=YOUR_API_KEY
```

### Method 2: URL Path Parameter (Client API)
```
/verifier/validate_single/{email}/{apikey}
```

### Method 3: POST Form Data (File Upload)
```
api_key=YOUR_API_KEY
```

## Error Handling

### HTTP Status Codes
- **200** - Success
- **400** - Bad Request (invalid parameters)
- **401** - Unauthorized (invalid API key)
- **403** - Forbidden (referer restriction or insufficient permissions)
- **429** - Too Many Requests (rate limit exceeded)
- **500** - Internal Server Error

### Example Error Responses

**Rate Limit Exceeded:**
```json
{
  "status": false,
  "message": "Rate limit exceeded. You can make 30 requests per minute.",
  "error": "RATE_LIMIT_EXCEEDED"
}
```

**Invalid API Key:**
```json
{
  "status": false,
  "message": "Invalid API key",
  "error": "INVALID_API_KEY"
}
```

**Insufficient Credits:**
```json
{
  "status": false,
  "message": "Insufficient credits. Please purchase more credits.",
  "error": "INSUFFICIENT_CREDITS"
}
```

## Best Practices

1. **Use Fast API for Single Emails**: Optimized for speed and AI integrations
2. **Use File Upload for Bulk**: More efficient than individual API calls
3. **Implement Error Handling**: Always handle rate limits and API errors
4. **Cache Results**: Don't verify the same email multiple times
5. **Monitor Credits**: Check credit balance regularly
6. **Secure API Keys**: Never expose in client-side code or public repos
7. **Set Timeouts**: Use 10-30 second timeouts for API requests

## Migration Guide

If you're using the old (incorrect) documentation:

### Before (Incorrect):
```python
response = requests.post(
    'https://api.myemailverifier.com/verify',
    json={'email': email, 'api_key': api_key}
)
```

### After (Correct):
```python
response = requests.get(
    'https://api.myemailverifier.com/api/validate_single.php',
    params={'apikey': api_key, 'email': email}
)
```

### Response Field Mapping:
| Old Field | New Field |
|-----------|-----------|
| `email` | `Address` |
| `is_valid` | `Status` (Value: "Valid"/"Invalid") |
| `is_catchall` | `catch_all` (String: "true"/"false") |
| `is_role_based` | `Role_Based` (String: "true"/"false") |
| `deliverability` | `Status` + `Diagnosis` |
| `message` | `Diagnosis` |

## Support and Resources

- **GitHub Repository**: [myemailverifier/api](https://github.com/myemailverifier/api)
- **Dashboard**: [client.myemailverifier.com](https://client.myemailverifier.com)
- **API Settings**: [client.myemailverifier.com/apis/settings](https://client.myemailverifier.com/apis/settings)
- **Support Email**: support@myemailverifier.com

## Testing

All examples have been tested against the production API and work correctly with:
- ✅ Single email validation (both Fast and Client APIs)
- ✅ Credit balance checking
- ✅ File upload for bulk verification
- ✅ File status polling and result download
- ✅ Error handling for rate limits and invalid API keys

## Notes

- All documentation now matches the **live production implementation**
- Code examples tested and verified working
- Response formats match actual API responses
- Bulk verification workflow documented with complete examples
- Intelligent caching system for fast responses

---

**Last Updated**: February 19, 2026
**Verified Against**: Production API at client.myemailverifier.com
