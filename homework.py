import datetime as dt
from typing import List, Optional

USD_RATE = 75
EURO_RATE = 90
today = dt.datetime.utcnow().date() + dt.timedelta(hours=3)


class Record:
    """Describtion."""

    def __init__(self,
                 amount: int,
                 comment: str,
                 date: Optional[str] = None) -> None:
        if amount > 0:
            self.amount = amount
        else:
            return print('Only use numbers grater then zero')
        self.comment = comment
        if date is None:
            self.date = today
        else:
            date_format = '%d.%m.%Y'
            user_moment = dt.datetime.strptime(date, date_format)
            self.date = user_moment.date()

    def get_record(self) -> List:
        record_data = []
        record_data.append(self.amount)
        record_data.append(self.comment)
        record_data.append(self.date)
        return record_data


class Calculator:
    """Describtion."""

    def __init__(self, limit: int) -> None:
        self.records = []
        if limit > 0:
            self.limit = limit
        else:
            return print('Only use numbers grater then zero')

    def add_record(self, record: Record) -> None:
        rec = record.get_record()
        self.records.append(rec)
        print(f'Записал {self.records}')

    def get_day_stats(self, minus_day_delta: Optional[int] = None) -> int:
        day_stats = 0
        if minus_day_delta is not None:
            day = today - dt.timedelta(days=minus_day_delta)
        else:
            day = today
        for rec in self.records:
            if rec[2] == day:
                day_stats = day_stats + rec[0]
        return day_stats

    def get_today_stats(self) -> int:
        today_stats = self.get_day_stats()
        return today_stats

    def get_week_stats(self) -> int:
        last_six = sum([self.get_day_stats(delta) for delta in range(1, 7)])
        week_stats = last_six + self.get_today_stats()
        return week_stats


class CaloriesCalculator(Calculator):
    """Describtion."""

    def get_calories_remained(self) -> str:
        calories_remained = self.limit - self.get_today_stats()
        if calories_remained > 0:
            return (f'Сегодня можно съесть что-нибудь ещё,'
                    f' но с общей калорийностью'
                    f' не более {calories_remained} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    """Describtion."""

    def get_today_cash_remained(currency: str) -> str:
        pass


calories_calculator = CaloriesCalculator(100)
rec1 = Record(amount=33, comment='wow', date='23.09.2013')
rec2 = Record(amount=25, comment='wow')
rec3 = Record(amount=10, comment='wow', date='12.10.2021')
rec4 = Record(amount=40, comment='wow', date='7.10.2021')
rec5 = Record(amount=89, comment='wow')
calories_calculator.add_record(rec1)
calories_calculator.add_record(rec2)
calories_calculator.add_record(rec3)
calories_calculator.add_record(rec4)
calories_calculator.add_record(rec5)
print(f'Week {calories_calculator.get_week_stats()}')
print(calories_calculator.get_calories_remained())
