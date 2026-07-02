# Home Site Docs Update Brief — Get File Info API (Endpoint 5)

**For:** Home site frontend developer / AI agent  
**File to update:** `docs/API_REFERENCE.md`  
**Date:** June 2026  

---

## What Changed

The **Get File Info** endpoint (`GET /verifier/file_info/{apikey}/{fileid}`) has been significantly expanded.  
The old response returned ~14 raw database fields with no computed values.  
The new response includes:

- **Computed `progress_percent`** (0–100 integer, never exceeds 100, hard-capped)
- **3-phase progress fields** (`phase`, `percent_phase1`, `percent_phase2`, domain counters)
- **Human-readable `status_label`** (`queued` | `processing` | `completed`)
- **Structured `result_counts` object** ready for pie/bar charts
- **Per-category download URLs** (valid, invalid, catch-all, unknown, XLS)
- All raw counts cast to **integers** (no more string numbers)

---

## Exact Section to Replace in `docs/API_REFERENCE.md`

Find the existing **Section 5 — Get File Information and Results** block and replace it entirely with the content below.

---

### 5. Get File Information, Live Progress & Results

**Endpoint:** `GET /verifier/file_info/{apikey}/{fileid}`

**Base URL:** `https://client.myemailverifier.com`

**Description:**  
Returns real-time verification status, live progress percentages, result counts and download links for a bulk-uploaded file.  
**Poll this endpoint every 30–60 seconds** while a file is processing. Server data updates approximately every 30 seconds to 1 minute. Stop polling when `status_label === "completed"`.

**URL Parameters:**

| Parameter | Type     | Required | Description                         |
|-----------|----------|----------|-------------------------------------|
| `apikey`  | string   | Yes      | Your API key                        |
| `fileid`  | integer  | Yes      | File ID returned by the upload endpoint |

**Example Request:**

```bash
curl "https://client.myemailverifier.com/verifier/file_info/YOUR_API_KEY/1669"
```

---

#### Response Structure

```json
{
  "status": true,
  "file": {
    "upload_id": 1669,
    "user_id": 54838,
    "filename": "my-list.csv",
    "created_at": "2026-06-19T10:22:00.000000Z",

    "ready_for_download": 1,
    "status": "finished",
    "status_label": "completed",
    "downloadable": true,

    "progress_percent": 100,
    "total_emails": 5000,
    "processed_res": 5000,

    "phase": "Validating emails",
    "percent_phase1": 100,
    "percent_phase2": 100,
    "unique_domains": 412,
    "domains_checked_p1": 412,
    "domains_checked_p2": 412,

    "total": 5000,
    "valid": 3800,
    "invalid": 750,
    "catchall": 320,
    "unknown": 80,
    "duplicates": 50,
    "spam_trap": 12,
    "toxic_domains": 38,
    "credit_used": 4950,

    "result_counts": {
      "Valid": 3800,
      "Invalid": 750,
      "CatchAll": 320,
      "Unknown": 80,
      "Spamtrap": 12,
      "Disposable": 38,
      "Duplicate": 50
    },

    "download_all_csv":      "https://client.myemailverifier.com/downloadreport/csv/...",
    "download_valid_csv":    "https://client.myemailverifier.com/downloadreport/validcsv/...",
    "download_invalid_csv":  "https://client.myemailverifier.com/downloadreport/invalidcsv/...",
    "download_catchall_csv": "https://client.myemailverifier.com/downloadreport/catchallcsv/...",
    "download_unknown_csv":  "https://client.myemailverifier.com/downloadreport/unknowncsv/...",
    "download_xls":          "https://client.myemailverifier.com/downloadreport/xls/...",

    "file_path":             "https://client.myemailverifier.com/downloadreport/csv/...",
    "xls_file_path":         "https://client.myemailverifier.com/downloadreport/xls/..."
  }
}
```

---

#### Complete Field Reference

**Identity**

