from datetime import datetime, timedelta

users = [
    {"name": "John", "birthday": datetime(1998, 5, 12)},
    {"name": "Sarah", "birthday": datetime(2000, 5, 21)},
    {"name": "Michael", "birthday": datetime(1995, 5, 7)},
    {"name": "Emily", "birthday": datetime(1994, 5, 15)},
    {"name": "William", "birthday": datetime(1987, 5, 25)},
    {"name": "Olivia", "birthday": datetime(1999, 5, 3)},
    {"name": "Jacob", "birthday": datetime(1992, 5, 30)},
    {"name": "Matthew", "birthday": datetime(1991, 5, 9)},
    {"name": "Hannah", "birthday": datetime(2002, 5, 1)},
    {"name": "Victoria", "birthday": datetime(1993, 5, 5)},
    {"name": "Andrew", "birthday": datetime(1996, 5, 14)},
    {"name": "Sophia", "birthday": datetime(1998, 5, 22)},
    {"name": "David", "birthday": datetime(1997, 5, 1)},
    {"name": "Isabella", "birthday": datetime(1994, 5, 12)},
    {"name": "Benjamin", "birthday": datetime(2001, 5, 23)}
]

def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    today = datetime.today().date()
    current_weekday = today.weekday()

    # створюємо словник для кожного дня тижня
    birthdays_by_weekday = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: []
    }

    # Дадаємо користувачів у відповідний день тижня
    for user in users:
        birthday = user['birthday']
        if birthday.weekday() >= 5:
            birthday = birthday + timedelta(days=7 - birthday.weekday())
        birthdays_by_weekday[birthday.weekday()].append(user['name'])

    # Роздруковуємо дні народження по днях тижня
    for i in range(7):
        weekday = (current_weekday + i + 1) % 7
        weekday_name = datetime.strptime(f"2023-04-{3+weekday}", "%Y-%m-%d").strftime('%A')
        if birthdays_by_weekday[weekday]:
            print(f"{weekday_name}: {', '.join(birthdays_by_weekday[weekday])}")


if __name__ == '__main__':
    get_birthdays_per_week(users)











