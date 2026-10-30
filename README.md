# MyEmailVerifier API

Real-time email verification API to validate email addresses instantly and increase inbox delivery.

## 🚀 Features

- **Real-time Email Verification** - Verify emails instantly with 99.9% accuracy
- **Lead Generation** - Find verified business emails from a prompt, a name + company, or a LinkedIn profile URL (emails confirmed deliverable before they're returned) — see [Lead Generation API](docs/LEAD_GENERATION_API.md)
- **Deep Catch-All Check** - Individually score catch-all addresses that standard checks can't confirm — see [Deep Catch-All API](docs/DEEP_CATCHALL_API.md)
- **Bulk Email Validation** - Upload CSV/TXT files for bulk verification
- **Intelligent Caching** - Lightning-fast response times with smart caching system
- **Catch-all Detection** - Identify catch-all email addresses
- **Role-based Email Detection** - Detect role-based emails (support@, info@, admin@, etc.)
- **Disposable Domain Detection** - Identify temporary/disposable email addresses
- **Free Domain Detection** - Detect free email providers (Gmail, Yahoo, etc.)
- **SMTP Verification** - Deep SMTP-level verification for accuracy
- **API Rate Limiting** - Flexible rate limiting (30 req/min default, customizable)
- **Multiple Response Formats** - JSON, CSV, and Excel downloads
- **API Credit System** - Check credits and usage tracking
- **Free Daily Credits** - 100 free credits per day (requires phone verification for fair usage)
- **Accumulative Credits** - Monthly subscription credits add up, never expire

## 📋 API Endpoints Overview

MyEmailVerifier provides two base URLs:

1. **api.myemailverifier.com** - Fast single email validation (NEW optimized endpoint)
2. **client.myemailverifier.com** - Comprehensive API suite (validation, bulk upload, credits, reports)

## 📋 Quick Start

### Option 1: Fast Single Email Validation (Recommended for AI/Automation)

**Endpoint:** `https://api.myemailverifier.com/api/validate_single.php`

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

### Option 2: Comprehensive Email Validation

**Endpoint:** `https://client.myemailverifier.com/verifier/validate_single/{email}/{apikey}`

```bash
curl "https://client.myemailverifier.com/verifier/validate_single/test@example.com/YOUR_API_KEY"
```

### JavaScript Example
```javascript
const apiKey = 'YOUR_API_KEY';
const email = 'test@example.com';

fetch(`https://api.myemailverifier.com/api/validate_single.php?apikey=${apiKey}&email=${email}`)
  .then(response => response.json())
  .then(data => {
    console.log('Status:', data.Status);
    console.log('Diagnosis:', data.Diagnosis);
  })
```

### Python Example
```python
import requests

api_key = 'YOUR_API_KEY'
email = 'test@example.com'

# Option 1: Fast API endpoint
response = requests.get(
    f'https://api.myemailverifier.com/api/validate_single.php',
    params={'apikey': api_key, 'email': email}
)
result = response.json()
print(f"Status: {result['Status']}")
print(f"Diagnosis: {result['Diagnosis']}")
```

### PHP Example
```php
<?php
$apiKey = 'YOUR_API_KEY';
$email = 'test@example.com';

// Option 1: Fast API endpoint
$url = "https://api.myemailverifier.com/api/validate_single.php?apikey={$apiKey}&email={$email}";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);

$response = curl_exec($ch);
$result = json_decode($response, true);

echo "Status: " . $result['Status'] . "\n";
echo "Diagnosis: " . $result['Diagnosis'] . "\n";

