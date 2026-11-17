"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:User input for one marketing campaign entry: campaign_name (text), channel (text), spend_eur (positive float), and clicks (non-negative integer).
# 2. Process:Validate that text fields are non-empty and numeric fields are valid positive/non-negative numbers (re-prompting on unacceptable values). Check if 'campaign_expenses.csv' exists and is non-empty; if not, create it and write the header line first, then append the new row.
# 3. Out, file name and columns:Creates/appends to 'campaign_expenses.csv' with columns: campaign_name,channel,spend_eur,clicks
# 4. Why these columns, and what this file is for:These four columns capture the core identity, platform, cost, and engagement of each ad campaign. Once it has 200 rows, I can analyze which marketing channels deliver the lowest Cost Per Click (spend_eur / clicks) and reallocate next quarter's budget toward top-performing channels.


# Your code below
import csv
import os

FILENAME = "campaign_expenses.csv"
HEADERS = ["campaign_name", "channel", "spend_eur", "clicks"]

# 1. Collect and validate inputs
while True:
    campaign_name = input("Enter campaign name: ").strip()
    if campaign_name != "":
        break
    print("Campaign name cannot be empty. Please try again.")

while True:
    channel = input("Enter marketing channel (e.g., Instagram, Google, TikTok): ").strip()
    if channel != "":
        break
    print("Channel cannot be empty. Please try again.")

while True:
    spend_input = input("Enter campaign spend in EUR: ").strip()
    try:
        spend_eur = float(spend_input)
        if spend_eur > 0:
            break
        print("Spend must be greater than 0.")
    except ValueError:
        print("Invalid number. Please enter a numeric amount (e.g., 250.50).")

while True:
    clicks_input = input("Enter number of clicks: ").strip()
    try:
        clicks = int(clicks_input)
        if clicks >= 0:
            break
        print("Clicks cannot be negative.")
    except ValueError:
        print("Invalid number. Please enter a whole number (e.g., 120).")

# 2. Check if file exists and already has content (so header is only written once)
file_exists = os.path.exists(FILENAME) and os.path.getsize(FILENAME) > 0

with open(FILENAME, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(HEADERS)
    writer.writerow([campaign_name, channel, spend_eur, clicks])

print(f"Saved entry for '{campaign_name}' to {FILENAME}.")