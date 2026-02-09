import csv
import random
from datetime import datetime, timedelta

# Output file
filename = "mock_hotels.csv"

hotel_names = [
    "Grand Plaza", "Ocean View", "City Inn",
    "Mountain Retreat", "Sunny Suites"
]

# City codes (we will clean later in Glue)
city_codes = ["TOR", "NYC", "PAR", "TYO", "DXB"]

num_rows = 100

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)

    # header
    writer.writerow(["hotel_id", "hotel_name", "city", "date", "price", "availability"])

    for i in range(1, num_rows + 1):
        hotel_id = i
        hotel_name = random.choice(hotel_names)
        city = random.choice(city_codes)

        date = (datetime.today() + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")

        # keep decimals → will clean in Glue
        price = round(random.uniform(50, 500), 2)

        availability = random.choice([True, False])

        writer.writerow([hotel_id, hotel_name, city, date, price, availability])

print("File generated: mock_hotels.csv with 100 rows")
