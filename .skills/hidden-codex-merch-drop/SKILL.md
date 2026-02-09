---
name: hidden-codex-merch-drop
description: Design and operate a hidden Codex merch drop (surprise/invite-only/unlisted) with gating, anti-bot controls, launch comms, and a ready-to-run response format. Use when users want a stealth merch release and ask for a practical launch plan.
---

# Hidden Codex Merch Drop

Use this skill for secret, surprise, or invite-only Codex merchandise launches.

## Fast Intake

Collect:
1. Launch datetime (UTC)
2. Total units + per-customer cap
3. Regions + fulfillment constraints
4. Secrecy mode: `soft-hidden` or `hard-hidden`
5. Platform constraints (Shopify/custom/etc.)

If inputs are missing, list assumptions before planning.

## Workflow

1. **Scope**: objective, audience, risk level.
2. **Access design**: choose primary gate + fallback gate.
3. **Protection controls**: queue/rate limit, cart timeout, per-user caps.
4. **Run of show**: T-7d, T-24h, T-1h, T+0, T+4h.
5. **Comms**: teaser, drop-live, sold-out.
6. **Post-drop**: metrics + two improvements.

## Required Output Format

Return exactly these sections:
1. **Drop Brief**
2. **Assumptions**
3. **Access Design (Primary + Fallback)**
4. **Run of Show Timeline**
5. **Comms Pack**
6. **Top Risks & Mitigations**
7. **Post-Drop Metrics Template**

## Let me try it

If the user asks to try it, provide this starter prompt:

```text
Use hidden-codex-merch-drop. Plan a hard-hidden Codex merch drop for 250 total units across US/EU. Launch at 2026-03-15 17:00 UTC. Platform is Shopify. Limit 1 per customer. Optimize for fairness over speed.
```

## Reference

Use `references/launch-checklist.md` for default checks.
