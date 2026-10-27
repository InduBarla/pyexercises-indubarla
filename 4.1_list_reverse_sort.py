"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The campaign budget list created in Exercise 4.0.
# 2. Process:Create four different orders of the list and check whether each method changes the original list.
# 3. Out:Four reordered lists and the original list at the end.
# 4. My four orders, and which ones modify the original: I use reverse(), sorted(), sort(), and reversed(). reverse() and sort() modify the original list;sorted() and reversed() create new results.


# Your code below

# Original list from Exercise 4.0
budgets = [500, 800, 1200, 650, 1500, 900, 700, 1750]

# Keep a copy to check whether the original list changes
original_budgets = budgets.copy()

# Order 1: Reverse the original list in place
budgets.reverse()
print("1. Reversed list:", budgets)

# Restore the original order
budgets = original_budgets.copy()

# Order 2: Sort the original list in place
budgets.sort()
print("2. Sorted list:", budgets)

# Restore the original order
budgets = original_budgets.copy()

# Order 3: Create a sorted copy in descending order
descending_budgets = sorted(budgets, reverse=True)
print("3. Descending order:", descending_budgets)

# Order 4: Create a reversed copy without changing the original
reversed_budgets = list(reversed(budgets))
print("4. Reversed copy:", reversed_budgets)

# Confirm the original list is unchanged
print("Original list unchanged:", budgets == original_budgets)
print("Original list:", budgets)