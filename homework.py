import datetime as dt
from typing import List, Optional


class Record:
    """Describtion."""

    def __init__(self,
                 amount: int,
                 comment: str,
                 date: Optional[str] = None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.utcnow().date() + dt.timedelta(hours=3)
        else:
            date_format = '%d.%m.%Y'
            user_moment = dt.datetime.strptime(date, date_format)
            self.date = user_moment.date()
        print(self.date)

    def get_record(self) -> List:
        record_data = [self.amount, self.comment, self.date]
        return record_data


class Calculator:
    """Describtion."""

    def __init__(self, limit: int) -> None:
        self.records = []
        self.limit = limit

    def add_record(self, record: Record):
        rec = record.get_record
        self.records.append(rec)

    def get_today_stats(self):
        pass


class CaloriesCalculator(Calculator):
    """Describtion."""

    def __init__(self, limit: int) -> None:
        super().__init__(limit)
    pass


class CashCalculator(Calculator):
    """Describtion."""

    def __init__(self, limit: int) -> None:
        super().__init__(self, limit)
    pass


rec1 = Record(33, 'wow')
r = rec1.get_record
print('done')
