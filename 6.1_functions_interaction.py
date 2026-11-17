"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A list of marketing campaign budgets in euros.
# 2. Process, function by function:Process, function by function:
#    - calculate_total_budget: sums all numbers in the budget list.
#    - count_campaigns: counts the number of items in the budget list.
#    - find_highest_budget: finds the maximum value in the budget list.
#    - summarize_campaign_budgets: calls those three functions to compute the total, average (total / count), and highest budget, returning a summary dictionary.
# 3. Out:A dictionary containing the total budget, average budget, and highest single campaign budget.
# 4. The question my fourth function answers:The question my fourth function answers:
#    Question: "What are the total, average, and peak campaign budgets for this marketing quarter?"
#    Why splitting into three makes it easier to check: Each small function has one clear input and output, so you can verify each piece independently with simple numbers before combining them into the final calculation.

# Three test cases for the three small functions:
# Test 1 (calculate_total_budget): input [100, 200, 300] -> expected output 600
# Test 2 (count_campaigns): input [100, 200, 300] -> expected output 3
# Test 3 (find_highest_budget): input [100, 200, 300] -> expected output 300
# Your code below
def calculate_total_budget(budgets):
    return sum(budgets)

def count_campaigns(budgets):
    return len(budgets)

def find_highest_budget(budgets):
    if len(budgets) == 0:
        return 0
    return max(budgets)

def summarize_campaign_budgets(budgets):
    total = calculate_total_budget(budgets)
    count = count_campaigns(budgets)
    highest = find_highest_budget(budgets)
    average = total / count if count > 0 else 0
    return {
        "total_budget": total,
        "average_budget": average,
        "highest_budget": highest
    }

# Individual checks on the three small functions
sample = [100, 200, 300]
print("Test total:", calculate_total_budget(sample))       # Expected: 600
print("Test count:", count_campaigns(sample))              # Expected: 3
print("Test highest:", find_highest_budget(sample))        # Expected: 300

# Full summary using my Exercise 4.0 campaign budgets
campaign_budgets = [500, 800, 1200, 650, 1500, 900, 700, 1750]
summary = summarize_campaign_budgets(campaign_budgets)
print("Campaign Budget Summary:", summary)