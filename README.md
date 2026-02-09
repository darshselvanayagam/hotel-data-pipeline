# Hotel Data Pipeline (AWS + Snowflake + Metabase)

An end-to-end data engineering project that ingests hotel pricing data, transforms it using AWS Glue, loads it into Snowflake, and visualizes analytics dashboards using Metabase.

This project demonstrates a modern cloud analytics architecture using serverless ETL, data lake storage, warehouse analytics, and BI dashboards.

---

## Architecture Diagram

```mermaid
flowchart LR
    A[Upload CSV to S3 Raw] --> B[S3 Event Notification]
    B --> C[AWS Lambda Trigger]
    C --> D[AWS Glue ETL Job]
    D --> E[S3 Curated Data]
    E --> F[Snowflake External Stage]
    F --> G[Snowflake Table]
    G --> H[Metabase Dashboard]