| Field        | Type   | Description                            |
|--------------|--------|----------------------------------------|
| `upload_id`  | integer | Unique file ID                        |
| `user_id`    | integer | User account ID (backward-compat field from original API) |
| `filename`   | string  | User-supplied file name               |
| `created_at` | string  | ISO 8601 upload timestamp             |

**Status**

| Field               | Type    | Description |
|---------------------|---------|-------------|
| `ready_for_download`| integer | Raw status: `0` = queued, `1` = completed, `3` = processing |
| `status`            | string  | Raw status string from server (e.g. `"finished"`, `"In Queue"`) |
| `status_label`      | string  | Normalised: `"queued"` \| `"processing"` \| `"completed"` — use this for logic |
| `downloadable`      | boolean | `true` only when `ready_for_download === 1`. Check this before using download URLs. |

**Overall Progress**

| Field             | Type    | Description |
|-------------------|---------|-------------|
| `progress_percent`| integer | **Main progress bar value.** 0–100. Computed as `(valid + invalid + unknown + catchall) / total_emails × 100`. Hard-capped at 100. Forced to 100 when complete. |
| `total_emails`    | integer | Total email lines minus blank lines — the correct denominator |
| `processed_res`   | integer | Emails verified so far (numerator of `progress_percent`) |

> **Note:** `spam_trap` and `toxic_domains` are sub-breakdowns of `invalid`. They are NOT added separately into `processed_res` to avoid exceeding `total_emails`.

**3-Phase Progress (for phase-by-phase UI)**

The verification engine runs in three sequential phases. Display these as sub-progress bars or status labels alongside the main `progress_percent`.

| Field              | Type    | Description |
|--------------------|---------|-------------|
| `phase`            | string  | Current phase label. Values: `"Blacklisted domain check"` → `"Checking catchall domains"` → `"Validating emails"` |
| `percent_phase1`   | integer | Phase 1 (domain blacklist / MX record check). 0–100. |
| `percent_phase2`   | integer | Phase 2 (catch-all domain detection). 0–100. |
| `unique_domains`   | integer | Total unique domains in the file (denominator for phase %) |
| `domains_checked_p1` | integer | Domains processed in Phase 1 (numerator for `percent_phase1`) |
| `domains_checked_p2` | integer | Domains processed in Phase 2 (numerator for `percent_phase2`) |

**Result Counts (raw integers)**

| Field          | Type    | Description |
|----------------|---------|-------------|
| `total`        | integer | Total email addresses in file (including blank lines) |
| `valid`        | integer | Confirmed deliverable mailboxes |
| `invalid`      | integer | Undeliverable (includes spam_trap + toxic_domains sub-types) |
| `catchall`     | integer | Catch-all domain — server accepts all email |
| `unknown`      | integer | Could not be determined (timeout / greylisted) |
| `duplicates`   | integer | Duplicate email lines found |
| `spam_trap`    | integer | Spam trap addresses detected (sub-type of invalid) |
| `toxic_domains`| integer | Disposable / toxic domain addresses (sub-type of invalid) |
| `credit_used`  | integer | Credits consumed for this file |

**`result_counts` Object (for charts)**

Ready-to-use for pie or bar chart rendering. Keys match the web dashboard chart labels.

```json
"result_counts": {
  "Valid":      3800,
  "Invalid":    750,
  "CatchAll":   320,
  "Unknown":    80,
  "Spamtrap":   12,
  "Disposable": 38,
  "Duplicate":  50
}
```

**Per-Category Download URLs**

All URLs are pre-built — no construction needed. Each is `null` if that category has zero results.

| Field                 | Type          | Description |
|-----------------------|---------------|-------------|
| `download_all_csv`    | string        | All results combined (always present) |
| `download_valid_csv`  | string \| null | Valid emails only |
| `download_invalid_csv`| string \| null | Invalid emails only |
| `download_catchall_csv`| string \| null | Catch-all emails only |
| `download_unknown_csv`| string \| null | Unknown emails only |
| `download_xls`        | string \| null | Full Excel report |
| `file_path`           | string         | Alias for `download_all_csv`. Backward-compatible — use either name. |
| `xls_file_path`       | string \| null | Alias for `download_xls`. Backward-compatible — use either name. |

