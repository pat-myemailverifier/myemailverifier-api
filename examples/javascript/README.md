# JavaScript Examples

Complete examples for using MyEmailVerifier API with JavaScript (Browser & Node.js).

## Browser Usage

```html
<script>
const verifyEmail = async (email) => {
  const response = await fetch('https://api.myemailverifier.com/verify', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      email: email,
      api_key: 'your_api_key'
    })
  });
  
  const data = await response.json();
  console.log(data);
  return data;
};

// Use it
verifyEmail('user@example.com');
</script>
```

## Node.js Usage

```javascript
const axios = require('axios');

const verifyEmail = async (email) => {
  const response = await axios.post(
    'https://api.myemailverifier.com/verify',
    {
      email: email,
      api_key: process.env.MYEMAILVERIFIER_API_KEY
    }
  );
  
  console.log(response.data);
  return response.data;
};

verifyEmail('user@example.com');
```

## Examples

- `verify_single.html` - Browser-based single email verification
- `verify_batch.html` - Batch verification in browser
- `verify_single.js` - Node.js single email
- `verify_batch.js` - Node.js batch verification
- `async_promise_examples.js` - Various async patterns

## Running Examples

### Browser
```bash
# Open in browser
open verify_single.html

# Or use a local server
python -m http.server 8000
# Visit http://localhost:8000/verify_single.html
```

### Node.js
```bash
npm install axios

node verify_single.js
node verify_batch.js
node async_promise_examples.js
```

## More Information

- [Back to examples](../)
- [API Reference](../../docs/API_REFERENCE.md)
- [Getting Started](../../docs/GETTING_STARTED.md)
