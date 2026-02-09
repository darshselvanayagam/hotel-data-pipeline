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
```

---

## Pipeline Flow

1. A CSV file is uploaded into the **S3 raw folder**
2. S3 event triggers **AWS Lambda**
3. Lambda starts **Glue ETL job**
4. Glue cleans & standardizes data
5. Cleaned data saved to **curated S3 folder**
6. Snowflake loads curated data from S3
7. Metabase dashboards visualize analytics

---

## Technologies Used

### Cloud & Storage
- AWS S3
- AWS IAM
- AWS Lambda
- AWS Glue (Python Shell)

### Data Warehouse
- Snowflake
- External Stage & Storage Integration

### Visualization
- Metabase (self-hosted using Docker)

### Programming
- Python (Pandas, Boto3)
- SQL

### Dev Tools
- Git & GitHub
- Docker

---

## Data Transformations (Glue ETL)

- Convert city codes → full city names
- Clean null values
- Cast data types
- Round hotel prices
- Output analytics-ready dataset

---

## Snowflake Processing

- Auto-suspend warehouse to reduce cost
- External stage reading S3 curated data
- `COPY INTO` loads structured table

---

## Analytics Dashboard Metrics

- Average hotel price by city
- Availability percentage by city
- Price trend over time

---

## Project Structure

```
hotel-data-pipeline/
│
├── data_generator/
│   └── generate_mock_hotels.py
│
├── glue_job/
│   └── clean_hotels_glue.py
│
├── lambda_trigger/
│   └── trigger_glue_lambda.py
│
├── sql/
│   ├── snowflake_setup.sql
│   └── analytics_queries.sql
│
└── README.md
```

---

## How To Run (High Level)

1. Upload CSV into S3 `/raw`
2. Glue job runs automatically
3. Clean data written to `/curated`
4. Run `COPY INTO` in Snowflake
5. View dashboards in Metabase

---

## Learning Outcomes

- Build event-driven pipelines
- Design data lake → warehouse architecture
- Use serverless ETL
- Secure Snowflake-AWS integration
- Create analytics-ready datasets

---

## Future Improvements

- Automate load using Snowpipe
- Add Airflow orchestration
- Add streaming ingestion (Kafka)
- Add data quality checks

---

## Author
Viswadarshini Selvanayagam
