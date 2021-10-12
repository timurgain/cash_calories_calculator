import datetime as dt
from typing import List, Optional


class Record:
    """Describtion."""

    def __init__(self, amount: int, comment: str, date: Optional[str] = None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.utcnow() + dt.timedelta(hours=3)
        else:
            date_format = '%d.%m.%Y'
            user_moment = dt.datetime.strptime(date, date_format)
            self.date = user_moment.date()

    def get_record(self) -> List:
        record_data = [self.amount, self.comment, self.date]
        return record_data


class Calculator:
    """Describtion."""

    def __init__(self, limit: int) -> None:
        self.limit = limit

    def add_record(record: Record):
        records = []
        rec = record.get_record
        records = records.append[rec]
        return records

    def get_today_stats():
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
