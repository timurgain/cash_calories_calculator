import datetime as dt
from typing import Optional


DATE_FORMAT = '%d.%m.%Y'


class Record:
    """Contains and return info about cash or calories."""

    def __init__(self,
                 amount: int,
                 comment: str,
                 date: Optional[str] = None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.utcnow().date() + dt.timedelta(hours=3)
        else:
            user_moment = dt.datetime.strptime(date, DATE_FORMAT)
            self.date = user_moment.date()


class Calculator:
    """Contains the limit and methods for calculations."""

    def __init__(self, limit: int) -> None:
        self.records = []
        self.limit = limit

    def add_record(self, record: Record) -> None:
        """Adds record into the list of records."""
        self.records.append(record)

    def get_today_stats(self) -> int:
        """Returns sum for any one day in the past."""
        today_stats = 0
        today = dt.datetime.utcnow().date() + dt.timedelta(hours=3)
        today_stats = sum(record.amount for record in self.records
                          if record.date == today)
        return today_stats

    def get_week_stats(self):
        """Returns sum for last week."""
        week_stats = 0
        today = dt.datetime.utcnow().date() + dt.timedelta(hours=3)
        start_day = today - dt.timedelta(days=7)
        week_stats = sum(record.amount for record in self.records
                         if start_day <= record.date <= today)
        return week_stats

    def get_limit_remained(self):
        """Returns limit remained for today."""
        limit_remained = self.limit - self.get_today_stats()
        return limit_remained


class CaloriesCalculator(Calculator):
    """Counts the amount of calories eaten per day."""

    def get_calories_remained(self) -> str:
        """Counts the remaining calories."""
        calories_remained = self.get_limit_remained()
        if calories_remained > 0:
            msg = (f'Сегодня можно съесть что-нибудь ещё,'
                   f' но с общей калорийностью'
                   f' не более {calories_remained} кКал')
        if calories_remained <= 0:
            msg = 'Хватит есть!'
        return msg


class CashCalculator(Calculator):
    """Counts the amount of cash spent per day."""

    USD_RATE = 75.0
    EURO_RATE = 90.0
    RUB_RATE = 1

    def get_today_cash_remained(self, currency: str) -> str:
        """Counts the remaining cash."""

        try:
            cur_info = {'rub': ('руб', CashCalculator.RUB_RATE),
                        'usd': ('USD', CashCalculator.USD_RATE),
                        'eur': ('Euro', CashCalculator.EURO_RATE)}
            if currency not in cur_info:
                raise Exception(f'Inappropriate value: {currency}')
            cash_remained = self.get_limit_remained() / cur_info[currency][1]
            cash_remained = round(cash_remained, 2)
            if cash_remained > 0:
                return (f'На сегодня осталось '
                        f'{cash_remained} {cur_info[currency][0]}')
            elif cash_remained == 0:
                return 'Денег нет, держись'
            elif cash_remained < 0:
                cash_remained = abs(cash_remained)
                return (f'Денег нет, держись: твой долг'
                        f' - {cash_remained} {cur_info[currency][0]}')

        except Exception as err:
            print(err)
            exit(1)


# Tests
if __name__ == '__main__':
    print(__name__)
    calories_calculator = CaloriesCalculator(100)
    cash = CashCalculator(100)

    rec1 = Record(amount=30, comment='wow', date='20.10.2021')
    rec2 = Record(amount=25, comment='wow')
    rec3 = Record(amount=78, comment='wow')
    rec4 = Record(amount=333, comment='wow', date='13.10.2021')
    rec5 = Record(amount=95, comment='wow', date='01.10.2021')

    cash.add_record(rec1)
    cash.add_record(rec2)
    cash.add_record(rec3)
    cash.add_record(rec4)
    cash.add_record(rec5)

    print(cash.get_today_cash_remained('usd'))
    print(f'cash week {cash.get_week_stats()}')

    calories_calculator.add_record(rec1)
    calories_calculator.add_record(rec2)
    calories_calculator.add_record(rec3)
    calories_calculator.add_record(rec4)
    calories_calculator.add_record(rec5)

    print(f'colories week {calories_calculator.get_week_stats()}')
    print(f'colories today {calories_calculator.get_today_stats()}')
    print(f'colories today remaining '
          f'{calories_calculator.get_calories_remained()}')
