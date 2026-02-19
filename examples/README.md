# Code Examples

Complete code examples for integrating MyEmailVerifier API with your application.

## 📚 Available Examples

### Node.js
Real-time email verification with Node.js
- Single email verification
- Batch email processing
- Domain validation
- Error handling
- Express.js integration

[View Node.js Examples →](nodejs/)

### Python
Python integration for email verification
- Single email verification
- Batch verification
- CSV file processing
- Domain validation
- Error handling

[View Python Examples →](python/)

### PHP
PHP integration with cURL
- Single email verification
- Batch verification
- Domain validation
- WordPress integration (coming soon)

[View PHP Examples →](php/)

### JavaScript
Browser and Node.js JavaScript examples
- Single email verification (HTML page)
- Batch verification
- Async/await patterns
- Promise-based examples
- Error handling

[View JavaScript Examples →](javascript/)

### cURL
Command-line examples using cURL
- Single email verification
- Batch verification
- Domain validation
- Shell scripts
- Processing results with jq

[View cURL Examples →](curl/)

---

## 🚀 Quick Start by Language

### Node.js
```bash
npm install myemailverifier
node examples/nodejs/verify-single.js
```

### Python
```bash
pip install requests python-dotenv
python examples/python/verify_single.py
```

### PHP
```bash
php examples/php/verify_single.php
```

### cURL
```bash
curl -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "api_key": "your_key"}'
```

### Browser
```html
<!-- Open examples/javascript/verify_single.html in your browser -->
```

---

## 📋 Example Structure

Each language directory contains:
- **README.md** - Setup and usage guide
- **Example files** - Working code examples
- **Configuration examples** - Environment setup
- **.env.example** - Environment variable template

---

## 🔑 API Key

Get your free API key:
1. Sign up at [MyEmailVerifier.com](https://myemailverifier.com)
2. Go to Dashboard → API Keys
3. Copy your API key
4. Use in examples (replace `your_api_key`)

**Test Key:**
```
sk_test_test1234567890123456789test
```

---

## 📖 Documentation

- [API Reference](../docs/API_REFERENCE.md) - Complete API documentation
- [Getting Started](../docs/GETTING_STARTED.md) - Step-by-step setup guide
- [Authentication](../docs/AUTHENTICATION.md) - API key management
- [Error Codes](../docs/ERROR_CODES.md) - Error reference
- [Integrations](../docs/INTEGRATIONS.md) - Third-party integrations

---

## 🛠️ Common Tasks

### Verify Single Email

All languages support this. See your language directory.

```python
# Python
result = verify_email('user@example.com')
print(result['is_valid'])
```

### Batch Verify Multiple Emails

```python
# Python
results = verify_batch([
  'user1@example.com',
  'user2@example.com',
  'user3@example.com'
])
```

### Validate Domain

```bash
# cURL
curl -X POST https://api.myemailverifier.com/validate-domain \
  -d '{"domain": "example.com", "api_key": "key"}'
```

### Check Catch-all Domain

All examples support catch-all detection. Check error code 2.

### Handle Errors

All examples include error handling patterns:

```javascript
// JavaScript
try {
  const result = await verifyEmail(email);
  if (result.error_code === 0) {
    // Email is valid
  } else {
    // Handle error
  }
} catch (error) {
  // Network or API error
}
```

---

## 💡 Tips

1. **Environment Variables** - Store API keys securely
2. **Error Handling** - Implement retry logic for reliability
3. **Rate Limiting** - Use batch endpoints for multiple emails
4. **Caching** - Store recent results to reduce API calls
5. **Logging** - Log verification results for debugging

---

## 🔗 Integration Examples

Check the [Integrations Guide](../docs/INTEGRATIONS.md) for:
- Zapier integration
- Make (Integromat) setup
- Mailchimp integration
- Salesforce integration
- HubSpot integration
- Webhooks

---

## ❓ Help

- 📖 Read the [documentation](../docs/)
- 💬 [Live support](https://myemailverifier.com/support)
- 📧 support@myemailverifier.com
- 🐛 [Report issues](https://github.com/myemailverifier/api/issues)

---

**Choose your language above and get started in minutes!**
