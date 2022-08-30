from enum import Enum


class Whether(Enum):
    YES = ('01', "예")
    NO = ('02', "아니오")

    def __init__(self, key, val):
        self.key = key
        self.val = val


class BizRegStatus(Enum):
    CONTINUE = ('01', "계속사업자")
    STOP = ('02', "휴업")
    CLOSE = ('03', "폐업")

    def __init__(self, key, val):
        self.key = key
        self.val = val


class PeriodUnit(Enum):
    DAY = ('01', "일")
    WEEK = ('02', "주")
    MONTH = ('03', "월")
    YEAR = ('04', "년")

    def __init__(self, key, val):
        self.key = key
        self.val = val


class Range(Enum):
    MORE_THAN = ('01', "초과")
    LESS_THAN = ('02', "미만")
    NOT_LESS_THAN = ('03', "이상")
    NOT_MORE_THAN = ('04', "이하")

    def __init__(self, key, val):
        self.key = key
        self.val = val
