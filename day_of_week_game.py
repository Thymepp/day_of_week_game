"""
Day of the Week Game
A random date is shown and the player guesses which day of the week it falls on.
"""

import random
from datetime import date, timedelta

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

ROUNDS = 10
LEVELS = {
    "1": ("Easy (current year ±1)", 1),
    "2": ("Medium (±20 years)", 20),
    "3": ("Hard (±100 years)", 100),
}


def random_date(year_range: int) -> date:
    """Pick a random date within year_range years of the current year."""
    today = date.today()
    start = date(max(today.year - year_range, 1900), 1, 1)
    end = date(today.year + year_range, 12, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))


def format_date(d: date) -> str:
    return f"{MONTHS[d.month - 1]} {d.day}, {d.year}"


def ask_choice(prompt: str, valid: set[str]) -> str:
    while True:
        answer = input(prompt).strip().lower()
        if answer in valid:
            return answer
        print("  ⚠️  Invalid choice, please try again.")


def choose_level() -> int:
    print("\nChoose a difficulty:")
    for key, (label, _) in LEVELS.items():
        print(f"  {key}. {label}")
    return LEVELS[ask_choice("Select (1-3): ", set(LEVELS))][1]


def play_round(n: int, year_range: int) -> bool:
    d = random_date(year_range)
    print(f"\n--- Question {n}/{ROUNDS} ---")
    print(f"📅 What day of the week is {format_date(d)}?")
    for i, name in enumerate(DAYS, start=1):
        print(f"  {i}. {name}")

    guess = int(ask_choice("Your answer (1-7): ", {str(i) for i in range(1, 8)})) - 1
    correct = d.weekday()  # Monday = 0 ... Sunday = 6

    if guess == correct:
        print("✅ Correct!")
        return True
    print(f"❌ Wrong! It was a {DAYS[correct]}.")
    return False


def rank(score: int) -> str:
    if score == ROUNDS:
        return "🏆 Calendar master!"
    if score >= 7:
        return "🥈 Great job!"
    if score >= 4:
        return "🥉 Not bad!"
    return "📚 Keep practicing!"


def main() -> None:
    print("=" * 40)
    print("   🎮 Day of the Week Game")
    print("=" * 40)

    while True:
        year_range = choose_level()
        score = streak = best_streak = 0

        for n in range(1, ROUNDS + 1):
            if play_round(n, year_range):
                score += 1
                streak += 1
                best_streak = max(best_streak, streak)
            else:
                streak = 0

        print("\n" + "=" * 40)
        print(f"Final score: {score}/{ROUNDS}   |   Best streak: {best_streak}")
        print(rank(score))
        print("=" * 40)

        if ask_choice("\nPlay again? (y/n): ", {"y", "n"}) == "n":
            print("Thanks for playing! 👋")
            break


if __name__ == "__main__":
    main()
