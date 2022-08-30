from console.domain.Algorithm import Algorithm
from console.domain.DocumentRuleTemplate import DocumentRuleTemplate
from console.domain.OCR import IOCR


# class DocumentClass(Algorithm):
#     OCR_Format = {}
#
#     def __init__(self, ocr: IOCR):
#         super().__init__()
#         self.ocr = ocr
#         self.composite = DocumentRuleTemplate()
#
#     def set_extract_items(self, document_type):
#         print("\nset items {}".format(__class__))
#         print("set extract_items from OCR")
#
#         # OCR
#         self.composite.extract_items = self.ocr.extract_items(document_type, DocumentClass.OCR_Format)
#         for extract_item in self.composite.extract_items:
#             print(extract_item)


class BizRegistration(Algorithm):
    OCR_Format = {'register_num': '',  # 사업자등록번호
                  'name': '',  # 법인명(단체명)
                  'representative': '',  # 대표자
                  'opening_date': '',  # 개업년월일
                  'issued_date': '',  # 발급년월일
                  }


class FamilyRelation(Algorithm):
    OCR_Format = {'relation': '',  # 관계
                  'name': '',  # 이름
                  'birth_date': '',  # 생년월일
                  }


class HouseholdRegisterCopy(Algorithm):
    OCR_Format = {'relation': '',  # 관계
                  'name': '',  # 이름
                  'birth_date': '',  # 생년월일
                  }


class HouseholdRegisterAbstract(Algorithm):
    OCR_Format = {'relation': '',  # 관계
                  'name': '',  # 이름
                  'birth_date': '',  # 생년월일
                  }
