# Frequently Asked Questions (FAQ)

Find answers to common questions about MyEmailVerifier API.

## Getting Started

### Q: What is MyEmailVerifier?

A: MyEmailVerifier is a real-time email verification service that validates email addresses instantly. It checks domain validity, MX records, and performs SMTP-level verification to ensure emails are deliverable.

### Q: How do I get started?

A: 
1. Sign up at [MyEmailVerifier.com](https://myemailverifier.com)
2. Verify your phone number (required for free daily credits)
3. Get your API key from the dashboard under API Settings
4. Choose your integration method (API, SDK, or free tools)
5. Start verifying emails!

### Q: Do I need to code to use MyEmailVerifier?

A: No! We offer:
- **Free web tools** - No coding required
- **API** - For developers
- **Integrations** - With popular platforms (Zapier, Make, etc.)

### Q: Is there a free plan?

A: Yes! Free plan includes:
- **100 credits per day** (requires phone verification for fair usage)
- Access to all API endpoints
- Single email verifier
- Bulk upload capability
- Domain validation tool

**Note:** Phone verification is required to prevent abuse and ensure fair usage for all users.

---

## API & Integration

### Q: How do I authenticate with the API?

A: Use your API key in the request:

**Method 1: JSON Body**
```json
{
  "email": "user@example.com",
  "api_key": "your_api_key"
}
```

**Method 2: Authorization Header**
```
Authorization: Bearer your_api_key
```

See [Authentication Guide](AUTHENTICATION.md) for details.

### Q: What's the rate limit?

A: Depends on your plan:
- **Free**: 10 requests/minute
- **Starter**: 30 requests/minute
- **Professional**: 100 requests/minute
- **Enterprise**: Custom limits

### Q: Can I batch verify emails?

A: Yes! Use `/verify-batch` endpoint:
```bash
curl -X POST https://api.myemailverifier.com/verify-batch \
  -H "Content-Type: application/json" \
  -d '{
    "emails": ["email1@example.com", "email2@example.com"],
    "api_key": "your_api_key"
  }'
```

Maximum 100 emails per batch.

### Q: Do you support webhooks?

A: Yes! Webhooks are available on Professional and Enterprise plans.
- Get real-time notifications
- Automatic callbacks on completion
- Event-driven architecture support

See [Integrations Guide](INTEGRATIONS.md)

### Q: What languages are supported?

A: We provide SDKs and examples for:
- JavaScript/Node.js
- Python
- PHP
- Ruby (coming soon)
- Go (coming soon)

You can also use any language with our REST API.

---

## Verification & Accuracy

### Q: How accurate is the verification?

A: **99.9% accurate** for valid emails. Our verification includes:
- Email format validation
- Domain existence check
- MX record verification
- SMTP-level verification

### Q: How long does verification take?

A: Usually **1-3 seconds** per email:
- Format check: ~0.1s
- Domain validation: ~0.5s
- SMTP verification: ~1-2s

### Q: What's the difference between error code 2 and 3?

A: 
- **Code 2 (Catch-all)**: Domain accepts ALL emails - can't verify specific email
- **Code 3 (Role-based)**: Specific email exists (support@, info@, etc) - can verify but shared inbox

### Q: Can you detect temporary email addresses?

A: We detect some temporary email services, but not all. For best results:
- Use in combination with user confirmation
- Employ additional validation layers
- Check [Error Codes](ERROR_CODES.md) for details

### Q: What about disposable/temporary emails?

A: These are detected:
- Temporary email services
- Throwaway email sites
- Some role-based addresses

Some may slip through - recommend secondary confirmation for critical use.

---

## Pricing & Plans

### Q: What's included in the free plan?

A: 
- **100 credits per day** (requires phone verification)
- Access to all API endpoints
- Single email verifier
- Bulk upload capability
- Domain validator
- Catch-all detector
- Full API access

**Note:** Phone verification is required for fair usage and abuse prevention.

### Q: How do subscription credits work?

A: **Credits are accumulative** - they add up each month and never expire:
- Monthly subscription adds credits to your balance
- Unused credits carry over to next month
- No reset or "use it or lose it" policy
- Example: 1,000 credits/month plan:
  - Month 1: Use 500, balance = 500
  - Month 2: Add 1,000, balance = 1,500
  - Month 3: Use 2,000, balance = 500

### Q: Do my credits expire?

A: **No!** Credits never expire:
- Subscription credits accumulate monthly
- Pay-as-you-go credits never expire
- Free daily credits renew every 24 hours

### Q: How much does verification cost?

A: Pricing options:
- **Free**: 100 credits/day (phone verification required)
- **Monthly Plans**: Credits accumulate, never expire
- **Pay-as-you-go**: Purchase credits anytime, no expiration
- **Enterprise**: Custom solutions with volume discounts

See our [pricing page](https://myemailverifier.com/pricing) for current rates.

### Q: Can I try before buying?

A: Yes! Using the free plan:
1. Sign up for free
2. Verify your phone number
3. Get 100 credits daily
4. Test the service thoroughly
5. Upgrade when ready

### Q: How do I upgrade my plan?

A: 
1. Log in to your dashboard
2. Go to Billing → Plans
3. Choose your plan
4. Update payment method
5. Credits are added immediately!

### Q: What happens if I cancel my subscription?

A: 
- Your existing credits remain in your account
- You can still use all accumulated credits
- You'll continue to receive 100 free credits daily (with phone verification)
- No credits are lost when you cancel

---

## Data & Privacy

### Q: How long do you keep my data?

A: 
- Email addresses: Not stored permanently
- Verification results: 30 days (configurable)
- Account data: Until deletion
- Logs: 90 days (for compliance)

See our [Privacy Policy](https://myemailverifier.com/privacy)

### Q: Is my data secure?

A: Yes! We use:
- **SSL/TLS encryption** - All data in transit
- **AES-256 encryption** - Sensitive data at rest
- **Regular audits** - Security assessments
- **GDPR compliant** - EU regulation support
- **SOC 2 certified** - Security standards

### Q: Can I delete my data?

A: Yes! You can:
- Delete individual verification results
- Delete batch results
- Permanently delete your account
- Request data export (GDPR)

Contact support for GDPR requests.

### Q: How is my API key protected?

A: Best practices:
- Use environment variables (not hardcoded)
- Rotate keys every 90 days
- Revoke unused keys immediately
- Use separate keys per environment
- Never commit keys to repositories

---

## Troubleshooting

### Q: I get "Invalid API key" error

A: Check:
1. API key copied correctly (no extra spaces)
2. Using correct base URL
3. Key is active in dashboard
4. Using correct authentication method

### Q: Rate limit exceeded - what do I do?

A: 
1. Implement exponential backoff retry
2. Batch requests efficiently
3. Upgrade your plan
4. Contact support for enterprise limits

### Q: Verification times out

A: 
1. Increase timeout value (10-20 seconds)
2. Retry the request
3. Check network connectivity
4. Contact support if persistent

### Q: Some emails return "unknown" status

A: This means:
- Unable to verify definitive
- Server didn't respond clearly
- Domain is protected/blocked
- Retry after a few minutes

### Q: Can I verify emails from my database?

A: Yes! Multiple options:
1. Use bulk verifier tool (UI)
2. Use `/verify-batch` API endpoint
3. Build custom script with API
4. Use integration (Zapier, Make)

---

## Integration & Tools

### Q: Do you have a WordPress plugin?

A: Not yet, but you can:
- Use Zapier integration
- Use custom PHP code with our API
- Contact support for custom solution

### Q: Can I use MyEmailVerifier in my SaaS?

A: Yes! White-label options available:
- Custom branding
- Dedicated infrastructure
- Enterprise support
- Volume discounts

Contact sales@myemailverifier.com

### Q: Do you support webhooks?

A: Yes! On Professional+ plans:
- Real-time callbacks
- Event-driven architecture
- Batch completion notifications
- Custom webhook endpoints

### Q: Can I integrate with my CRM?

A: Yes! We support:
- Salesforce
- HubSpot
- Pipedrive
- Zapier (works with any platform)
- Custom API integration

See [Integrations Guide](INTEGRATIONS.md)

---

## Support & Account

### Q: How do I contact support?

A: Multiple options:
- 📧 Email: support@myemailverifier.com
- 💬 Live chat: On our website (9am-5pm EST)
- 📖 Documentation: Full guides available
- 🐛 GitHub: Report technical issues

### Q: What's your support SLA?

A: Response times:
- **Free plan**: 24-48 hours
- **Paid plans**: 12-24 hours
- **Enterprise**: 4 hours or SLA

### Q: Can I cancel my subscription?

A: Yes, anytime:
1. Go to Billing → Subscription
2. Click "Cancel Subscription"
3. Immediate cancellation
4. No refunds for used services
5. Data deleted after 30 days

### Q: Do you offer refunds?

A: 
- 14-day money-back guarantee
- No questions asked refund
- Contact support to process
- Prorated refunds for annual billing

---

## Business Questions

### Q: Can I resell MyEmailVerifier?

A: Yes! We offer:
- Affiliate program (20% commission)
- Reseller partnerships
- White-label solutions
- Enterprise licensing

Contact partnerships@myemailverifier.com

### Q: Do you have educational discounts?

A: Yes! Students get:
- 50% off Starter plan
- Proof required (.edu email)
- Annual billing only
- Contact education@myemailverifier.com

### Q: Is there an API SLA?

A: Enterprise customers get:
- 99.9% uptime SLA
- Incident support
- Dedicated account manager
- Custom infrastructure

---

## Still Have Questions?

We're always happy to help!

- 📧 **Email:** support@myemailverifier.com
- 💬 **Live Chat:** Available on our website
- 📚 **Docs:** See [all documentation](../)
- 🐛 **Report Issues:** [GitHub](https://github.com/myemailverifier)

---

**Last Updated:** February 2024
