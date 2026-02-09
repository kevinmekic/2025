---
name: limited-codex-merch-drop
description: Plan and execute a stealth/hidden limited Codex merchandise drop with secrecy controls, inventory gating, launch timeline, communications, and post-drop analysis. Use for surprise, invite-only, unlisted, password-gated, or limited merch launch requests.
---

# Limited Codex Merch Drop

Use this skill when the user wants a **hidden or surprise** release for Codex-branded merchandise.

## What this skill does

- Produces a practical launch plan that balances secrecy, fairness, and fulfillment reliability.
- Chooses an access model (invite/password/unlisted) and a fallback model.
- Adds anti-bot and anti-oversell controls before launch.
- Produces concise launch copy (teaser, live, sold-out) plus a post-drop metrics template.

## Fast intake (ask first)

Collect these inputs before proposing the plan:

1. Total units and per-SKU limits.
2. Launch date/time in UTC and target regions.
3. Store platform constraints (e.g., Shopify, custom checkout).
4. Desired secrecy level:
   - **Soft-hidden**: unlisted URL + low-friction gating.
   - **Hard-hidden**: invite-only codes + strict limits.
5. Success metric priority (speed, fairness, revenue, or low support volume).

If the user omits any item, provide assumptions explicitly.

## Core workflow

1. **Define constraints**
   - Confirm quantities, SKU count, regions, fulfillment caps, and support staffing.

2. **Design access + fallback**
   - Recommend one primary model and one fallback.
   - Default priority:
     1) unique invite codes,
     2) password-protected landing page,
     3) unlisted URL with rate limiting.

3. **Apply protections**
   - Queue/rate limit at launch.
   - Cart reservation timeout (5–10 min).
   - Inventory hold on checkout start.
   - Per-customer caps and duplicate detection.

4. **Prepare launch comms**
   - Draft teaser, live, and sold-out copy.
   - Include UTC time and access instructions.
   - Do not publish full stock counts pre-launch.

5. **Run readiness checks**
   - T-24h and T-1h checks for payment, shipping, taxes, and email flows.
   - Verify secret-link leakage with logged-out tests.
   - Document rollback criteria and owner.

6. **Post-drop review**
   - Report sell-through time, conversion, payment failure, support load, and blocked bot attempts.
   - Propose one secrecy improvement and one conversion improvement.

## Output contract

Return sections in this exact order:

1. **Drop Brief** (goal, audience, quantity, risk level)
2. **Assumptions**
3. **Access Design** (primary + fallback)
4. **Run of Show** (T-7d to T+1d)
5. **Comms Pack** (teaser/live/sold-out)
6. **Risk Register** (top 5 risks + mitigations + owner)
7. **Post-Drop Metrics Template**

## Guardrails

- Do not provide instructions to bypass platform security, payment controls, or legal requirements.
- Optimize for fair access and operational stability over maximizing checkout velocity.
- If constraints are contradictory (e.g., ultra secrecy + broad reach), call out tradeoffs clearly.

## References

- Operational timeline and checks: `references/hidden-drop-checklist.md`
- Fill-in template for execution docs: `references/drop-runbook-template.md`
- Reusable copy snippets: `references/comms-templates.md`
