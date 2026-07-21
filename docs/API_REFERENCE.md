# API Reference

Complete API documentation for MyEmailVerifier.

## Base URLs

MyEmailVerifier provides two base URLs:

1. **Fast API (Recommended for AI/Automation)**
   ```
   https://api.myemailverifier.com
   ```
   - Optimized for speed and high-performance tasks
   - Best for single email validation
   - Default rate limit: 30 requests per minute (customizable based on plan)

2. **Client API (Comprehensive Suite)**
   ```
   https://client.myemailverifier.com
   ```
   - Full API suite including bulk operations
   - Single email validation, bulk upload, credits, file management
   - Same rate limiting: 30 requests per minute (default)

## Authentication

All API requests require an API key. You can obtain your API key from your [MyEmailVerifier Dashboard](https://client.myemailverifier.com/apis/settings).

### Authentication Methods

**Method 1: Query Parameter (GET requests)**
```
?apikey=YOUR_API_KEY
```

**Method 2: URL Path Parameter**
```
/verifier/validate_single/{email}/{apikey}
```

**Method 3: POST Form Data**
```
api_key=YOUR_API_KEY
```

## Rate Limiting

- **Default**: 30 requests per minute per API key
- **Custom Limits**: Available based on your credit plan and requirements

Rate limit headers are included in responses:
- `X-RateLimit-Limit`: Your rate limit
- `X-RateLimit-Remaining`: Remaining requests
- `X-RateLimit-Reset`: Time when limit resets

## Endpoints

### 1. Single Email Verification (Fast API)

**Endpoint:** `GET /api/validate_single.php`

**Base URL:** `https://api.myemailverifier.com`

**Description:** High-performance endpoint optimized for speed. Best for AI integrations and automation tasks.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| apikey | string | Yes | Your API key |
| email | string | Yes | Email address to verify |

**Example Request:**

```bash
curl \"https://api.myemailverifier.com/api/validate_single.php?apikey=YOUR_API_KEY&email=test@example.com\"
```

**Example Response:**

```json
{
  \"Address\": \"test@example.com\",
  \"catch_all\": \"false\",
  \"Status\": \"Valid\",
  \"Disposable_Domain\": \"false\",
  \"Role_Based\": \"true\",
  \"Free_Domain\": \"false\",
  \"Greylisted\": \"false\",
  \"Diagnosis\": \"Mailbox Exists and Active\"
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| Address | string | The email address verified |
| Status | string | `Valid`, `Invalid`, `Catch-all`, or `Unknown` |
| catch_all | string | \"true\" if domain accepts all emails |
| Disposable_Domain | string | \"true\" if temporary/disposable email |
| Role_Based | string | \"true\" if role-based (support@, info@, etc) |
| Free_Domain | string | \"true\" if free provider (Gmail, Yahoo, etc) |
| Greylisted | string | \"true\" if server uses greylisting |
| Diagnosis | string | Detailed diagnosis message |

---

### 2. Single Email Verification (Client API)

**Endpoint:** `GET /verifier/validate_single/{email}/{apikey}`

**Base URL:** `https://client.myemailverifier.com`

**Description:** Comprehensive email validation with same features as Fast API.

**Example Request:**

```bash
curl \"https://client.myemailverifier.com/verifier/validate_single/test@example.com/YOUR_API_KEY\"

**Description:** Verify multiple emails in a single request.

**Request Body:**

```json
{
  "emails": [
    "user1@example.com",
    "user2@example.com",
    "user3@example.com"
  ],
  "api_key": "your_api_key"
}
```

**Parameters:**

```

**Response:** Same as Fast API response format above.

---

### 3. Get Credit Balance

**Endpoint:** `GET /verifier/getcredits/{apikey}`

**Base URL:** `https://client.myemailverifier.com`

**Description:** Check your remaining API credits.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| apikey | string | Yes | Your API key |

**Example Request:**

```bash
curl "https://client.myemailverifier.com/verifier/getcredits/YOUR_API_KEY"
```

**Example Response:**

```json
{
  "credits": "7800"
}
```

---

### 4. Upload File for Bulk Verification

**Endpoint:** `POST /verifier/upload_file`

**Base URL:** `https://client.myemailverifier.com`

**Description:** Upload a TXT or CSV file containing emails for bulk verification.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| api_key | string | Yes | Your API key (POST form field) |
| filename | file | Yes | TXT or CSV file with emails |

**Example Request:**

```bash
curl -F "filename=@emails.txt" -F "api_key=YOUR_API_KEY" \
  "https://client.myemailverifier.com/verifier/upload_file"
```

**Example Response:**

```json
{
  "status": true,
  "file_name": "emails.txt",
  "file_id": 1670,
  "msg": "File uploaded successfully."
}
```

**Error Response:**

```json
{
  "status": false,
  "msg": "Invalid file format. Please upload TXT or CSV file."
}
```

---

### 5. Get File Information and Results

**Endpoint:** `GET /verifier/file_info/{apikey}/{fileid}`

**Base URL:** `https://client.myemailverifier.com`

**Description:** Get verification status and download links for uploaded files.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| emails | array | Yes | Array of email addresses (max 100 per request) |
| api_key | string | Yes | Your API key |
| format | string | No | Response format: json (default) or csv |

**Description:** Get verification status and download links for uploaded files.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| apikey | string | Yes | Your API key |
| fileid | integer | Yes | File ID from upload response |

**Example Request:**

```bash
curl "https://client.myemailverifier.com/verifier/file_info/YOUR_API_KEY/1670"
```

**Example Response:**

```json
{
  "upload_id": "1670",
  "file_name": "emails.txt",
  "file_path": "https://client.myemailverifier.com/downloadreport/csv/1670",
  "xls_file_path": "https://client.myemailverifier.com/downloadreport/xls/1670",
  "user_id": "26",
  "created_at": "2024-02-19 10:30:00",
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

**Status Values:**

- `processing` - File is being verified
- `finished` - Verification complete, ready for download
- `failed` - Verification failed (check error message)

**File Download:**

Once `ready_for_download` is `1` and `status` is `finished`:
- **CSV Download:** Use the `file_path` URL
- **Excel Download:** Use the `xls_file_path` URL

---

## Response Status Codes

| Code | Description |
|------|-------------|
| 200 | Success - Request completed successfully |
| 400 | Bad Request - Invalid parameters or missing required fields |
| 401 | Unauthorized - Invalid or missing API key |
| 403 | Forbidden - API key doesn't have permission (e.g., referer restriction) |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error - Server-side issue |

## Error Handling

### Rate Limit Error (429)

```json
{
  "status": false,
  "message": "Rate limit exceeded. You can make 30 requests per minute.",
  "error": "RATE_LIMIT_EXCEEDED"
}
```

### Invalid API Key (401)

```json
{
  "status": false,
  "message": "Invalid API key",
  "error": "INVALID_API_KEY"
}
```

### Insufficient Credits

```json
{
  "status": false,
  "message": "Insufficient credits. Please purchase more credits.",
  "error": "INSUFFICIENT_CREDITS"
}
```

## Best Practices

1. **Cache Results**: Cache validation results to avoid redundant API calls
2. **Batch Operations**: Use file upload for bulk verification (more efficient than individual calls)
3. **Error Handling**: Always implement proper error handling for rate limits and API errors
4. **Rate Limiting**: Monitor your usage and upgrade plan if hitting limits frequently
5. **API Key Security**: Never expose API keys in client-side code or public repositories
6. **Timeout Settings**: Set appropriate timeouts (10-30 seconds recommended)

## Intelligent Caching System

MyEmailVerifier uses an intelligent caching system with **millions of verified emails** for lightning-fast responses:

- **Cache Hit**: < 100ms response time
- **Cache Miss**: 3-30 seconds (full SMTP verification)
- **Cache Hit Rate**: Typically 70-90% for most use cases

The cache automatically updates when verifying new emails, benefiting all users.

---

## Deep Catch-All API

Standard verification can't confirm addresses on **catch-all** domains. This API scores each catch-all address individually to estimate whether a real mailbox is active.

| Action | Endpoint | Cost |
|--------|----------|------|
| Score one email (sync) | `GET /catchall/score/{email}/{apikey}` | 5 cr |
| Batch upload (async: upload → poll → download) | `POST /catchall/upload/{apikey}` → `GET /catchall/status/{apikey}/{job_id}` → `GET /catchall/download/{apikey}/{job_id}` | 5 cr / email |

Verdicts: `high_probability` (≥ 50) · `low_probability` (< 50) · `avoid_send`.

📖 **Full reference with request/response examples, batch flow, error codes and rate limits:** [Deep Catch-All API →](DEEP_CATCHALL_API.md)

---

## Lead Generation API

Find verified business contacts three ways — a plain-English **prompt**, a **name + company**, or just a **LinkedIn profile URL** — then reveal emails and phone numbers. Every email is confirmed deliverable before it's returned.

| Tool | Endpoint | Cost |
|------|----------|------|
| Prompt Search | `POST /leads/search/{apikey}` | 5 cr / search |
| LinkedIn Finder | `POST /leads/search/{apikey}` (structured fields) | 5 cr / search |
| Find by URL (async: submit → poll) | `POST /leads/linkedin-url/{apikey}` → `GET /leads/linkedin-url/{apikey}/{job_id}` | Free to submit; 5 cr if no match |
| Reveal contact | `POST /leads/reveal/{apikey}` | 10 cr (free re-reveal within 24 h) |
| Save / List / Delete | `POST` / `GET` / `DELETE /leads/saved/{apikey}` | Free |

📖 **Full reference with request/response examples, error codes and rate limits:** [Lead Generation API →](LEAD_GENERATION_API.md)

---

## Support

- **Documentation**: [https://github.com/myemailverifier/api](https://github.com/myemailverifier/api)
- **Dashboard**: [https://client.myemailverifier.com](https://client.myemailverifier.com)
- **Support Email**: support@myemailverifier.com
