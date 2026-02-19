# Authentication Guide

Learn how to authenticate with the MyEmailVerifier API.

## API Key Authentication

All API requests require authentication using your API key.

### Getting Your API Key

1. Log in to your [MyEmailVerifier Dashboard](https://myemailverifier.com/dashboard)
2. Navigate to **Settings** → **API Keys**
3. Click **Create New API Key** or copy your existing key
4. Keep your API key secure and never share it

### Using Your API Key

#### Method 1: In Request Body (Recommended)

```json
{
  "email": "user@example.com",
  "api_key": "sk_live_abc123xyz"
}
```

#### Method 2: Authorization Header

```
POST /verify HTTP/1.1
Authorization: Bearer sk_live_abc123xyz
Content-Type: application/json

{
  "email": "user@example.com"
}
```

#### Method 3: Query Parameter

```
GET /account?api_key=sk_live_abc123xyz
```

## API Key Format

MyEmailVerifier API keys follow this format:

```
sk_[live|test]_[32 character random string]
```

- `sk_live_` - Production API key
- `sk_test_` - Test/development API key

## Test API Key

Use the test API key for development and testing without consuming quota:

```
sk_test_test1234567890123456789test
```

## Managing API Keys

### In Your Dashboard

1. Go to **Settings** → **API Keys**
2. View all your API keys
3. Create new keys for different applications
4. Revoke keys you no longer need
5. Rotate keys periodically for security

### Key Permissions

Each API key can be configured with specific permissions:

- **Read** - View account info and verification results
- **Execute** - Perform email verification
- **Admin** - Manage keys and account settings

## Security Best Practices

### ✅ DO's

- ✅ Store API keys in environment variables
- ✅ Use different keys for different projects
- ✅ Rotate keys periodically (every 90 days)
- ✅ Use test keys for development
- ✅ Revoke old/unused keys
- ✅ Monitor API key usage

### ❌ DON'Ts

- ❌ Commit API keys to version control
- ❌ Share keys with team members directly
- ❌ Use production keys in development
- ❌ Expose keys in client-side code
- ❌ Use the same key for multiple projects
- ❌ Log or print API keys

## Environment Variables

### Store Your Key Safely

Create a `.env` file (add to `.gitignore`):

```env
MYEMAILVERIFIER_API_KEY=sk_live_abc123xyz
MYEMAILVERIFIER_BASE_URL=https://api.myemailverifier.com
```

### Load in Your Application

**Node.js:**
```javascript
require('dotenv').config();
const apiKey = process.env.MYEMAILVERIFIER_API_KEY;
```

**Python:**
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('MYEMAILVERIFIER_API_KEY')
```

**PHP:**
```php
<?php
require 'vendor/autoload.php';
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();
$apiKey = $_ENV['MYEMAILVERIFIER_API_KEY'];
?>
```

## Error Handling

### Invalid API Key

```json
{
  "error_code": 101,
  "message": "Invalid API key",
  "status": "error"
}
```

### Missing API Key

```json
{
  "error_code": 104,
  "message": "Missing API key parameter",
  "status": "error"
}
```

### Expired API Key

```json
{
  "error_code": 101,
  "message": "API key has expired",
  "status": "error"
}
```

## Troubleshooting

### "Invalid API Key" Error

1. Check if key is correctly copied (no extra spaces)
2. Verify you're using the correct API base URL
3. Ensure the key hasn't been revoked
4. Try regenerating the key in your dashboard

### "Rate Limit Exceeded" Error

1. Check your plan's rate limits
2. Implement exponential backoff retry
3. Contact support for higher limits
4. Use batch endpoints for multiple verifications

### Authentication Not Working

1. Check you're using the correct authentication method
2. Verify API key format
3. Check that key is active (not revoked)
4. Ensure Content-Type header is set correctly

## Support

For authentication issues:
- 📧 Email: support@myemailverifier.com
- 💬 Live chat: Available on myemailverifier.com
- 📖 Documentation: See [Getting Started](GETTING_STARTED.md)
