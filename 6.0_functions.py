"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A list of marketing campaign budgets (numbers in euros).
# 2. Process:Check if the list is empty; if not, divide the total sum of budgets by the number of campaigns.
# 3. Out:Returns the average campaign budget as a number (or 0 if the list is empty).
# 4. My function name, and why return rather than print:
#    Function name: calculate_average_budget — yes, the name clearly tells you it computes the average budget without reading the code.
#    Why return matters: 'return' hands the calculated number back to the rest of the program so you can save it in a variable, compare it, or reuse it in other math. 'print' only shows text on the screen and throws the value away.
#    Empty list check: When called with [], dividing sum(budgets) / len(budgets) would normally crash with a ZeroDivisionError. Handling it to return 0 is acceptable because an empty list of campaigns has 0 average spend.


# Your code below
def calculate_average_budget(budgets):
    if len(budgets) == 0:
        return 0
    return sum(budgets) / len(budgets)

# Call 1: Using the original list from Exercise 4.0
q1_budgets = [500, 800, 1200, 650, 1500, 900, 700, 1750]
avg_q1 = calculate_average_budget(q1_budgets)
print("Q1 Average Budget:", avg_q1)

# Call 2: Using a second set of campaign budgets
q2_budgets = [1000, 2000, 1500]
avg_q2 = calculate_average_budget(q2_budgets)
print("Q2 Average Budget:", avg_q2)

# Call 3: Using a third set of campaign budgets
q3_budgets = [400, 600, 800, 1000]
avg_q3 = calculate_average_budget(q3_budgets)
print("Q3 Average Budget:", avg_q3)

# Empty list check
empty_avg = calculate_average_budget([])
print("Empty List Average Budget:", empty_avg)