"""TODO (V1): agree and implement shared Job, Price and ScheduleResult contracts.

Owners: 남하원 + 오성민. Integration review: 정병주.
Jobs: id, release, deadline (exclusive end), duration (slots), mw.
Prices: timestamps, eur_per_mwh, interval_hours, timezone, information mode.
Results: solver status, starts/ends, load_mw, cost proxy, warnings and metadata.
Reject invalid inputs; do not represent infeasible schedules as zero-cost success.
No schema or validator is implemented yet.
"""
