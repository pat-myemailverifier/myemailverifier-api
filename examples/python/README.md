# Python Examples

Complete examples for using MyEmailVerifier API with Python.

## Installation

```bash
pip install requests python-dotenv
```

## Basic Usage

See the example files in this directory:

- `verify_single.py` - Verify a single email
- `verify_batch.py` - Verify multiple emails
- `domain_validation.py` - Validate domain
- `error_handling.py` - Handle errors properly
- `csv_processor.py` - Process CSV files

## Quick Start

```python
import requests

API_KEY = 'your_api_key'
BASE_URL = 'https://api.myemailverifier.com'

def verify_email(email):
    response = requests.post(
        f'{BASE_URL}/verify',
        json={
            'email': email,
            'api_key': API_KEY
        }
    )
    return response.json()

result = verify_email('user@example.com')
print(result)
```

## Configuration

Set environment variables:
```bash
export MYEMAILVERIFIER_API_KEY="your_api_key"
python verify_single.py
```

Or use `.env` file:
```env
MYEMAILVERIFIER_API_KEY=your_api_key
```

Load in your code:
```python
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('MYEMAILVERIFIER_API_KEY')
```

## Running Examples

```bash
# Single email verification
python verify_single.py

# Batch verification
python verify_batch.py

# Domain validation
python domain_validation.py

# Error handling
python error_handling.py

# CSV processing
python csv_processor.py emails.csv
```

## More Information

- [Back to examples](../)
- [API Reference](../../docs/API_REFERENCE.md)
- [Getting Started](../../docs/GETTING_STARTED.md)
