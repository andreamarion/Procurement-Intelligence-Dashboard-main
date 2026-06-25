# Procurement Intelligence Dashboard

## Overview

This project simulates a heavy equipment procurement and supplier performance environment using Python-generated supply chain data and Tableau dashboards.

The goal of the project is to create a procurement analytics dashboard that helps users understand spend concentration, supplier performance, delivery reliability, quality issues, and supplier risk. The project is based on synthetic data, but the logic was designed to reflect realistic procurement and operations scenarios, including purchase orders, supplier lead times, defect rates, cost of poor quality, and supplier risk scoring.

The first completed dashboard is the **Executive Overview** for Spend Analytics. Additional dashboard pages for **Supplier Performance** and **Risk** are currently in progress.

## Business Problem

Procurement teams need visibility into where money is being spent, which suppliers represent the largest share of spend, and where operational risks may exist across delivery performance, quality, and supplier concentration.

This dashboard is designed to answer questions such as:

* Which suppliers account for the largest share of total spend?
* Which categories drive the most procurement cost?
* How is spend distributed by country and region?
* What is the overall on-time and in-full delivery performance?
* What is the defect rate across suppliers and categories?
* Which suppliers may require closer monitoring based on cost, quality, and delivery risk?

## Tools Used

* **Python** — data simulation, data preparation, risk-score generation, and exploratory analysis
* **Pandas** — dataset creation and transformation
* **Tableau** — dashboard design, calculated fields, KPIs, filters, and visual analytics
* **GitHub** — project documentation and version control

## Data Creation Process

This project uses three synthetic CSV files:

### 1. `synthetic_procurement_orders.csv`

This was the original simulated procurement dataset. It includes purchase order activity for heavy equipment components, including order dates, suppliers, parts, categories, quantities, unit costs, total cost, lead times, on-time delivery flags, and defect indicators.

### 2. `supplier_risk_scores_monthly.csv`

This file contains monthly supplier risk scores by supplier. It was created to support supplier risk analysis and trend-based monitoring.

### 3. `orders_with_risk_score.csv`

This is the final enriched dataset used as the master Tableau data source. It combines the original procurement order data with supplier risk scoring information.

This is the primary dataset used in the Tableau workbook.

## Python Files

### `01_data_simulation.ipynb`

Used to simulate the original procurement dataset. The notebook creates:

* Heavy equipment component categories
* Part types and units of measure
* Supplier profiles
* Supplier countries and regions
* Purchase order records
* Lead time behavior
* Defect flags and defect reasons
* Total cost calculations

### `risk_scores.py`

Used to generate supplier risk scoring logic and support the creation of monthly supplier risk data.

## Main Dataset Fields

| Field                     | Description                                                                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `order_date`              | Date when the purchase order was placed                                                                                             |
| `po_id`                   | Unique purchase order identifier                                                                                                    |
| `supplier_id`             | Unique supplier identifier                                                                                                          |
| `supplier_region`         | Geographic region of the supplier                                                                                                   |
| `supplier_country`        | Supplier country                                                                                                                    |
| `part_id`                 | Unique part identifier                                                                                                              |
| `part_type`               | Type of heavy equipment part                                                                                                        |
| `category`                | Procurement category, such as Steel, Hydraulics, Engines, Electronics, Undercarriage, Filters, Attachments, and Lubricants & Fluids |
| `unit_of_measure`         | Unit used for the order quantity, such as each, pound, gallon, foot, or pack                                                        |
| `quantity`                | Ordered quantity                                                                                                                    |
| `delivery_qty`            | Delivered quantity used to support in-full delivery analysis                                                                        |
| `unit_cost_usd`           | Unit cost in U.S. dollars                                                                                                           |
| `total_cost_usd`          | Total purchase order cost                                                                                                           |
| `promised_lead_time_days` | Agreed supplier lead time at the time of order                                                                                      |
| `actual_lead_time_days`   | Actual delivery lead time                                                                                                           |
| `on_time_flag`            | Indicates whether the order was delivered on time                                                                                   |
| `in_full_flag`            | Indicates whether the order was delivered in full                                                                                   |
| `otif_flag`               | On-Time, In-Full delivery indicator                                                                                                 |
| `defect_flag`             | Indicates whether a quality defect was recorded                                                                                     |
| `defect_reason`           | Reason for defect, when applicable                                                                                                  |
| `risk_score_month`        | Month associated with the supplier risk score                                                                                       |
| `risk_score`              | Supplier risk score used for supplier risk monitoring                                                                               |

## Dashboard Pages

### Executive Overview

![Executive Overview](dashboard/ExecutiveOverview.png)

Status: **Completed**

The Executive Overview dashboard provides a high-level view of procurement performance, including:

* Total spend
* Average supplier spend
* Cost of poor quality
* OTIF percentage
* Defect rate
* Top suppliers by spend
* Top categories by spend
* Supplier spend concentration
* Spend distribution by country

### Supplier Performance

Status: **In Progress**

Planned focus areas include:

* Supplier-level delivery performance
* Lead time variance
* Supplier quality trends
* On-time delivery comparison
* Supplier ranking and drill-downs

### Risk

Status: **In Progress**

Planned focus areas include:

* Supplier risk score trends
* High-risk supplier identification
* Risk distribution by supplier, region, or category
* Relationship between risk, quality, delivery, and spend concentration

## Key Metrics

| Metric                       | Description                                                             |
| ---------------------------- | ----------------------------------------------------------------------- |
| Total Spend                  | Sum of total procurement cost                                           |
| Average Supplier Spend       | Average spend across suppliers                                          |
| OTIF (%)                     | Percentage of orders delivered on time and in full                      |
| Defect Rate                  | Percentage of orders with recorded defects                              |
| COPQ ($)                     | Estimated cost of poor quality based on defective or problematic orders |
| Supplier Spend Concentration | Share of total spend represented by the largest suppliers               |
| Lead Time Variance           | Difference between promised and actual lead time                        |
| Risk Score                   | Monthly supplier risk indicator                                         |

## Project Status

This project is currently in progress.

Completed:

* Synthetic procurement data simulation
* Supplier risk score dataset creation
* Enriched master dataset creation
* Executive Overview dashboard
* Tableau packaged workbook setup

In progress:

* Supplier Performance dashboard
* Risk dashboard
* Final dashboard polish
* Tableau Public publishing
* README and portfolio documentation

## Notes

This project uses fully simulated data. It does not represent any real company, supplier, or procurement system.

The purpose of the project is to demonstrate how procurement and supplier performance data can be modeled, enriched, and visualized for operational decision-making.