> ⚠️ Only use download URLs when `downloadable === true`. URLs exist in the response regardless but files are not ready until then.

---

#### 3-Phase Verification Explained

```
Phase 1 — Domain Blacklist & MX Check
  ↓  (percent_phase1: 0→100)
Phase 2 — Catch-All Domain Detection
  ↓  (percent_phase2: 0→100)
Phase 3 — Individual SMTP Email Validation
       (progress_percent: 0→100, phase = "Validating emails")
```

During Phase 1 and 2, `progress_percent` may stay low because individual email SMTP checks haven't started yet. Show `percent_phase1` / `percent_phase2` as sub-progress bars during those phases for a better user experience.

---

#### Polling Example — JavaScript Progress Bar

```javascript
/**
 * Poll the file info endpoint every 10 seconds.
 * Updates a progress bar and renders a result chart on completion.
 */
async function trackBulkVerification(apiKey, fileId) {
  const url = `https://client.myemailverifier.com/verifier/file_info/${apiKey}/${fileId}`;

  while (true) {
    const res = await fetch(url);
    const data = await res.json();

    if (!data.status) {
      console.error('API error:', data.message);
      break;
    }

    const f = data.file;

    // ── Main progress bar (0–100) ────────────────────────────
    document.getElementById('progress-bar').style.width = f.progress_percent + '%';
    document.getElementById('progress-label').textContent = f.progress_percent + '%';

    // ── Phase sub-progress ───────────────────────────────────
    if (f.phase) {
      document.getElementById('phase-label').textContent = f.phase;
    }
    if (f.percent_phase1 < 100) {
      showPhaseBar('phase1-bar', f.percent_phase1);
    } else if (f.percent_phase2 < 100) {
      showPhaseBar('phase2-bar', f.percent_phase2);
    }

    // ── Live counts ──────────────────────────────────────────
    document.getElementById('count-valid').textContent   = f.valid;
    document.getElementById('count-invalid').textContent = f.invalid;
    document.getElementById('count-catchall').textContent= f.catchall;
    document.getElementById('count-unknown').textContent = f.unknown;

    // ── Done? ────────────────────────────────────────────────
    if (f.status_label === 'completed') {
      // Render pie/bar chart with result_counts
      renderResultChart(f.result_counts);

      // Show per-category download buttons
      if (f.download_valid_csv)     showDownloadBtn('valid',   f.download_valid_csv);
      if (f.download_invalid_csv)   showDownloadBtn('invalid', f.download_invalid_csv);
      if (f.download_catchall_csv)  showDownloadBtn('catchall',f.download_catchall_csv);
      if (f.download_unknown_csv)   showDownloadBtn('unknown', f.download_unknown_csv);
      if (f.download_xls)           showDownloadBtn('xls',     f.download_xls);
      showDownloadBtn('all', f.download_all_csv);

      break; // Stop polling
    }

    // Wait 30 seconds before next poll (server updates every 30s–1min)
    await new Promise(resolve => setTimeout(resolve, 30000));
  }
}

