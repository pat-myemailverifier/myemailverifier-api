# Lead Generation API

Find verified business contacts three ways — a plain-English prompt, a name + company, or just a LinkedIn profile URL — then reveal email addresses and phone numbers. **Every email is confirmed deliverable before it is returned.**

- **Base URL:** `https://client.myemailverifier.com`
- **Auth:** API key in the URL path
- **Content type:** `application/json` for POST bodies

---

## The three search tools

| Tool | Endpoint | Sync? | Cost |
|------|----------|-------|------|
| **Prompt Search** — describe the leads you want | `POST /leads/search` | Sync | 5 cr / search |
| **LinkedIn Finder** — name + company → email | `POST /leads/search` | Sync | 5 cr / search |
| **Find by URL** — LinkedIn profile URL → verified email | `POST /leads/linkedin-url` → poll `GET` | **Async** | Free to submit; 5 cr if no match |

Prompt Search and LinkedIn Finder are the **same endpoint** — the mode is chosen automatically by which fields you send.

---

## Credit costs

| Action | Credits |
|--------|---------|
| Prompt / LinkedIn Finder search | 5 per search |
| Find by URL — start a search | Free |
| Find by URL — no match found | 5 |
| Reveal contact (first time) | 10 per reveal |
| Re-reveal same token within 24 h | Free |
| Save / List / Delete leads | Free |

Reveal tokens expire **24 hours** after the search that produced them.

---

## Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| `POST` | `/leads/search/{apikey}` | Search by prompt or LinkedIn fields |
| `POST` | `/leads/linkedin-url/{apikey}` | Start a LinkedIn-URL email lookup (returns a job id) |
| `GET`  | `/leads/linkedin-url/{apikey}/{job_id}` | Poll a LinkedIn-URL lookup for its result |
| `POST` | `/leads/reveal/{apikey}` | Reveal full contact by token |
| `POST` | `/leads/save/{apikey}` | Save/bookmark a revealed lead |
| `GET`  | `/leads/saved/{apikey}` | List saved leads |
| `DELETE` | `/leads/saved/{apikey}/{lead_id}` | Delete a saved lead |

---

## 1. Prompt Search

Describe the leads you want in plain English.

```bash
curl -X POST "https://client.myemailverifier.com/leads/search/YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "CTO at fintech companies in Mumbai"}'
```

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `prompt` | string | ✅ | 5–500 characters |

**Response `200`**
```json
{
  "status": true,
  "total": 3,
  "cached": false,
  "sources": ["professional network", "database"],
  "credits_remaining": 4995,
  "data": [
    {
      "company": "PayFast India",
      "website": "payfast.in",
      "masked_email": "r*****@payfast.in",
      "email_token": "eyJ...",
      "masked_phone": "+91 *****3210",
      "phone_token": "eyJ...",
      "source_url": "https://www.linkedin.com/in/example",
      "snippet": "…context excerpt from the result…",
      "guessed": false
    }
  ],
  "error": null
}
```

`masked_email` / `masked_phone` are safe to display; use the tokens with **Reveal Contact** (§4) to get the full values.

---

## 2. LinkedIn Finder

Find a specific person by name + company. Same endpoint as Prompt Search — sending `company` plus a name switches modes automatically.

```bash
curl -X POST "https://client.myemailverifier.com/leads/search/YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Priya","last_name":"Mehta","company":"Infosys","designation":"Data Engineer","domain":"infosys.com"}'
```

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `company` | string | ✅ | Company name |
| `first_name` / `last_name` | string | ▲ | Send at least one |
| `designation` | string | — | Job title — improves accuracy |
| `location` | string | — | City/country — improves accuracy |
| `domain` | string | — | Company email domain — improves accuracy the most |

Response shape matches Prompt Search (§1).

---

## 3. Find Email from LinkedIn URL (async)

Give only a LinkedIn profile URL. Because resolution takes a few seconds, this is a two-step flow: **submit → poll**. Submitting is free; you pay 10 credits only when you reveal a contact that was found, or 5 credits if no address can be confirmed.

### Step 1 — Submit
```bash
curl -X POST "https://client.myemailverifier.com/leads/linkedin-url/YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"linkedin_url": "https://www.linkedin.com/in/username"}'
```

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `linkedin_url` | string | ✅ | Public profile URL. Company/school pages are rejected (`422 INVALID_URL`). |

**Response `202`**
```json
{
  "status": true,
  "job_id": 4821,
  "job_status": "processing",
  "poll_url": "https://client.myemailverifier.com/leads/linkedin-url/YOUR_API_KEY/4821",
  "message": "Lookup started. Poll poll_url every ~3s until job_status is \"done\" or \"failed\"."
}
```

### Step 2 — Poll (every ~3 seconds)
```bash
curl "https://client.myemailverifier.com/leads/linkedin-url/YOUR_API_KEY/4821"
```

**While running:**
```json
{ "status": true, "job_id": 4821, "job_status": "processing", "progress": 55 }
```
Use `progress` (0–100) to drive a progress bar.

