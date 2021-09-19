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


def date_to_nyt_url(date):
    return f"https://www.nytimes.com/crosswords/game/daily/{date.year}/{date.month}/{date.day}"


def main():
    print("Generated a random puzzle:")
    print(date_to_nyt_url(random_date(NYT_ARCHIVE_START, TODAYS_DATE)))


if __name__ == "__main__":
    main()
