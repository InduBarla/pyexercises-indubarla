"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Information about a fashion marketing campaign.
# 2. Process:Create a dictionary, read and update a value,remove one field, and display all remaining fields.
# 3. Out:The selected value, updated value, and remaining fields.
# 4. My object, my five fields, and why those:I describe a  fashion campaign using its name, brand,channel, budget, and target audience. These fields are useful for understanding and managing a marketing campaign.


# Your code below
# Create a dictionary describing a luxury fashion campaign
campaign = {
    "campaign_name": "Summer Collection 2027",
    "brand": "Dior",
    "channel": "Instagram",
    "budget": 50000,
    "target_audience": "Young luxury consumers"
}

# Read and display one field
print("Brand:", campaign["brand"])

# Change the value of one field
campaign["budget"] = 60000
print("Updated budget:", campaign["budget"])

# Remove one field
del campaign["channel"]

# Display every remaining field and its value
print("Campaign details:")
for key, value in campaign.items():
    print(key, ":", value)

# Check what happens when a field does not exist
# Using .get() avoids an error and returns "Not available".
print("Campaign location:", campaign.get("location", "Not available"))