**When finished — a verified contact was found:**
```json
{
  "status": true,
  "job_status": "done",
  "progress": 100,
  "outcome": "verified",
  "identity": {
    "name": "Marc Benioff",
    "headline": "Chair & CEO",
    "company": "Salesforce.com",
    "location": "San Francisco, California, United States",
    "profile_url": "https://www.linkedin.com/in/username"
  },
  "total": 1,
  "data": [
    {
      "company": "Salesforce.com",
      "verification_status": "valid",
      "masked_email": "m***********@salesforce.com",
      "email_token": "eyJ...",
      "email_format": "firstname.lastname",
      "alternates": [
        { "masked_email": "m*******@salesforce.com", "email_token": "eyJ...", "format": "first-initial + lastname" },
        { "masked_email": "m***@salesforce.com",     "email_token": "eyJ...", "format": "firstname only" }
      ]
    }
  ]
}
```

**When no address can be confirmed:**
```json
{
  "status": true,
  "job_status": "done",
  "outcome": "not_found",
  "identity": { "name": "Jane Doe", "company": "Acme Inc", "location": "London, UK" },
  "total": 0,
  "data": [],
  "message": "We found this person but could not confirm an email address for them."
}
```

**When it errored:**
```json
{ "status": true, "job_status": "failed", "progress": 100, "message": "Lookup failed. Please try again." }
```

### `outcome` values
| Value | Meaning |
|-------|---------|
| `verified` | A deliverable address was confirmed — see `data[0]`. |
| `catch_all` | The company accepts all mail, so the exact inbox can't be confirmed by a standard check. `verification_status` will be `catch_all`. |
| `not_found` | No address could be confirmed for this person. |

### Alternates
Several address formats can all be deliverable for one person. The most likely is the primary (`masked_email` / `email_token`); the rest are in `alternates[]`, each with a plain-language `format` label and its own `email_token`. Reveal any of them the same way as the primary (§4).

---

## 4. Reveal Contact

Turn an `email_token` (or `phone_token`) into the real value. **10 credits** the first time per contact; free to re-reveal the same token within 24 h. Works for a primary token or any alternate token.

```bash
# Email only
curl -X POST "https://client.myemailverifier.com/leads/reveal/YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email_token": "eyJ..."}'

# Email + phone together (single call, single charge)
curl -X POST "https://client.myemailverifier.com/leads/reveal/YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email_token": "eyJ...", "phone_token": "eyJ..."}'
```

**Response (first reveal — 10 credits deducted):**
```json
{ "status": true, "email": "marc.benioff@salesforce.com", "phone": "+91 9876543210", "already_revealed": false, "credits_remaining": 4985 }
```

**Response (re-reveal — free):**
```json
{ "status": true, "email": "marc.benioff@salesforce.com", "phone": "+91 9876543210", "already_revealed": true, "credits_remaining": 4985 }
```

- `already_revealed: true` → no credits were charged.
- `null` for a field means no token was sent for it.

---

## 5. Save / List / Delete (all free)

### Save
```bash
curl -X POST "https://client.myemailverifier.com/leads/save/YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email":"marc.benioff@salesforce.com","name":"Marc Benioff","company":"Salesforce","title":"CEO","linkedin_url":"https://www.linkedin.com/in/username"}'
```
`email` required; everything else optional. → `{ "status": true, "lead_id": 91, "message": "Lead saved successfully." }`

### List
```bash
curl "https://client.myemailverifier.com/leads/saved/YOUR_API_KEY"
```
```json
{
  "status": true,
  "total": 1,
  "data": [
    { "lead_id": 91, "name": "Marc Benioff", "email": "marc.benioff@salesforce.com",
      "phone": null, "company": "Salesforce", "title": "CEO",
      "linkedin_url": "https://www.linkedin.com/in/username", "notes": null,
      "saved_at": "2026-07-21T09:20:00+00:00" }
  ]
}
```

### Delete
```bash
curl -X DELETE "https://client.myemailverifier.com/leads/saved/YOUR_API_KEY/91"
```
→ `{ "status": true, "message": "Lead removed from saved list." }`

---

## Error codes

| HTTP | `error` | Meaning |
|------|---------|---------|
| 401 | `INVALID_API_KEY` | Key wrong or inactive |
| 402 | `INSUFFICIENT_CREDITS` | Not enough credits (`credits_needed` + `credits_balance` included) |
| 403 | `ACCOUNT_BLOCKED` | The account is blocked |
| 403 | `PAYMENT_VERIFICATION_REQUIRED` | The account is on hold until a payment is verified |
| 403 | `DEMO_KEY_NOT_ALLOWED` | The public demo key can't be used for this API (except the LinkedIn-URL demo on the website) — use your own API key |
| 404 | `JOB_NOT_FOUND` / `NOT_FOUND` | Unknown job id / lead id for this key |
| 422 | `INVALID_URL` | LinkedIn URL missing or not a profile URL |
| 422 | `INVALID_TOKEN` / `MISSING_TOKEN` | Reveal token bad/expired, or none provided |
| 429 | — | Rate limit exceeded — slow down |
| 500 | `SERVICE_ERROR` | Search backend error (no credits charged) |

All error bodies: `{ "status": false, "error": "CODE", "message": "…", "http_code": NNN }`.

---

## Rate limits

| Endpoint | Limit |
|----------|-------|
| `POST /leads/search` | 10 / min |
| `POST /leads/linkedin-url` (submit) | 10 / min |
| `GET /leads/linkedin-url/.../{job_id}` (poll) | 120 / min |
| `POST /leads/reveal` | 60 / min |
| `save` / `saved` / `delete` | 30 / min |

---

*See also: [API Reference](API_REFERENCE.md) · [Error Codes](ERROR_CODES.md) · [Authentication](AUTHENTICATION.md)*
