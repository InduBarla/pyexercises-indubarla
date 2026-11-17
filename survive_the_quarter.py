# Name: Indu Barla
# Group: A (scenarios_A.csv)
#
# FOUR QUESTIONS BEFORE STARTING:
# 1. What goes in?
#    The player's name from keyboard input, their daily choices (A, B, or C), and the file
#    'scenarios_A.csv'. The CSV uses a comma (',') separator and has 14 columns:
#    ID, Scenario, OptionA, OptionB, OptionC, BudgetA, BudgetB, BudgetC,
#    ReputationA, ReputationB, ReputationC, FeedbackA, FeedbackB, FeedbackC.
#    All budget and reputation changes are written as signed whole numbers (integers).
#
# 2. What happens?
#    - Ask the player for their name and initialize budget = 10000, reputation = 50, streak = 0.
#    - Load all 33 scenarios from scenarios_A.csv and shuffle them randomly.
#    - Loop through up to 10 days: display the day number, current budget, and reputation.
#    - Show the day's situation and options A, B, and C, then ask until a valid letter is entered.
#    - Unpack the chosen option's tuple, update budget and reputation (capping reputation at 100),
#      and award a +500 EUR bonus if the player achieves 3 reputation gains in a row.
#    - Print the feedback and gauge changes, record the move in history, and stop immediately
#      if budget <= 0 or reputation <= 0.
#
# 3. What comes out?
#    At the end, the player sees whether they got fired (and which gauge hit 0) or survived
#    all 10 days, along with their final budget, reputation, calculated score, marketing title,
#    and their best and worst moves of the quarter. One summary row is also appended to
#    'results.csv' formatted as: name,budget,reputation,title,date
#
# 4. What could go wrong?
#    - The player types an invalid key like 'D', a number, or presses Enter: a while loop keeps
#      re-prompting cleanly until 'A', 'B', or 'C' is entered.
#    - Budget or reputation drops to 0 or below mid-quarter: the loop checks both gauges right
#      after each choice and breaks immediately with a fired message.
#    - 'scenarios_A.csv' is missing or empty: a try/except FileNotFoundError block catches it
#      and prints a clear message instead of crashing with a traceback.
#
# MANDATORY FEATURE CHOSEN:
# Option (a) — Streak bonus: three reputation gains in a row give +500 EUR.
# Why I chose it: As a marketing manager, building consistent brand trust over consecutive days
# should create positive business momentum and reward steady strategy with extra budget.

import csv
import random
from datetime import date

SCENARIO_FILE = "scenarios_A.csv"
RESULTS_FILE = "results.csv"
STARTING_BUDGET = 10000
STARTING_REPUTATION = 50
TOTAL_DAYS = 10


