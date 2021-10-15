import datetime as dt
from typing import List, Optional


today = dt.datetime.utcnow().date() + dt.timedelta(hours=3)


class Record:
    """Contains and return info about cash or calories."""

    def __init__(self,
                 amount: int,
                 comment: str,
                 date: Optional[str] = None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = today
        else:
            date_format = '%d.%m.%Y'
            user_moment = dt.datetime.strptime(date, date_format)
            self.date = user_moment.date()

    def get_record(self) -> List:
        """Returns list of properties for one record."""
        record_data = []
        record_data.append(self.amount)
        record_data.append(self.comment)
        record_data.append(self.date)
        return record_data


class Calculator:
    """Contains the limit and methods for calculations."""

    def __init__(self, limit: int) -> None:
        self.records = []
        self.limit = limit

    def add_record(self, record: Record) -> None:
        """Adds record into the list of records."""
        self.records.append(record)

    def get_day_stats(self, minus_day_delta: Optional[int] = None) -> int:
        """Returns sum for any one day in the past."""
        day_stats = 0
        if minus_day_delta is not None:
            day = today - dt.timedelta(days=minus_day_delta)
        else:
            day = today
        for rec in self.records:
            rec = Record.get_record(rec)  # rec: list = [amount, comment, date]
            if rec[2] == day:
                day_stats = day_stats + rec[0]
        return day_stats

    def get_today_stats(self) -> int:
        """Returns sum for today."""
        today_stats = self.get_day_stats()
        return today_stats

    # 1й вариант - тест не принял, хотя значения на выходе те же
    # >>> буду рад, если скажете, что в этом решении не так <<<
    # def get_week_stats(self) -> int:
    #    last_six = sum([self.get_day_stats(delta) for delta in range(1, 7)])
    #    week_stats = last_six + self.get_today_stats()
    #    # week_stats = f'six days {last_six} + today {self.get_today_stats()}'
    #    return week_stats

    # 2й вариант get_week_stats - тест его принял
    def get_week_stats(self):
        """Returns sum for last week."""
        week_stats = 0
        start_day = today - dt.timedelta(days=7)
        for rec in self.records:
            rec = Record.get_record(rec)  # rec = [amount, comment, date]
            if start_day <= rec[2] <= today:
                week_stats = week_stats + rec[0]
        return week_stats


class CaloriesCalculator(Calculator):
    """Counts the amount of calories eaten per day."""

    def get_calories_remained(self) -> str:
        """Counts the remaining calories."""
        calories_remained = self.limit - self.get_today_stats()
        if calories_remained > 0:
            return (f'Сегодня можно съесть что-нибудь ещё,'
                    f' но с общей калорийностью'
                    f' не более {calories_remained} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    """Counts the amount of cash spent per day."""

    USD_RATE = 75.
    EURO_RATE = 90.0
    RUB_RATE = 1

    def get_today_cash_remained(self, currency: str) -> str:
        """Counts the remaining cash."""
        cur_info = {'rub': ['руб', CashCalculator.RUB_RATE],
                    'usd': ['USD', CashCalculator.USD_RATE],
                    'eur': ['Euro', CashCalculator.EURO_RATE]}
        cash_remained = self.limit - self.get_today_stats()
        cash_remained = cash_remained / cur_info[currency][1]
        cash_remained = round(cash_remained, 2)
        if cash_remained > 0:
            return (f'На сегодня осталось '
                    f'{cash_remained} {cur_info[currency][0]}')
        elif cash_remained == 0:
            return 'Денег нет, держись'
        else:
            cash_remained = abs(cash_remained)
            return (f'Денег нет, держись: твой долг'
                    f' - {cash_remained} {cur_info[currency][0]}')


calories_calculator = CaloriesCalculator(100)
cash = CashCalculator(100)

rec1 = Record(amount=30, comment='wow', date='20.10.2021')  # Будущее
rec2 = Record(amount=25, comment='wow')
rec3 = Record(amount=10, comment='wow', date='14.10.2021')  # Вчера
rec4 = Record(amount=333, comment='wow', date='13.10.2021')  # Позавчера
rec5 = Record(amount=95, comment='wow', date='01.10.2021')  # - Давно

cash.add_record(rec1)
cash.add_record(rec2)
cash.add_record(rec3)
cash.add_record(rec4)
cash.add_record(rec5)

print(cash.get_today_cash_remained('usd'))
print(f'week {cash.get_week_stats()}')

calories_calculator.add_record(rec1)
calories_calculator.add_record(rec2)
calories_calculator.add_record(rec3)
calories_calculator.add_record(rec4)
calories_calculator.add_record(rec5)

print(calories_calculator.get_week_stats())
print(calories_calculator.get_calories_remained())