// Kick off after upload returns file_id
const uploadResult = await uploadFile(apiKey, file);
if (uploadResult.status) {
  trackBulkVerification(apiKey, uploadResult.file_id);
}
```

**Recommended polling interval:** 30–60 seconds. Server data updates approximately every 30 seconds to 1 minute. Files with more unique domains spend longer in Phases 1 and 2 before Phase 3 begins.

---

#### Chart.js / ApexCharts Integration

When `status_label === "completed"`, the `result_counts` object is ready to pass directly to any chart library — no transformation needed.

**`result_counts` keys (in display order):** `Valid`, `Invalid`, `CatchAll`, `Unknown`, `Spamtrap`, `Disposable`, `Duplicate`

```javascript
// ── Chart.js — pie chart ──────────────────────────────────────────────
new Chart(document.getElementById('resultsChart'), {
  type: 'pie',
  data: {
    labels: Object.keys(f.result_counts),   // ['Valid','Invalid','CatchAll',...]
    datasets: [{
      data: Object.values(f.result_counts), // [3800, 750, 320, ...]
      backgroundColor: [
        '#22c55e', // Valid     — green
        '#ef4444', // Invalid   — red
        '#f59e0b', // CatchAll  — amber
        '#6b7280', // Unknown   — gray
        '#8b5cf6', // Spamtrap  — purple
        '#f97316', // Disposable— orange
        '#64748b'  // Duplicate — slate
      ]
    }]
  }
});

// ── ApexCharts — donut chart ─────────────────────────────────────────
new ApexCharts(document.getElementById('resultsChart'), {
  series: Object.values(f.result_counts),
  labels: Object.keys(f.result_counts),
  chart: { type: 'donut' },
  colors: ['#22c55e','#ef4444','#f59e0b','#6b7280','#8b5cf6','#f97316','#64748b']
}).render();
```

**Suggested color mapping for consistent branding:**

| Category | Color | Hex |
|----------|-------|-----|
| Valid | 🟢 Green | `#22c55e` |
| Invalid | 🔴 Red | `#ef4444` |
| CatchAll | 🟡 Amber | `#f59e0b` |
| Unknown | ⚫ Gray | `#6b7280` |
| Spamtrap | 🟣 Purple | `#8b5cf6` |
| Disposable | 🟠 Orange | `#f97316` |
| Duplicate | 🔵 Slate | `#64748b` |

---

#### `status_label` State Machine

```
upload response received
        ↓
  status_label = "queued"        (ready_for_download = 0)
        ↓ processing begins
  status_label = "processing"    (ready_for_download = 3)
        ↓ all emails done
  status_label = "completed"     (ready_for_download = 1)
                                  → downloadable = true
                                  → progress_percent = 100
```

---

#### Error Responses

```json
{ "status": false, "message": "Invalid API Key" }        // 401
{ "status": false, "message": "Unauthorized Request" }   // 403
{ "status": false, "message": "File not found" }         // 404
```

---

## What to Do With the Old Example Response

The old example response block for Section 5 returned flat raw fields like:
```json
{ "upload_id": "1670", "ready_for_download": "1", "valid": "850", ... }
```

**Replace it entirely** with the new response block above. Key differences:

| Old | New |
|-----|-----|
| All values returned as strings | All counts returned as integers |
| No `progress_percent` | `progress_percent` integer 0–100 |
| No `status_label` | `status_label` string (`queued`/`processing`/`completed`) |
| No phase fields | `phase`, `percent_phase1`, `percent_phase2` + domain counters |
| No `result_counts` object | `result_counts` object keyed for charting |
| Only `file_path` + `xls_file_path` | Six per-category download URL fields **plus** `file_path`, `xls_file_path` and `user_id` **retained** as backward-compat aliases |
| No `total_emails` / `processed_res` | Both present as integers |

---

## Files to Update on the Home Site

| File | Action |
|------|--------|
| `docs/API_REFERENCE.md` | Replace Section 5 entirely with content above |
| Any existing polling / integration example pages | Update response shape to match new field names |
| SDK / wrapper libraries (if any) | Add `progress_percent`, `status_label`, `result_counts`, `download_*` fields |

---

## Do NOT Change

- Section 1 (Single email validation — Fast API)  
- Section 2 (Single email validation — Client API)  
- Section 3 (Get Credit Balance)  
- Section 4 (Upload File for Bulk Verification)  
- Error response format or HTTP status code table  
- Authentication docs  

These are unchanged and existing API consumers depend on them.
