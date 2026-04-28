# Retail Analytics Project

## Project Overview

This project analyzes retail sales data to identify customer behavior, revenue trends, and business opportunities using Python, SQL, PostgreSQL, Power BI, Docker, CI/CD, and Microsoft Azure.

The objective is to simulate a real professional data workflow from data processing to cloud deployment and business dashboarding.

---

## Tech Stack

* Python (Pandas, NumPy, SQLAlchemy)
* SQL
* PostgreSQL
* Power BI
* Docker
* Git & GitHub
* GitHub Actions (CI/CD)
* Microsoft Azure PostgreSQL Flexible Server

---

## Project Architecture

```text
Raw Data
↓
Python ETL Pipeline
↓
PostgreSQL Database
↓
Power BI Dashboard
↓
Business Insights
```

---

## Key Features

* Retail sales data analysis using Python and SQL
* Automated ETL pipeline for data loading
* PostgreSQL database design and management
* Local deployment using Docker for reproducibility
* Interactive Power BI dashboard for KPIs and reporting
* CI/CD workflow using GitHub Actions
* Cloud deployment of PostgreSQL on Microsoft Azure

---

## Business KPIs

The dashboard focuses on:

* Revenue trends
* Top-selling products
* Customer segmentation
* Regional sales performance
* Monthly sales evolution
* Business recommendations

---
## Key Business Insights

- The company generated approximately 8.9M in total revenue.

- Revenue is highly concentrated in the United Kingdom, which represents the vast majority of total sales.

- Around 33% of customers are at risk of churn (no purchase in the last 90 days), indicating a significant retention issue.

- Only a small group of 274 VIP customers (high spenders) contribute disproportionately to revenue.

## Power BI Dashboard

### Dashboard Preview

![Sales_Overview](powerbi/Image.png)

![Customer_Segmentation](powerbi/Image1.png)

![Business_Recommendations](powerbi/Image2.png)

![Summary](powerbi/Image3.png)

---

## Docker Usage

Build the Docker image:

```bash
docker build -t retail-analytics-project .
```

Run the container:

```bash
docker run retail-analytics-project
```

---

## Cloud Deployment

PostgreSQL was deployed to Microsoft Azure PostgreSQL Flexible Server to simulate a production-ready cloud architecture.

This project demonstrates both:

-Local deployment (Docker + PostgreSQL)
-Cloud deployment (Azure PostgreSQL)

---

## CI/CD

GitHub Actions automatically verifies project quality on each push to GitHub.

---

## Author

Sidbewendin Angelique Yameogo