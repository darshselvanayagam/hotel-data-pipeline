import os
import urllib.parse
import boto3

glue = boto3.client("glue")

def lambda_handler(event, context):
    if os.environ.get("RUN_ENABLED", "false").lower() != "true":
        print("RUN_ENABLED is false. Skipping Glue trigger.")
        return {"status": "disabled"}

    job_name = os.environ["GLUE_JOB_NAME"]

    for record in event.get("Records", []):
        bucket = record["s3"]["bucket"]["name"]
        key = urllib.parse.unquote_plus(record["s3"]["object"]["key"])

        # Only trigger for raw/*.csv
        if not key.startswith("raw/") or not key.endswith(".csv"):
            print(f"Skipping key: {key}")
            continue

        print(f"Starting Glue job {job_name} for s3://{bucket}/{key}")

        response = glue.start_job_run(
            JobName=job_name,
            Arguments={
                "--SOURCE_BUCKET": bucket,
                "--SOURCE_KEY": key,
                "--TARGET_PREFIX": "curated/mock_hotels_cleaned/"
            }
        )
        print(f"Started Glue RunId: {response['JobRunId']}")

    return {"status": "ok"}
