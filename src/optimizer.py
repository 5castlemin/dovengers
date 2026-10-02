"""TODO (V1): small enumeration oracle followed by MILP joint scheduling.

Owner: 남하원. Reviewer: 오성민.
Proposed interface (not implemented):
    solve_schedule(prices, jobs, site_limit, interval_hours, objective_config)
Minimize sum(price_eur_mwh * load_mw * interval_hours) with all jobs completed.
Report optimal/feasible/infeasible/timeout/error separately.
Scenario/CVaR and battery are future extensions, not current functionality.
"""
