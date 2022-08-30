from abc import ABC, abstractmethod


class IOCR(ABC):
    @abstractmethod
    def extract_items(self, document_type, extract_items):
        pass


class OCR(IOCR):
    def extract_items(self, document_type, items):
        if document_type == 'D0001':
            extract_items = [{
                'name': '체크메이트',
                'representative': '최기형',
                'opening_date': '20220101',
                'issued_date': '20220608'
            }]
        elif document_type == 'D0002':
            extract_items = {'issued_date': '20220623',
                             'member': [{'relation': '본인',
                                         'name': '조경민',
                                         'birth_date': '780912'
                                         },
                                        {'relation': '배우자',
                                         'name': '김정현',
                                         'birth_date': '801112'
                                         }]
                             }
        elif document_type == 'D0003':
            extract_items = {'issued_date': '20220623',
                             'member': [{'relation': '본인',
                                         'name': '조경민',
                                         'birth_date': '780912'
                                         },
                                        {'relation': '배우자',
                                         'name': '김정현',
                                         'birth_date': '801112'
                                         }]
                             }
        elif document_type == 'D0004':
            extract_items = {'issued_date': '20220623',
                             'member': [{'relation': '본인',
                                         'name': '조경민',
                                         'birth_date': '780912'
                                         },
                                        {'relation': '배우자',
                                         'name': '김정현',
                                         'birth_date': '801112'
                                         }]
                             }
        return extract_items

