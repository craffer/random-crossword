import random
import datetime

# the first crossword puzzle in the archives is November 21, 1993
NYT_ARCHIVE_START = datetime.date(1993, 11, 21)
TODAYS_DATE = datetime.date.today()
WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def random_date_helper(start_date, end_date):
    delta = end_date - start_date
    random_day = random.randrange(delta.days)
    return start_date + datetime.timedelta(days=random_day)


def random_date(start_date, end_date, weekday=None):
    while True:
        date = random_date_helper(start_date, end_date)
        # generate a new date if until we get the one we're looking for if one is specified
        if weekday == None or date.weekday() == weekday:
            return date


def date_to_nyt_url(date):
    return f"https://www.nytimes.com/crosswords/game/daily/{date.year}/{date.month}/{date.day}"


def output_options():
    print("Select a weekday:\n")
    for i, day in enumerate(WEEKDAYS):
        print(f"{i}: {day}")
    print("7: no preference")


def output_puzzle(date):
    print(f"\nGenerated a link to a random {WEEKDAYS[date.weekday()]} puzzle:")
    print(date_to_nyt_url(date))


def run_generator():
    puzzle_date = None
    while not puzzle_date:
        output_options()
        user_choice = input("\nYour choice: ")
        if user_choice.isdigit() and 0 <= int(user_choice) <= 7:
            puzzle_date = random_date(
                NYT_ARCHIVE_START,
                TODAYS_DATE,
                None if int(user_choice) == 7 else int(user_choice),
            )
            output_puzzle(puzzle_date)
        else:
            print(
                "\nYou must enter an integer between 0 and 7 (inclusive). Try again.\n"
            )


def main():
    run_generator()


if __name__ == "__main__":
    main()
