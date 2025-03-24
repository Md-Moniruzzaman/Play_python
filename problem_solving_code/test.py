from datetime import datetime, timedelta, timezone

# Get the current time in UTC
utc_now = datetime.now(timezone.utc)

# Convert UTC to Dhaka time (UTC + 6 hours)
dhaka_time = utc_now + timedelta(hours=6)

# Extract only the date (YYYY-MM-DD)
dhaka_date = dhaka_time.date()

print(dhaka_date)
