# Third-Party Integrations

Integrate MyEmailVerifier with popular platforms and tools.

## Email Marketing Platforms

### Mailchimp Integration

Verify email lists before uploading to Mailchimp:

1. Export your email list from MyEmailVerifier
2. Import into Mailchimp
3. Use our [free bulk verification tool](FREE_TOOLS.md)

**Webhook Integration:**
```
Add webhook: https://api.myemailverifier.com/hooks/mailchimp
```

### Zapier Integration

Automate email verification with Zapier:

1. Create a Zapier Zap
2. Trigger: When new subscriber added
3. Action: MyEmailVerifier - Verify Email
4. Map email field
5. Use results to tag/segment subscribers

**Configuration:**
```
Trigger: Mailchimp - New Subscriber
Action: MyEmailVerifier - Verify Email
Filter: If valid, continue; if invalid, stop
```

### Make (Integromat)

Automate workflows:

1. Create new scenario in Make
2. Add MyEmailVerifier module
3. Choose "Verify Email" operation
4. Map email input
5. Add conditional logic for results

---

## CRM Platforms

### Salesforce

Use custom flow or formula field with webhook calls:

```
Flow: Email Verification on Lead Creation
1. Create lead
2. HTTP Request to MyEmailVerifier API
3. Update Lead.Email_Status field with result
```

### HubSpot

HubSpot Workflow Setup:

1. Go to Automation → Workflows
2. Create enrollment trigger
3. Add custom action calling MyEmailVerifier API
4. Update contact property with verification result

### Pipedrive

Verify emails in contact creation pipeline:

1. Use Pipedrive API integration
2. Call MyEmailVerifier when new contact added
3. Store verification status in custom field
4. Segment contacts based on validation

---

## Bulk Verification Services

### Google Sheets Add-on

Coming soon! Check back for official Google Sheets integration.

**Manual Integration:**
```
Use IMPORTJSON() function to call API
=IMPORTJSON("https://api.myemailverifier.com/verify?email=" & A1)
```

### Airtable Integration

Using Airtable Automations:

1. Create base with email field
2. Set up automation trigger
3. Use webhook to MyEmailVerifier API
4. Write results back to Airtable

---

## Webhook Integrations

### Setting Up Webhooks

1. Go to Dashboard → Webhooks
2. Click "Add Webhook"
3. Enter endpoint URL
4. Select events to receive
5. Test the webhook

### Supported Events

- `email.verified` - Email verification completed
- `batch.completed` - Batch verification completed
- `batch.failed` - Batch verification failed
- `limit.reached` - Monthly limit reached

### Webhook Payload

```json
{
  "event_type": "email.verified",
  "timestamp": "2024-02-19T10:30:00Z",
  "data": {
    "email": "user@example.com",
    "is_valid": true,
    "deliverability": "safe",
    "error_code": 0
  }
}
```

---

## E-Commerce Platforms

### Shopify Integration

Verify customer emails on signup:

```javascript
// In Shopify theme / custom app
fetch('https://api.myemailverifier.com/verify', {
  method: 'POST',
  body: JSON.stringify({
    email: customerEmail,
    api_key: MYEMAILVERIFIER_API_KEY
  })
})
.then(response => response.json())
.then(data => {
  if (data.is_valid) {
    // Complete checkout
  } else {
    // Show error and ask for confirmation
  }
})
```

### WooCommerce Integration

```php
<?php
// In WooCommerce checkout validation hook
add_action('woocommerce_checkout_process', function() {
    $email = $_POST['post_data']['billing_email'];
    
    $response = wp_remote_post('https://api.myemailverifier.com/verify', [
        'body' => json_encode([
            'email' => $email,
            'api_key' => MYEMAILVERIFIER_API_KEY
        ]),
        'headers' => ['Content-Type' => 'application/json']
    ]);
    
    $data = json_decode(wp_remote_retrieve_body($response), true);
    
    if (!$data['is_valid']) {
        wc_add_notice('Invalid email address', 'error');
    }
});
?>
```

---

## Form Builders

### Typeform Integration

Add real-time validation to Typeform:

1. Create Typeform with email field
2. Use Zapier as middleware
3. Connect to MyEmailVerifier
4. Route based on validation result

### JotForm Integration

Using webhooks in JotForm:

1. In JotForm editor, add email field
2. Go to Settings → Integration
3. Add custom webhook to MyEmailVerifier
4. When form submitted, verify email in real-time

---

## Communication Platforms

### Twilio Integration

Verify email before sending SMS:

```python
from twilio.rest import Client
import requests

def verify_and_sends_sms(phone, email):
    # Verify email
    verify_response = requests.post(
        'https://api.myemailverifier.com/verify',
        json={'email': email, 'api_key': API_KEY}
    )
    
    if verify_response.json()['is_valid']:
        # Send SMS
        client = Client(account_sid, auth_token)
        client.messages.create(
            body="Email verified successfully!",
            from_=TWILIO_PHONE,
            to=phone
        )
```

---

## Analytics & Monitoring

### Mixpanel Integration

Track verification events:

```javascript
import Mixpanel from 'mixpanel-browser';

Mixpanel.init('PROJECT_TOKEN');

const verifyEmail = async (email) => {
    const response = await fetch('https://api.myemailverifier.com/verify', {
        method: 'POST',
        body: JSON.stringify({
            email: email,
            api_key: API_KEY
        })
    });
    
    const data = await response.json();
    
    Mixpanel.track('Email Verified', {
        email: email,
        is_valid: data.is_valid,
        deliverability: data.deliverability
    });
};
```

### Segment Integration

```javascript
analytics.track('Email Verified', {
  email: email,
  is_valid: is_valid,
  deliverability: deliverability,
  verification_time: verification_time
});
```

---

## Custom Integrations

### Using Our API

For custom integrations, use our REST API:

- **Base URL:** https://api.myemailverifier.com
- **Documentation:** [API Reference](API_REFERENCE.md)
- **Code Examples:** [Examples Directory](../examples/)

### Webhook Testing

Use RequestBin for testing webhooks:
1. Create bin at https://requestbin.com
2. Add webhook URL in MyEmailVerifier dashboard
3. Verify payload format

---

## Support for Integrations

- 📧 Email: integrations@myemailverifier.com
- 💬 Discord: [Community Server](#)
- 📖 API Docs: [API Reference](API_REFERENCE.md)
- 🐛 GitHub: [Report Integration Issues](#)

---

More integrations coming soon! If you need a specific integration, please let us know.
