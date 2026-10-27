"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:list of marketing campaign budgets.
# 2. Process:Loop through each budget, find its position,and calculate its percentage of the total
# 3. Out:One line for each budget with its position and percentage.
# 4. What I compute for each item, and why it is worth showing:The percentage shows how much each campaign contributesto the total budget, helping compare campaign spending.


# Your code below
# Reuse the budget list from Exercise 4.0
budgets = [500, 800, 1200, 650, 1500, 900, 700, 1750]

# Calculate the total budget
total = sum(budgets)

# Display each budget, its position, and its percentage of the total
for position, budget in enumerate(budgets, start=1):
    percentage = budget / total * 100
    print("Position:", position,
          "| Budget: €", budget,
          "| Share of total:", round(percentage, 2), "%")

