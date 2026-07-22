import pandas as pd

# orders df expected columns: order_date, supplier_id, total_cost_usd, quantity,
# defect_flag, on_time_flag, actual_lead_time_days, supplier_region, supplier_country

data = pd.read_csv('/Users/AndreaLopera/Desktop/Data Science Portfolio/Procurement-Intelligence-Dashboard-main/data/synthetic_procurement_orders.csv').copy()
data["order_date"] = pd.to_datetime(data["order_date"])
data["month"] = data["order_date"].dt.to_period("M").dt.to_timestamp()  # month start

# Monthly supplier aggregates
monthly = (data
  .groupby(["supplier_id", "month"])
  .agg(
      total_spend=("total_cost_usd", "sum"),
      total_qty=("quantity", "sum"),
      defect_count=("defect_flag", "sum"),
      orders=("po_id", "count"),
      on_time=("on_time_flag", "sum"),
      avg_lead_time=("actual_lead_time_days", "mean"),
      region=("supplier_region", "first"),
      country=("supplier_country", "first"),
  )
  .reset_index()
)

# Rates
monthly["defect_rate"] = monthly["defect_count"] / monthly["orders"].clip(lower=1)
monthly["late_rate"]   = 1 - (monthly["on_time"] / monthly["orders"].clip(lower=1))

# Normalize PER MONTH (keeps scores comparable and stable month-to-month)
def minmax(s):
    return (s - s.min()) / (s.max() - s.min() + 1e-9)

monthly["avg_lead_time_norm"] = monthly.groupby("month")["avg_lead_time"].transform(minmax)
monthly["defect_rate_norm"]   = monthly.groupby("month")["defect_rate"].transform(minmax)
monthly["late_rate_norm"]     = monthly.groupby("month")["late_rate"].transform(minmax)
monthly["spend_share_norm"]   = monthly["total_spend"] / monthly.groupby("month")["total_spend"].transform("max").clip(lower=1e-9)

# Regional risk (example)
region_risk_map = {"North America":0.00,"Europe":0.02,"Asia":0.10,"South America":0.05}
monthly["region_risk"] = monthly["region"].map(region_risk_map).fillna(0.03)

# Weighted risk (0–100)
w_defect, w_late, w_lead, w_spend, w_region = 0.35, 0.30, 0.20, 0.10, 0.05
monthly["risk_score"] = 100 * (
    w_defect*monthly["defect_rate_norm"] +
    w_late*monthly["late_rate_norm"] +
    w_lead*monthly["avg_lead_time_norm"] +
    w_spend*monthly["spend_share_norm"] +
    w_region*monthly["region_risk"]
)

# This is your separate table to save (e.g., CSV/DB)
# Build & save the score table
risk_scores_monthly = (
    monthly[["supplier_id","month","risk_score"]]
      .rename(columns={"month":"score_month"})
      .sort_values(["supplier_id","score_month"])
)

risk_scores_monthly.to_csv(
    "/Users/AndreaLopera/Desktop/Data Science Portfolio/Procurement-Intelligence-Dashboard-main/data/supplier_risk_scores_monthly.csv",
    index=False
)