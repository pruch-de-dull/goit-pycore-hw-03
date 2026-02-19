from datetime import datetime


def get_days_from_today(date: str) -> int | None:
  
    try:
        date_n = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print(f"Помилка: дата '{date}' не відповідає формату 'РРРР-ММ-ДД'.")
        return None
        
    now = datetime.now()
    difference = now - date_n
    return difference.days


if __name__ == "__main__":
    f = get_days_from_today('2020-09-10')
    print(f"Кількість днів: {f}")
