# Hidden Drop Checklist

## T-7d Planning
- Finalize SKU list, unit counts, and hard-stop inventory.
- Confirm packaging SLAs, carrier cutoffs, and return policy copy.
- Lock access model and fallback path.
- Set per-customer caps and blocked-country logic.

## T-3d Dry Run
- Test secret URL behavior in incognito and mobile.
- Validate invite/password edge cases (invalid, expired, already used).
- Simulate 10x expected launch traffic.
- Verify event logging for queue joins, checkouts, and failures.

## T-24h Readiness
- Verify payment gateways, fraud filters, and 3DS behavior.
- Verify taxes/shipping by target region.
- Check confirmation emails (order placed, failed payment, sold out).
- Prepare support macros and escalation channel.

## T-1h Launch Freeze
- Freeze catalog and checkout config edits.
- Enable rate limiting, bot controls, and queue banner.
- Pre-stage announcement copy and support status page.
- Confirm rollback owner and on-call contacts.

## T+0 Launch
- Send access message with UTC timestamp.
- Monitor checkout errors, queue latency, and payment decline spikes.
- Trigger fallback flow if errors exceed threshold.

## T+4h Wrap
- Publish sold-out or inventory-low update.
- Export order, payment, and bot-block reports.
- Capture incident notes while fresh.

## Post-Drop Metrics
- Sell-through time (minutes)
- Conversion rate (%)
- Payment failure rate (%)
- Average order value
- Support tickets per 100 orders
- Suspected bot attempts blocked
