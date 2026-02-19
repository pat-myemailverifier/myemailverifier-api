# Node.js Examples

Complete examples for using MyEmailVerifier API with Node.js.

## Installation

```bash
npm install myemailverifier axios
```

Or:
```bash
npm install myemailverifier
```

## Basic Usage

See the example files in this directory:

- `verify-single.js` - Verify a single email
- `verify-batch.js` - Verify multiple emails
- `domain-validation.js` - Validate domain
- `error-handling.js` - Handle errors properly
- `async-batch.js` - Async batch processing
- `express-integration.js` - Express.js integration

## Quick Start

```javascript
const axios = require('axios');

const API_KEY = process.env.MYEMAILVERIFIER_API_KEY;
const BASE_URL = 'https://api.myemailverifier.com';

async function verifyEmail(email) {
  try {
    const response = await axios.post(`${BASE_URL}/verify`, {
      email: email,
      api_key: API_KEY
    });
    
    console.log('Result:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

verifyEmail('user@example.com');
```

## Configuration

Set environment variables:
```bash
export MYEMAILVERIFIER_API_KEY="your_api_key"
node verify-single.js
```

Or use `.env` file:
```env
MYEMAILVERIFIER_API_KEY=your_api_key
```

Load in your code:
```javascript
require('dotenv').config();
const API_KEY = process.env.MYEMAILVERIFIER_API_KEY;
```

## Running Examples

```bash
# Single email verification
node verify-single.js

# Batch verification
node verify-batch.js

# Domain validation
node domain-validation.js

# Error handling
node error-handling.js

# Express integration
node express-integration.js
```

## More Information

- [Back to examples](../)
- [API Reference](../../docs/API_REFERENCE.md)
- [Getting Started](../../docs/GETTING_STARTED.md)
