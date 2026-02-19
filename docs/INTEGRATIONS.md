# Third-Party Integrations

Integrate MyEmailVerifier with 2000+ apps via Zapier or use our REST API for custom integrations.

## Zapier Integration (Recommended)

MyEmailVerifier's official Zapier app connects with **2000+ platforms** including:
- Email marketing tools (Mailchimp, SendGrid, ActiveCampaign, etc.)
- CRM systems (Salesforce, HubSpot, Pipedrive, etc.)
- Form builders (Typeform, Gravity Forms, JotForm, etc.)
- E-commerce platforms (Shopify, WooCommerce, etc.)
- Spreadsheets (Google Sheets, Airtable, Excel, etc.)
- And many more!

### How to Connect

1. **Log in to Zapier** at [zapier.com](https://zapier.com)
2. **Search for "MyEmailVerifier"** in the app directory
3. **Connect your account** using your MyEmailVerifier API key
4. **Create Zaps** to automate email verification

### Popular Zap Examples

#### Verify Emails from Google Forms
```
Trigger: New Google Form Response
Action: MyEmailVerifier - Verify Email
Filter: Only proceed if Status = "Valid"
Action: Add to Google Sheets
```

#### Clean Mailchimp Lists
```
Trigger: New Mailchimp Subscriber
Action: MyEmailVerifier - Verify Email
Filter: If Status = "Invalid", unsubscribe
```

####  Validate Salesforce Leads
```
Trigger: New Salesforce Lead
Action: MyEmailVerifier - Verify Email
Action: Update Lead custom field with validation status
```

#### Filter HubSpot Contacts
```
Trigger: New HubSpot Contact
Action: MyEmailVerifier - Verify Email
Action: Tag contact based on email status
```

#### Verify Shopify Customers
```
Trigger: New Shopify Customer
Action: MyEmailVerifier - Verify Email
Action: Tag customer if email is invalid
```

---

## Direct REST API Integration

For custom integrations, use our REST API with any platform that supports HTTP requests.

### Email Service Providers

#### Mailchimp
```python
# Verify before adding subscriber
result = requests.get(
    'https://api.myemailverifier.com/api/validate_single.php',
    params={'apikey': API_KEY, 'email': email}
).json()

if result['Status'] == 'Valid':
    mailchimp.lists.add_member(list_id, {'email_address': email})
```

#### SendGrid
```javascript
const verifyAndSend = async (email) => {
    const verify = await axios.get('https://api.myemailverifier.com/api/validate_single.php', {
        params: { apikey: API_KEY, email: email }
    });
    
    if (verify.data.Status === 'Valid') {
        await sendgrid.send({ to: email, from: 'noreply@example.com', ... });
    }
};
```

#### ActiveCampaign
```php
$result = file_get_contents(
    "https://api.myemailverifier.com/api/validate_single.php?apikey=$apiKey&email=$email"
);
$data = json_decode($result, true);

if ($data['Status'] === 'Valid') {
    // Add to ActiveCampaign
}
```

### CRM Platforms

#### Salesforce
Apex HTTP Callout:
```apex
Http http = new Http();
HttpRequest req = new HttpRequest();
req.setEndpoint('https://api.myemailverifier.com/api/validate_single.php?apikey=' + apiKey + '&email=' + email);
req.setMethod('GET');
HttpResponse res = http.send(req);

Map<String, Object> result = (Map<String, Object>) JSON.deserializeUntyped(res.getBody());
String status = (String) result.get('Status');

// Update Lead/Contact field
lead.Email_Status__c = status;
update lead;
```

#### HubSpot
Workflow webhook:
```
Webhook URL: https://api.myemailverifier.com/api/validate_single.php
Method: GET
Parameters:
  - apikey: YOUR_API_KEY
  - email: {{contact.email}}
```

#### Pipedrive
```python
def verify_pipedrive_contact(person_id):
    # Get contact from Pipedrive
    person = pipedrive.get_person(person_id)
    email = person['email']
    
    # Verify email
    result = requests.get(
        'https://api.myemailverifier.com/api/validate_single.php',
        params={'apikey': API_KEY, 'email': email}
    ).json()
    
    # Update custom field
    pipedrive.update_person(person_id, {
        'email_status': result['Status']
    })
```

---

## E-commerce Platforms

### Shopify
Theme/app checkout validation:
```javascript
document.getElementById('checkout-email').addEventListener('blur', async function() {
    const email = this.value;
    
    const response = await fetch(
        `https://api.myemailverifier.com/api/validate_single.php?apikey=${API_KEY}&email=${email}`
    );
    const result = await response.json();
    
    if (result.Status !== 'Valid') {
        alert('Please enter a valid email address');
    }
});
```

### WooCommerce
WordPress validation hook:
```php
add_action('woocommerce_checkout_process', 'verify_checkout_email');

