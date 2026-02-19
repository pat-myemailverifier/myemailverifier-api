# Installation Guide

Get started using MyEmailVerifier in your project.

## System Requirements

- Node.js 14+ (for JavaScript)
- Python 3.6+ (for Python)
- PHP 7.2+ (for PHP)
- cURL (for command line)
- Internet connection for API access

## Quick Installation

### Option 1: Using npm (Node.js)

```bash
npm install myemailverifier
```

### Option 2: Using pip (Python)

```bash
pip install myemailverifier
```

### Option 3: Using composer (PHP)

```bash
composer require myemailverifier/api
```

### Option 4: cURL (Command Line)

No installation needed! Just use cURL commands.

---

## Setup by Language

### Node.js / JavaScript

#### Installation

```bash
npm install myemailverifier
```

#### Basic Setup

```javascript
const MyEmailVerifier = require('myemailverifier');

const verifier = new MyEmailVerifier('your_api_key');

// Verify single email
verifier.verify('user@example.com')
  .then(result => console.log(result))
  .catch(error => console.error(error));
```

#### Configuration

```javascript
const options = {
  apiKey: 'your_api_key',
  baseUrl: 'https://api.myemailverifier.com',
  timeout: 10000,
  retries: 3
};

const verifier = new MyEmailVerifier(options);
```

---

### Python

#### Installation

```bash
pip install myemailverifier
```

#### Basic Setup

```python
from myemailverifier import EmailVerifier

verifier = EmailVerifier('your_api_key')

# Verify single email
result = verifier.verify('user@example.com')
print(result)
```

#### Configuration

```python
from myemailverifier import EmailVerifier

verifier = EmailVerifier(
    api_key='your_api_key',
    base_url='https://api.myemailverifier.com',
    timeout=10,
    retries=3
)
```

---

### PHP

#### Installation

Using Composer:
```bash
composer require myemailverifier/api
```

#### Basic Setup

```php
<?php
require 'vendor/autoload.php';

use MyEmailVerifier\EmailVerifier;

$verifier = new EmailVerifier('your_api_key');

// Verify single email
$result = $verifier->verify('user@example.com');
print_r($result);
?>
```

#### Manual Installation

Without Composer:
```php
<?php
require 'src/EmailVerifier.php';

$verifier = new \MyEmailVerifier\EmailVerifier('your_api_key');
$result = $verifier->verify('user@example.com');
print_r($result);
?>
```

---

### cURL / Command Line

No installation required! Use your terminal:

```bash
curl -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "api_key": "your_api_key"
  }'
```

---

## Environment Variables

### Create .env File

```env
# .env
MYEMAILVERIFIER_API_KEY=sk_live_your_api_key_here
MYEMAILVERIFIER_BASE_URL=https://api.myemailverifier.com
```

### Add to .gitignore

```gitignore
.env
.env.local
.env.*.local
```

### Load Environment Variables

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
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();
$apiKey = $_ENV['MYEMAILVERIFIER_API_KEY'];
?>
```

---

## Verify Installation

### Node.js

```javascript
const MyEmailVerifier = require('myemailverifier');
const verifier = new MyEmailVerifier('sk_test_test1234567890123456789test');

verifier.verify('test@example.com')
  .then(result => console.log('✅ Connection successful!', result))
  .catch(error => console.error('❌ Error:', error));
```

### Python

```python
from myemailverifier import EmailVerifier

verifier = EmailVerifier('sk_test_test1234567890123456789test')
result = verifier.verify('test@example.com')

if result.get('is_valid'):
    print('✅ Connection successful!')
else:
    print('❌ Error:', result.get('message'))
```

### PHP

```php
<?php
require 'vendor/autoload.php';
use MyEmailVerifier\EmailVerifier;

$verifier = new EmailVerifier('sk_test_test1234567890123456789test');
$result = $verifier->verify('test@example.com');

if ($result['is_valid']) {
    echo '✅ Connection successful!';
} else {
    echo '❌ Error: ' . $result['message'];
}
?>
```

### cURL

```bash
curl -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "api_key": "sk_test_test1234567890123456789test"
  }'
```

Expected response:
```json
{
  "email": "test@example.com",
  "is_valid": true,
  "error_code": 0,
  "message": "Email is valid"
}
```

---

## Troubleshooting Installation

### Issue: "Module not found"

**Solution:**
```bash
# Node.js
npm install myemailverifier

# Python
pip install myemailverifier --upgrade

# PHP
composer require myemailverifier/api
```

### Issue: "API Key not recognized"

**Solution:**
1. Copy API key from dashboard
2. Check for extra spaces in key
3. Use test key to verify: `sk_test_test1234567890123456789test`
4. Generate new key in dashboard

### Issue: "Connection timeout"

**Solution:**
1. Check internet connection
2. Increase timeout value:
   ```python
   verifier = EmailVerifier(api_key, timeout=20)
   ```
3. Check firewall/proxy settings

### Issue: "SSL Certificate Error"

**Solution:**
```bash
# Python
pip install certifi --upgrade

# Node.js
npm install --save node-fetch@2
```

---

## Next Steps

After successful installation:

1. ✅ [Getting Started Guide](GETTING_STARTED.md)
2. ✅ [API Reference](API_REFERENCE.md)
3. ✅ View [Code Examples](../examples/)
4. ✅ Check [Integrations](INTEGRATIONS.md)

---

## Support

Having trouble? We're here to help!

- 📧 support@myemailverifier.com
- 💬 Live chat on myemailverifier.com
- 📖 [Documentation](../)
- 🐛 [GitHub Issues](https://github.com/myemailverifier/api/issues)

---

**Ready to verify emails? Let's go!**
