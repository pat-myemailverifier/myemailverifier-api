# cURL Examples

Email verification examples using cURL command line tool.

## Installation

cURL is built-in on most systems. Check:
```bash
curl --version
```

If not installed:
```bash
# macOS
brew install curl

# Ubuntu/Debian
sudo apt-get install curl

# Windows
# Download from https://curl.se/download.html
```

## Examples

### 1. Single Email Verification

```bash
curl -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "api_key": "your_api_key"
  }'
```

### 2. Pretty-Print JSON Response

```bash
curl -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "api_key": "your_api_key"
  }' | jq '.'
```

### 3. Save Response to File

```bash
curl -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "api_key": "your_api_key"
  }' > result.json
```

### 4. Batch Email Verification

```bash
curl -X POST https://api.myemailverifier.com/verify-batch \
  -H "Content-Type: application/json" \
  -d '{
    "emails": [
      "user1@example.com",
      "user2@example.com",
      "user3@example.com"
    ],
    "api_key": "your_api_key"
  }'
```

### 5. Domain Validation

```bash
curl -X POST https://api.myemailverifier.com/validate-domain \
  -H "Content-Type: application/json" \
  -d '{
    "domain": "example.com",
    "api_key": "your_api_key"
  }'
```

### 6. Check Catch-all Domain

```bash
curl -X POST https://api.myemailverifier.com/check-catchall \
  -H "Content-Type: application/json" \
  -d '{
    "domain": "example.com",
    "api_key": "your_api_key"
  }'
```

### 7. Using Authorization Header

```bash
curl -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "email": "user@example.com"
  }'
```

### 8. Get Account Information

```bash
curl "https://api.myemailverifier.com/account?api_key=your_api_key"
```

### 9. With Verbose Output

```bash
curl -v -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "api_key": "your_api_key"
  }'
```

### 10. Set Custom User-Agent

```bash
curl -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -H "User-Agent: MyApp/1.0" \
  -d '{
    "email": "user@example.com",
    "api_key": "your_api_key"
  }'
```

## Using Environment Variables

### Store API Key in Variable

```bash
API_KEY="your_api_key"
EMAIL="user@example.com"

curl -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -d "{
    \"email\": \"$EMAIL\",
    \"api_key\": \"$API_KEY\"
  }"
```

### Load from .env File

```bash
# Create .env file
echo 'API_KEY=your_api_key' > .env
source .env

curl -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -d "{
    \"email\": \"user@example.com\",
    \"api_key\": \"$API_KEY\"
  }"
```

## Processing Results

### Extract Specific Field

```bash
curl -s -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "api_key": "your_api_key"
  }' | jq '.is_valid'
```

### Check if Email is Valid

```bash
response=$(curl -s -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "api_key": "your_api_key"
  }')

is_valid=$(echo $response | jq '.is_valid')

if [ "$is_valid" = "true" ]; then
  echo "Email is valid!"
else
  echo "Email is invalid!"
fi
```

### Loop Through Emails

```bash
emails=("user1@example.com" "user2@example.com" "user3@example.com")

for email in "${emails[@]}"
do
  echo "Checking: $email"
  curl -s -X POST https://api.myemailverifier.com/verify \
    -H "Content-Type: application/json" \
    -d "{
      \"email\": \"$email\",
      \"api_key\": \"$API_KEY\"
    }" | jq '.email, .is_valid'
done
```

## Useful Tools

### Pretty-Print with jq

```bash
# Install jq
# macOS: brew install jq
# Ubuntu: sudo apt-get install jq

curl -s https://api.myemailverifier.com/verify ... | jq '.'
```

### Convert to CSV

```bash
curl -s https://api.myemailverifier.com/verify-batch ... | jq -r '.results[] | [.email, .is_valid, .deliverability] | @csv'
```

### Monitor Rate Limits

```bash
curl -I -X POST https://api.myemailverifier.com/verify \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "api_key": "your_api_key"
  }' | grep -i "X-RateLimit"
```

## Troubleshooting

### Check Connection

```bash
curl -I https://api.myemailverifier.com
```

### Debug Request

```bash
curl -v -X POST https://api.myemailverifier.com/verify \
  --data-binary @data.json \
  -H "Content-Type: application/json"
```

### SSL Issues

```bash
# Disable SSL verification (not recommended for production)
curl -k -X POST https://api.myemailverifier.com/verify ...

# Or update certificates
curl --cacert /path/to/ca-bundle.crt ...
```

## More Information

- [API Reference](../../docs/API_REFERENCE.md)
- [Getting Started](../../docs/GETTING_STARTED.md)
- [Back to examples](../)
