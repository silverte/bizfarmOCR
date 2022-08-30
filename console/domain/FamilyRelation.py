from console.domain.Algorithm import Algorithm
from console.domain.DocumentRuleTemplate import DocumentRuleTemplate
from console.domain.OCR import IOCR
from console.domain.Legacy import ILegacy


class FamilyRelation(Algorithm):
    OCR_format = [{'relation': '',  # 관계
                   'name': '',  # 이름
                   'birth_date': '',  # 생년월일
                   }, ]
    Legacy_Format = [{'relation': '',  # 관계
                      'name': '',  # 이름
                      'birth_date': '',  # 생년월일
                      }, ]

    def __init__(self, ocr: IOCR):
        super().__init__()
        self.ocr = ocr
        self.composite = DocumentRuleTemplate()

    def set_extract_items(self, document_type):
        print("\nset items {}".format(__class__))
        print("set extract_items from OCR")

        # OCR
        self.composite.extract_items = self.ocr.extract_items(document_type, FamilyRelation.OCR_format)
        for extract_item in self.composite.extract_items:
            print(extract_item)
