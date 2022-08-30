from console.domain.Code import Code
from console.domain.Enums import Whether, Range, PeriodUnit, BizRegStatus


class CodeFactory:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Code()
            cls.__instance.put("Whether", "여부", Whether)
            cls.__instance.put("Range", "범위", Range)
            cls.__instance.put("PeriodUnit", "기간단위", PeriodUnit)
            cls.__instance.put("BizRegStatus", "사업자등록상태", BizRegStatus)
        else:
            pass
        return cls.__instance