# Load all scenarios from scenarios_A.csv and store each option (A, B, C) as a 4-item tuple
def load_scenarios(filename):
    scenarios = []
    try:
        with open(filename, mode="r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not row.get("Scenario"):
                    continue
                scenario_data = {
                    "id": row["ID"].strip(),
                    "situation": row["Scenario"].strip(),
                    "options": {
                        "A": (
                            row["OptionA"].strip(),
                            int(row["BudgetA"]),
                            int(row["ReputationA"]),
                            row["FeedbackA"].strip(),
                        ),
                        "B": (
                            row["OptionB"].strip(),
                            int(row["BudgetB"]),
                            int(row["ReputationB"]),
                            row["FeedbackB"].strip(),
                        ),
                        "C": (
                            row["OptionC"].strip(),
                            int(row["BudgetC"]),
                            int(row["ReputationC"]),
                            row["FeedbackC"].strip(),
                        ),
                    },
                }
                scenarios.append(scenario_data)
    except FileNotFoundError:
        print(f"Error: Could not find '{filename}'. Please place it in the same folder.")
    return scenarios


# Ask the player to choose A, B, or C and keep asking until a valid option is entered
def get_player_choice():
    choice = input("Your choice (A, B or C): ").strip().upper()
    while choice not in ("A", "B", "C"):
        choice = input("Please type A, B or C: ").strip().upper()
    return choice


# Apply the chosen option's impact, cap reputation at 100, and return (budget, reputation) as a tuple
def apply_choice(budget, reputation, budget_change, rep_change):
    new_budget = budget + budget_change
    new_reputation = min(100, reputation + rep_change)
    return new_budget, new_reputation


# Calculate the final score and return the player's marketing title
def get_final_title(budget, reputation):
    score = reputation + (budget // 200)
    if score < 95:
        title = "Eternal Intern"
    elif score <= 119:
        title = "Growth Hacker"
    elif score <= 139:
        title = "CMO Material"
    else:
        title = "Viral Legend"
    return score, title


# Append one summary line for the completed game to results.csv (creating the header if the file is new)
def save_result(filename, player_name, budget, reputation, title):
    today_str = date.today().isoformat()
    file_has_content = False
    try:
        with open(filename, mode="r", encoding="utf-8") as check_file:
            if check_file.read().strip():
                file_has_content = True
    except FileNotFoundError:
        file_has_content = False

    with open(filename, mode="a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if not file_has_content:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([player_name, budget, reputation, title, today_str])


# Run the main 10-day game loop and print the end-of-quarter summary
def play_game():
    scenarios = load_scenarios(SCENARIO_FILE)
    if len(scenarios) < TOTAL_DAYS:
        print("Not enough scenarios loaded to play a 10-day quarter.")
        return

    print("=== SURVIVE THE QUARTER: CROISSANT ROCKET ===")
    player_name = input("Enter your name, Marketing Manager: ").strip()
    while not player_name:
        player_name = input("Please enter a valid name: ").strip()

    random.shuffle(scenarios)
    selected_scenarios = scenarios[:TOTAL_DAYS]

    budget = STARTING_BUDGET
    reputation = STARTING_REPUTATION
    rep_streak = 0
    history = []
    fired_reason = ""

    # Play through each of the 10 days unless a gauge hits 0 or less
    for day in range(1, TOTAL_DAYS + 1):
        current = selected_scenarios[day - 1]
        print(f"\nDay {day}")
        print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
        print(current["situation"])
        print(f"A: {current['options']['A'][0]}")
        print(f"B: {current['options']['B'][0]}")
        print(f"C: {current['options']['C'][0]}")

        choice = get_player_choice()
        option_text, budget_change, rep_change, feedback = current["options"][choice]

        budget, reputation = apply_choice(budget, reputation, budget_change, rep_change)

        # Feature (a): Streak bonus — three reputation gains in a row give +500 EUR
        if rep_change > 0:
            rep_streak += 1
            if rep_streak == 3:
                budget += 500
                print("STREAK BONUS! 3 reputation gains in a row: +500 EUR added to your budget!")
                rep_streak = 0
        else:
            rep_streak = 0

        print(feedback)
        print(f"Budget {budget_change:+d} EUR, Reputation {rep_change:+d}")

        # Store (reputation_change, day, option_text) so tuple comparison ranks moves by reputation impact
        history.append((rep_change, day, option_text))

        if budget <= 0:
            fired_reason = "Your budget hit 0 EUR or less. The bank shut down Croissant Rocket."
            break
        if reputation <= 0:
            fired_reason = "Your reputation hit 0/100 or less. The internet cancelled Croissant Rocket."
            break

    print("\n==============================")
    if fired_reason:
        final_title = "Fired"
        print("YOU ARE FIRED!")
        print(fired_reason)
        print(f"Final Budget: {budget} EUR | Final Reputation: {reputation}/100")
        print(f"{player_name}, your title: {final_title}")
    else:
        score, final_title = get_final_title(budget, reputation)
        print("Quarter survived!")
        print(f"Budget left: {budget} EUR, reputation: {reputation}/100")
        print(f"Final score: {score}")
        print(f"{player_name}, your title: {final_title}")

    # Find best and worst moves using tuple comparison on (rep_change, day, option_text)
    if history:
        best_move = max(history)
        worst_move = min(history)
        print(f'Best move: day {best_move[1]}, "{best_move[2]}" ({best_move[0]:+d})')
        print(f'Worst move: day {worst_move[1]}, "{worst_move[2]}" ({worst_move[0]:+d})')

    save_result(RESULTS_FILE, player_name, budget, reputation, final_title)
    print(f"Saved in {RESULTS_FILE}")


if __name__ == "__main__":
    play_game()