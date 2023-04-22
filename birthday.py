from datetime import date, timedelta

users = [
    {"name": "John", "birthday": date(1996, 4, 22)},
    {"name": "Sarah", "birthday": date(2000, 4, 26)},
    {"name": "Michael", "birthday": date(1995, 4, 29)},
    {"name": "Emily", "birthday": date(1994, 4, 30)},
    {"name": "William", "birthday": date(1987, 4, 25)},
    {"name": "Olivia", "birthday": date(1999, 4, 24)},
    {"name": "Jacob", "birthday": date(1991, 4, 28)},
    {"name": "Matthew", "birthday": date(1991, 4, 23)},
    {"name": "Hannah", "birthday": date(2002, 4, 27)},
    {"name": "Victoria", "birthday": date(1993, 4, 21)}
]

def get_birthdays_per_week(users):
    #  Отримуємо поточну дату
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    next_monday = monday + timedelta(days=7)

    # проходимо по списку і перевіряємо їх дні народження
    birthday_list = []
    for user in users:
        birthday = user["birthday"].replace(year=today.year)

        # якщо день народження вже пройшов цього року
        if birthday < today:
            birthday = user["birthday"].replace(year=today.year + 1)

        # якщо день народження випадає на поточний тиждень
        if monday <= birthday <= monday + timedelta(days=6):
            if birthday.weekday() >= 5:
                birthday_list.append({"name": user["name"], "birthday": next_monday})
            else:
                birthday_list.append({"name": user["name"], "birthday": birthday})

        # якщо день народження припадає на наступний тиждень і не в суботу / неділю
        elif next_monday <= birthday <= next_monday + timedelta(days=4):
            if birthday.weekday() < 5:
                birthday_list.append({"name": user["name"], "birthday": birthday})

    # сортуємо список по датах народження
    birthday_list.sort(key=lambda x: x["birthday"])

    # виводимо список імен по днях тижня
    for day in range(7):
        date_str = (monday + timedelta(days=day)).strftime("%A")
        names = [x["name"] for x in birthday_list if x["birthday"].weekday() == day]
        if names:
            print(f"{date_str}: {', '.join(names)}")

if __name__ == '__main__':
    get_birthdays_per_week(users)
