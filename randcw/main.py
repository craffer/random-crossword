import random
import datetime

# the first crossword puzzle in the archives is November 21, 1993
NYT_ARCHIVE_START = datetime.date(1993, 11, 21)
TODAYS_DATE = datetime.date.today()


def random_date(start_date, end_date):
    delta = end_date - start_date
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start_date + datetime.timedelta(seconds=random_second)


def random_weekday(start_date, end_date, weekday):
    while True:
        date = random_date(start_date, end_date)
        if date.weekday() == weekday:
            return date


def date_to_nyt_url(date):
    return f"https://www.nytimes.com/crosswords/game/daily/{date.year}/{date.month}/{date.day}"


def main():
    print("Generated a random Monday puzzle:")
    print(date_to_nyt_url(random_weekday(NYT_ARCHIVE_START, TODAYS_DATE, 0)))


if __name__ == "__main__":
    main()
