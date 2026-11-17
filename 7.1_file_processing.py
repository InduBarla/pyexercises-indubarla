"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# -Blank lines appear between names (lines 3 and 9 are empty).
# - Leading whitespace/spaces appear before some names ("  alan TURING" and "  linus torvalds").
# - Inconsistent capitalization across lines (all lowercase like "grace hopper", uppercase surnames like "ada LOVELACE", and uppercase first names like "GUIDO van rossum").
# -One name has a two-word last name with a particle ("GUIDO van rossum"), so taking only the very last word would miss "van".

# 1. In:'names.txt' containing 10 lines (8 full names and 2 blank lines) with messy spacing and capitalization.
# 2. Process, problem by problem:- Blank lines: strip each line and skip it if it is empty (`if not clean_line: continue`), reducing 10 lines to 8 valid names.
#    - Leading/trailing spaces: use `.strip()` to remove extra spaces at the start and end of each line.
#    - Inconsistent capitalization: apply `.title()` so every name is standardized to "First Last" (e.g., "Ada Lovelace", "Guido Van Rossum").
#    - Multi-word last name & sorting: split on the first space (`split(" ", 1)[1]`) to extract the full last name (e.g., "Van Rossum", "Hopper") and sort alphabetically with `sorted()`.
# 3. Out:A new file 'cleaned_names.txt' containing the 8 cleaned, Title-Cased names sorted alphabetically by last name, leaving 'names.txt' untouched.
# 4. How I decide which word is the last name:How I decide which word is the last name: Each line starts with a single first name followed by a space and the surname (which may be one word like "Hopper" or two words like "Van Rossum"). Splitting once on the first space (`name.split(" ", 1)[1]`) treats everything after the first name as the last name.


# Your code below
INPUT_FILE = "names.txt"
OUTPUT_FILE = "cleaned_names.txt"

def get_last_name(full_name):
    parts = full_name.split(" ", 1)
    if len(parts) > 1:
        return parts[1].lower()
    return parts[0].lower()

cleaned_names = []

with open(INPUT_FILE, mode="r", encoding="utf-8") as infile:
    for line in infile:
        clean_line = line.strip()
        if not clean_line:
            continue
        formatted_name = clean_line.title()
        cleaned_names.append(formatted_name)

sorted_names = sorted(cleaned_names, key=get_last_name)

with open(OUTPUT_FILE, mode="w", encoding="utf-8") as outfile:
    for name in sorted_names:
        outfile.write(name + "\n")

print(f"Processed {len(sorted_names)} names into {OUTPUT_FILE}.")