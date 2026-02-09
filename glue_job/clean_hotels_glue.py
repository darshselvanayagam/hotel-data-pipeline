import sys
import math
import boto3
import pandas as pd
from io import StringIO

def get_arg(name: str):
    # Glue passes args like: --SOURCE_BUCKET value
    if f"--{name}" in sys.argv:
        return sys.argv[sys.argv.index(f"--{name}") + 1]
    return None

SOURCE_BUCKET = get_arg("SOURCE_BUCKET")
SOURCE_KEY = get_arg("SOURCE_KEY")
TARGET_PREFIX = get_arg("TARGET_PREFIX") or "curated/mock_hotels_cleaned/"

if not SOURCE_BUCKET or not SOURCE_KEY:
    raise ValueError("Missing required args: SOURCE_BUCKET and SOURCE_KEY")

print(f"Input: s3://{SOURCE_BUCKET}/{SOURCE_KEY}")
print(f"Output prefix: s3://{SOURCE_BUCKET}/{TARGET_PREFIX}")

s3 = boto3.client("s3")

# ---- Read CSV from S3 ----
obj = s3.get_object(Bucket=SOURCE_BUCKET, Key=SOURCE_KEY)
csv_text = obj["Body"].read().decode("utf-8")

df = pd.read_csv(StringIO(csv_text))

print("Before transform (sample):")
print(df.head(5))

# ---- Transform: city codes -> full names ----
city_map = {
    "TOR": "Toronto",
    "NYC": "New York",
    "PAR": "Paris",
    "TYO": "Tokyo",
    "DXB": "Dubai"
}

df["city"] = df["city"].map(city_map).fillna("Unknown")

# ---- Transform: price -> whole number rounded up ----
# Ensure numeric first (in case it came as string)
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["price"] = df["price"].fillna(0).apply(lambda x: int(math.ceil(x)))

print("After transform (sample):")
print(df.head(5))

# ---- Write cleaned CSV back to S3 ----
out_key = f"{TARGET_PREFIX}cleaned_hotels.csv"
out_csv = df.to_csv(index=False)

s3.put_object(
    Bucket=SOURCE_BUCKET,
    Key=out_key,
    Body=out_csv.encode("utf-8"),
    ContentType="text/csv"
)

print(f"Wrote cleaned file to s3://{SOURCE_BUCKET}/{out_key}")
