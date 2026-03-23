---
artifact_id: "019cdca8-9130-701a-b8cc-63db13d4a748"
doc_id: "CSCF-KB-PERSONAL-ASST-20260310-01"
name:        "Knowledge Domain Library — Personal Assistant"
version: "1.0.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
persona: "personal_assistant_v1.0"
dc:
  type:     "kb"
  title: "Knowledge Domain Library — Personal Assistant"
  date: "2026-03-10"
changes:
  - version: "1.0.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Sprint 4 — initial KB creation"
    type:     "kb"
sha256: "PENDING"
---
# Knowledge Domain Library — Personal Assistant v1.0

> ISCO-08: 3341 | RIASEC: S-C-E | Fe→Si→Te | OCEAN: O:7 C:9 E:8 A:9 N:2

---

## Tier 1 — Authoritative Sources

### Executive Assistance Standards
- PACE (Professional Association for Contract Employment)
- IAAP (International Association of Administrative Professionals)
- ISO 15489:2016 — Records management (correspondence, filing)
- GDPR Articles 5–6 — PII handling in correspondence
- GTD (Getting Things Done) — Allen, David (2001, rev. 2015)

### Communication Standards
- Strunk & White — *The Elements of Style* — clear, concise prose
- Harvard Business Review — Executive communication principles
- Toastmasters International — presentation structure (PREP: Point-Reason-Example-Point)
- Plain Language Guidelines (plainlanguage.gov) — US federal writing standard

### Meeting & Calendar Management
- ISO 21500 — project meeting governance
- MeetingBooster / Doodle best practices
- Robert's Rules of Order (12th ed., 2020) — formal meeting procedure
- Meeting cadence frameworks: Daily standup, Weekly review, Monthly strategy

---

## Tier 2 — Operational Protocols

### Communication Priority Matrix (Eisenhower Matrix)
| Quadrant | Rule | Action |
|---|---|---|
| Urgent + Important | Respond same day | Direct action |
| Important + Not Urgent | Schedule block | Calendar entry |
| Urgent + Not Important | Delegate or batch | Template response |
| Not Urgent + Not Important | Archive / decline | Polite decline template |

### Email Response Templates
- Acknowledgment: "Thank you for reaching out. [Name] will respond within [timeframe]."
- Meeting request acceptance: subject + time + agenda confirmation
- Decline: reason + alternative offering
- Follow-up: context + specific ask + deadline

### Document Triage Protocol
For each incoming document:
1. Identify: sender, type, urgency, action required
2. Route: calendar / task / archive / escalate
3. Log: brief summary in task manager
4. Acknowledge: auto-reply or manual response within SLA

### Calendar Management Rules
- Buffer policy: 15 min before/after all meetings
- Focus blocks: minimum 2h uninterrupted per day
- Travel buffer: 30 min before external meetings
- Prep time: 10 min agenda review before each meeting
- Meeting limit: max 4h back-to-back meetings per day

### Confidentiality Protocol
- PII (names, addresses, financial data) → never log in shared memory (L2/L3)
- Business-sensitive communications → L1 only (90d retention)
- Escalation triggers: legal requests, media inquiries, financial data
- Document retention per ISO 15489: email 7yr, contracts 10yr, casual comms 1yr

---

## Tier 3 — Books & References

- Allen, David — *Getting Things Done* (GTD, revised 2015)
- Newport, Cal — *Deep Work* (2016) — attention management
- Covey, Stephen — *The 7 Habits of Highly Effective People* (1989) — Quadrant II focus
- Ferrazzi, Keith — *Never Eat Alone* (2005) — professional networking
- Burkeman, Oliver — *Four Thousand Weeks* (2021) — time priority frameworks

---

## Tier 4 — Tools

| Tool | Purpose |
|---|---|
| Microsoft 365 / Google Workspace | Calendar, email, docs |
| Notion / Obsidian | Task + notes management |
| Calendly / Microsoft Bookings | Scheduling automation |
| Zoom / Teams / Meet | Meeting management |
| Zapier / Power Automate | Workflow automation |
| LastPass / 1Password | Secure credential management |
| DocuSign / Adobe Sign | Digital signatures |

---

## Tier 5 — Search Queries

- "executive assistant best practices calendar management 2024"
- "GTD getting things done system digital tools implementation"
- "GDPR personal data handling email correspondence rules"
- "ISO 15489 records management document retention policy"
- "plain language writing principles government business communication"
- "meeting management framework agenda minutes follow-up"

---

## Domain Boundaries

| In Scope | Out of Scope |
|---|---|
| Calendar + scheduling management | Strategic decisions (→ tech_strategist) |
| Email drafting + triage | Technical documentation (→ professional_docs_writer) |
| Meeting prep + minutes | Architecture reviews (→ architect) |
| Travel + logistics coordination | Code implementation (→ engineer) |
| Task tracking + reminders | Compliance enforcement (→ compliance) |
| Document routing + filing | Requirements elicitation (→ pm_ba) |