# Deep Catch-All API

Standard verification can't confirm addresses on **catch-all** domains — servers that accept mail for any address. The Deep Catch-All API scores each catch-all address individually to estimate whether a real, active mailbox is behind it.

- **Base URL:** `https://client.myemailverifier.com`
- **Auth:** API key in the URL path
- **Credit cost:** 5 credits per email scored

---

## Endpoints

| Method | URL | Description | Credits |
|--------|-----|-------------|---------|
| `GET`  | `/catchall/score/{email}/{apikey}` | Score a single email (synchronous) | 5 |
| `POST` | `/catchall/upload/{apikey}` | Upload CSV/TXT for batch scoring | 5 per email |
| `GET`  | `/catchall/status/{apikey}/{job_id}` | Poll batch job status | 0 |
| `GET`  | `/catchall/jobs/{apikey}` | List all batch jobs | 0 |
| `GET`  | `/catchall/download/{apikey}/{job_id}` | Download scored results CSV | 0 |

---

## 1. Single Score (synchronous)

```bash
curl "https://client.myemailverifier.com/catchall/score/john@acme.com/YOUR_API_KEY"
```

**Response `200`**
```json
{
  "status": true,
  "email": "john@acme.com",
  "score": 75,
  "verdict": "high_probability",
  "exists": true
}
```

| Field | Type | Description |
|-------|------|-------------|
| `score` | integer | Confidence score, 0–100 |
| `verdict` | string | `high_probability` · `low_probability` · `avoid_send` |
| `exists` | boolean | Best estimate of whether a real mailbox exists |

> A single score can take a few seconds while the address is analysed. Charged **5 credits** on success only — if scoring fails, no credits are deducted.

### Verdict reference

| Verdict | Score | Meaning |
|---------|-------|---------|
| `high_probability` | ≥ 50 | Strong signals — likely a real, active mailbox. Safe to include. |
| `low_probability` | < 50 | Weak or mixed signals — proceed with caution or exclude. |
| `avoid_send` | any | Strong negative signals detected — do not send. |

---

## 2. Batch Scoring (async)

For a list of catch-all addresses: upload → poll → download.

### Step 1 — Upload
```bash
curl -X POST "https://client.myemailverifier.com/catchall/upload/YOUR_API_KEY" \
  -F "file=@emails.csv"
```
Accepts a CSV or TXT file (one email per line, or the first column of a CSV).

**Response `201`**
```json
{
  "status": true,
  "job_id": 42,
  "total_emails": 500,
  "credits_deducted": 2500,
  "credits_remaining": 7500,
  "message": "Batch job queued. Poll /catchall/status/{apikey}/42 for progress."
}
```

### Step 2 — Poll status
```bash
curl "https://client.myemailverifier.com/catchall/status/YOUR_API_KEY/42"
```

**Response `200`**
```json
{
  "status": true,
  "data": {
    "id": 42,
    "file_name": "emails.csv",
    "status_label": "Processing",
    "status_message": "Scoring in progress",
    "progress_percent": 60,
    "total_emails": 500,
    "valid_count": 210,
    "invalid_count": 60,
    "unknown_count": 15,
    "credits_charged": 2500,
    "credits_used": 1425,
    "credits_refunded": 0,
    "has_result": false,
    "created_at": "2026-07-21 09:20:00",
    "updated_at": "2026-07-21 09:24:10"
  }
}
```
Poll every few seconds until `has_result` is `true` (job finished). Unknown/unscored addresses are refunded on completion (`credits_refunded`).

### Step 3 — Download results
```bash
curl -L "https://client.myemailverifier.com/catchall/download/YOUR_API_KEY/42" -o results.csv
```
Returns the scored CSV once the job has finished.

### List all batch jobs
```bash
curl "https://client.myemailverifier.com/catchall/jobs/YOUR_API_KEY"
```
Returns your most recent batch jobs (same object shape as the status `data` above).

---

## Error codes

| HTTP | `error` | Meaning |
|------|---------|---------|
| 401 | `INVALID_API_KEY` | Key wrong or inactive |
| 402 | `INSUFFICIENT_CREDITS` | Not enough credits (`credits_needed` + `credits_balance` included) |
| 403 | `ACCOUNT_BLOCKED` | The account is blocked |
| 403 | `PAYMENT_VERIFICATION_REQUIRED` | The account is on hold until a payment is verified |
| 403 | `DEMO_KEY_NOT_ALLOWED` | The public demo key can't be used for this API — use your own API key |
| 404 | `JOB_NOT_FOUND` | Unknown job id for this key |
| 409 | `JOB_NOT_COMPLETE` | Download requested before the job finished |
| 422 | `INVALID_EMAIL` / `NO_VALID_EMAILS` | Bad email / no valid emails in the file |
| 429 | — | Rate limit exceeded — slow down |
| 500 | `SERVICE_ERROR` | Scoring backend error (no credits charged) |

All error bodies: `{ "status": false, "error": "CODE", "message": "…", "http_code": NNN }`.

---

## Rate limits

| Endpoint | Limit |
|----------|-------|
| `GET /catchall/score` | 10 / min |
| `POST /catchall/upload` | 5 / min |
| `GET /catchall/status` | 120 / min |
| `GET /catchall/jobs` | 30 / min |
| `GET /catchall/download` | 30 / min |

---

*See also: [API Reference](API_REFERENCE.md) · [Lead Generation API](LEAD_GENERATION_API.md) · [Error Codes](ERROR_CODES.md)*