function verify_checkout_email() {
    $email = $_POST['billing_email'];
    $apiKey = get_option('myemailverifier_api_key');
    
    $response = file_get_contents(
        "https://api.myemailverifier.com/api/validate_single.php?apikey=$apiKey&email=$email"
    );
    $result = json_decode($response, true);
    
    if ($result['Status'] !== 'Valid') {
        wc_add_notice('Please enter a valid email address.', 'error');
    }
}
```

### Magento
```php
// Observer for customer registration
public function execute(\Magento\Framework\Event\Observer $observer)
{
    $customer = $observer->getEvent()->getCustomer();
    $email = $customer->getEmail();
    
    $result = $this->verifyEmail($email);
    
    if ($result['Status'] !== 'Valid') {
        throw new \Magento\Framework\Exception\LocalizedException(
            __('Please enter a valid email address.')
        );
    }
}
```

---

## Form Builders

### Gravity Forms (WordPress)
```php
add_filter('gform_field_validation', 'verify_email_field', 10, 4);

function verify_email_field($result, $value, $form, $field) {
    if ($field->type == 'email' && !$result['is_valid']) {
        return $result; // Already invalid
    }
    
    if ($field->type == 'email') {
        $apiKey = get_option('myemailverifier_api_key');
        $response = file_get_contents(
            "https://api.myemailverifier.com/api/validate_single.php?apikey=$apiKey&email=$value"
        );
        $data = json_decode($response, true);
        
        if ($data['Status'] !== 'Valid') {
            $result['is_valid'] = false;
            $result['message'] = 'Please enter a valid email address.';
        }
    }
    
    return $result;
}
```

### Typeform
Use webhooks to verify submissions on your server.

### JotForm
Add webhook integration in Form Settings → Integrations.

---

## Development Frameworks

### Laravel (PHP)
```php
// Service class
namespace App\Services;

use Illuminate\Support\Facades\Http;

class EmailVerifier
{
    public function verify($email)
    {
        $response = Http::get('https://api.myemailverifier.com/api/validate_single.php', [
            'apikey' => config('services.myemailverifier.api_key'),
            'email' => $email
        ]);
        
        return $response->json();
    }
}

// Usage in controller
$result = app(EmailVerifier::class)->verify($email);
if ($result['Status'] === 'Valid') {
    // Proceed
}
```

### Django (Python)
```python
# utils/email_verifier.py
import requests
from django.conf import settings

def verify_email(email):
    response = requests.get(
        'https://api.myemailverifier.com/api/validate_single.php',
        params={
            'apikey': settings.MYEMAILVERIFIER_API_KEY,
            'email': email
        }
    )
    return response.json()

# Usage in views
from utils.email_verifier import verify_email

result = verify_email(request.POST['email'])
if result['Status'] == 'Valid':
    # Proceed
```

### Express.js (Node.js)
```javascript
// services/emailVerifier.js
const axios = require('axios');

async function verifyEmail(email) {
    const response = await axios.get('https://api.myemailverifier.com/api/validate_single.php', {
        params: {
            apikey: process.env.MYEMAILVERIFIER_API_KEY,
            email: email
        }
    });
    return response.data;
}

module.exports = { verifyEmail };

// Usage in routes
const { verifyEmail } = require('./services/emailVerifier');