curl_close($ch);
?>
```

## 📚 Documentation

- [Getting Started](docs/GETTING_STARTED.md) - Complete setup guide
- [API Reference](docs/API_REFERENCE.md) - Full API documentation
- [Authentication](docs/AUTHENTICATION.md) - API key management
- [Integrations](docs/INTEGRATIONS.md) - Zapier and third-party integrations
- [Free Tools](docs/FREE_TOOLS.md) - Available free verification tools
- [Error Codes](docs/ERROR_CODES.md) - API error codes reference
- [FAQ](docs/FAQ.md) - Frequently asked questions

## 💻 Code Examples

Browse language-specific examples:
- [Node.js Examples](examples/nodejs/)
- [Python Examples](examples/python/)
- [PHP Examples](examples/php/)
- [JavaScript Examples](examples/javascript/)
- [cURL Examples](examples/curl/)

## 📋 Additional Endpoints

### Get Your Credit Balance
```bash
curl "https://client.myemailverifier.com/verifier/getcredits/YOUR_API_KEY"
```

**Response:**
```json
{
  "credits": "7800"
}
```

### Upload File for Bulk Verification
```bash
curl -F "filename=@emails.txt" -F "api_key=YOUR_API_KEY" \
  "https://client.myemailverifier.com/verifier/upload_file"
```

**Response:**
```json
{
  "status": true,
  "file_name": "emails.txt",
  "file_id": 1670,
  "msg": "File uploaded successfully."
}
```

### Get File Info and Download Results
```bash
curl "https://client.myemailverifier.com/verifier/file_info/YOUR_API_KEY/FILE_ID"
```

**Response:**
```json
{
  "upload_id": "1669",
  "file_name": "test.xlsx",
  "file_path": "https://client.myemailverifier.com/download/csv/12345?expires=1795845308&signature=…",
  "xls_file_path": "https://client.myemailverifier.com/download/xls/12345?expires=1795845308&signature=…",
  "created_at": "2019-09-09 00:17:23",
  "ready_for_download": "1",
  "valid": "27",
  "invalid": "2",
  "catchall": 0,
  "unknown": 0,
  "duplicates": 0,
  "spam_trap": 10,
  "toxic_domains": 0,
  "credit_used": "29",
  "total": "31",
  "status": "finished"
}
```

## 🔑 API Key

Sign up at [MyEmailVerifier](https://myemailverifier.com) to get your free API key.

## 📊 Response Format

```json
{
  "email": "user@example.com",
  "is_valid": true,
  "is_catchall": false,
  "is_role_based": false,
  "domain_valid": true,
  "mx_records": true,
  "smtp_check": true,
  "deliverability": "safe",
  "verification_time": 2.5,
  "error_code": 0
}
```

## 🛠️ Free Tools

- Email List Checker
- Batch Email Verification
- Domain Validator
- Catch-all Detector

[View all Free Tools](docs/FREE_TOOLS.md)

## 🚀 Getting Started

1. **Create an Account** - Sign up at [MyEmailVerifier.com](https://myemailverifier.com)
2. **Verify Your Phone** - Required for 100 free daily credits (fair usage)
3. **Get Your API Key** - Found in your dashboard under API Settings
4. **Start Verifying** - Use any of our code examples
5. **Monitor Usage** - Check your dashboard for stats and remaining credits

## 💼 Integrations

MyEmailVerifier supports integrations with popular platforms:
- Zapier
- Make/Integromat
- IFTTT
- Custom Webhooks
- More integrations available

[View Integration Guide](docs/INTEGRATIONS.md)

## 📈 Plans & Pricing

Choose the plan that fits your needs:

### Free Plan
- **100 credits per day** (requires phone verification for fair usage)
- Access to all API endpoints
- Perfect for testing and small projects

### Monthly Subscription Plans
- Credits **add up monthly** (accumulative, never reset)
- Unused credits carry over to next month
- Higher credit packages available
- Priority support on higher tiers

### Pay-as-you-go
- Purchase credits anytime
- Credits never expire
- No monthly commitment

**Note:** All plans use an accumulative credit system - credits are added to your balance each month, not reset.

## 🆘 Support

- 📧 Email: support@myemailverifier.com
- 💬 Live Chat: Available on our website
- 📖 Documentation: See docs folder
- 🐛 Report Issues: [GitHub Issues](https://github.com/myemailverifier/api/issues)

## 📄 License

This repository is licensed under the MIT License - see LICENSE file for details.

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines for more information.

---

**Start verifying emails today and improve your email delivery rates!**
