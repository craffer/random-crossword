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


def random_date(start_date, end_date):
    delta = end_date - start_date
    random_day = random.randrange(delta.days)
    return start_date + datetime.timedelta(days=random_day)


def random_weekday(start_date, end_date, weekday):
    while True:
        date = random_date(start_date, end_date)
        if date.weekday() == weekday:
            return date


def date_to_nyt_url(date):
    return f"https://www.nytimes.com/crosswords/game/daily/{date.year}/{date.month}/{date.day}"


def run_generator():
    generated = False
    while not generated:
        print("Select a weekday:\n")
        for i, day in enumerate(WEEKDAYS):
            print(f"{i}: {day}")

        user_choice = input("\nYour choice: ")
        if user_choice.isdigit() and 0 <= int(user_choice) < 7:
            user_choice_int = int(user_choice)
            print(f"\nGenerated a link to a random {WEEKDAYS[user_choice_int]} puzzle:")
            print(
                date_to_nyt_url(
                    random_weekday(NYT_ARCHIVE_START, TODAYS_DATE, user_choice_int)
                )
            )
            generated = True
        else:
            print(
                "\nYou must enter an integer between 0 and 6 (inclusive). Try again.\n"
            )


def main():
    run_generator()


if __name__ == "__main__":
    main()
