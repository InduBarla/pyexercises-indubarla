"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The user enters an answer until they get it right or run out of attempts.
# 2. Process: A while loop checks the answer and counts each attempt.
# 3. Out: A message showing whether the user succeeded and how many attempts they used.
# 4. My stop condition, my attempt limit, my summary:The answer is "yes" (case-insensitive).3 tries success or failure and attempts used.


# Your code below
# Set the correct answer and maximum attempts
correct_answer = "yes"
maximum_attempts = 3
attempts = 0
success = False

# Keep asking until the answer is correct or attempts run out
while attempts < maximum_attempts and not success:
    answer = input("Do you understand Python while loops? Answer: ")
    attempts += 1

    # Accept uppercase and extra spaces too
    if answer.strip().lower() == correct_answer:
        success = True
        print("Correct! Well done.")
    else:
        print("That is not the expected answer. Try again.")

# Display the final summary
print("Attempts used:", attempts)

if success:
    print("Summary: You answered correctly.")
else:
    print("Summary: You reached the maximum number of attempts.")