app.post('/signup', async (req, res) => {
    const result = await verifyEmail(req.body.email);
    if (result.Status === 'Valid') {
        // Proceed with signup
    }
});
```

### Ruby on Rails
```ruby
# app/services/email_verifier.rb
class EmailVerifier
  def self.verify(email)
    require 'net/http'
    require 'json'
    
    uri = URI('https://api.myemailverifier.com/api/validate_single.php')
    params = { 
      apikey: ENV['MYEMAILVERIFIER_API_KEY'], 
      email: email 
    }
    uri.query = URI.encode_www_form(params)
    
    response = Net::HTTP.get_response(uri)
    JSON.parse(response.body)
  end
end

# Usage in controller
result = EmailVerifier.verify(params[:email])
if result['Status'] == 'Valid'
  # Proceed
end
```

---

## Real-time Form Validation

### JavaScript (Client-side)
```javascript
document.getElementById('email').addEventListener('blur', async function() {
    const email = this.value;
    const statusDiv = document.getElementById('email-status');
    
    if (!email) return;
    
    statusDiv.textContent = 'Verifying...';
    
    try {
        const response = await fetch(
            `https://api.myemailverifier.com/api/validate_single.php?apikey=${API_KEY}&email=${email}`
        );
        const result = await response.json();
        
        if (result.Status === 'Valid') {
            statusDiv.textContent = '✓ Email verified';
            statusDiv.className = 'success';
        } else if (result.Status === 'Invalid') {
            statusDiv.textContent = '✗ Invalid email';
            statusDiv.className = 'error';
        } else {
            statusDiv.textContent = '⚠ ' + result.Diagnosis;
            statusDiv.className = 'warning';
        }
    } catch (error) {
        statusDiv.textContent = 'Verification failed';
        statusDiv.className = 'error';
    }
});
```

### jQuery
```javascript
$('#email').on('blur', function() {
    var email = $(this).val();
    
    $.get('https://api.myemailverifier.com/api/validate_single.php', {
        apikey: API_KEY,
        email: email
    }, function(result) {
        if (result.Status === 'Valid') {
            $('#email-status').html('✓ Email verified').addClass('success');
        } else {
            $('#email-status').html('✗ Invalid email').addClass('error');
        }
    });
});
```

---

## Best Practices

### 1. Cache Results
Avoid verifying the same email multiple times:
```python
from functools import lru_cache

@lru_cache(maxsize=10000)
def verify_email_cached(email):
    return verify_email(email)
```

### 2. Async Processing
For bulk verification, use background jobs:
```python
# Celery task
@celery.task
def verify_email_async(email):
    result = verify_email(email)
    update_user_status(email, result['Status'])
```

### 3. Error Handling
Always handle API errors gracefully:
```javascript
try {
    const result = await verifyEmail(email);
    // Process result
} catch (error) {
    if (error.response?.status === 429) {
        // Rate limited - retry after delay
        await sleep(60000);
        return verifyEmail(email);
    } else if (error.response?.status === 401) {
        // Invalid API key
        console.error('Invalid API key');
    }
    // Fallback behavior
    return { Status: 'Unknown' };
}
```

### 4. Rate Limiting
Respect API rate limits (default 30 req/min):
```python
import time
from threading import Lock

class RateLimiter:
    def __init__(self, max_calls=30, period=60):
        self.max_calls = max_calls
        self.period = period
        self.calls = []
        self.lock = Lock()
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with self.lock:
                now = time.time()
                self.calls = [c for c in self.calls if c > now - self.period]
                
                if len(self.calls) >= self.max_calls:
                    sleep_time = self.period - (now - self.calls[0])
                    time.sleep(sleep_time)
                
                self.calls.append(time.time())
                return func(*args, **kwargs)
        return wrapper

@RateLimiter(max_calls=30, period=60)
def verify_email(email):
    # API call
    pass
```

---

## Support & Resources

- **Zapier App**: Search "MyEmailVerifier" in Zapier app directory
- **API Reference**: [API Documentation](API_REFERENCE.md)
- **Code Examples**: See [examples](../examples/) folder
- **Support Email**: support@myemailverifier.com
- **Live Chat**: Available on our website

---

**Connect MyEmailVerifier with 2000+ apps via Zapier or build custom integrations with our REST API!**
