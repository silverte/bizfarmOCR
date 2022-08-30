from abc import ABC, abstractmethod


class ILegacy(ABC):
    @abstractmethod
    def get_compare_items(self, review_id):
        pass


class Legacy(ILegacy):
    def get_compare_items(self, review_id):
        compare_items = None
        # 결합상품 자동심사
        if review_id == 1:
            compare_items = [{'relation': '본인',
                              'name': '조경민',
                              'birth_date': '780912'
                              },
                             {'relation': '배우자',
                              'name': '김정현',
                              'birth_date': '801112'
                              }]
        return compare_items
