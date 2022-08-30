import asyncio
from asgiref.sync import sync_to_async
from console.domain.Builder import Builder


class DocumentFactory(Builder):
    def __init__(self, review_id, document_id, ocr, image_id, review_document_id, algorithm=None):
        super().__init__()
        self.document_id = document_id
        self.ocr = ocr
        self.image_id = image_id
        self.review_document_id = review_document_id
        self.review_id = review_id

        # Factory 생성자에 algorithm 세팅했을 경우 의존성 주입
        if algorithm:
            self.algorithm = algorithm

    # async def async_build(self):
    #     # 이벤트 루프가 함수호출을 알아서 스케줄하여 비동기로 호출할 수 있도록 asyncio.wait 사용
    #     await asyncio.wait([
    #         # OCR 추출항목 세팅
    #         self.algorithm.set_extract_items(self.document_type),
    #
    #         # self.algorithm.set_rule_list(self.document_type),
    #     ])

    def build(self):
        # 이벤트 루프 생성
        # asyncio.run(self.async_build())

        # OCR 추출항목 세팅
        self.algorithm.set_extract_items(self.review_id, self.document_id, self.ocr, self.image_id, self.review_id)

        # 심사 Rule 목록 세팅
        self.algorithm.set_rule_list(self.review_document_id)

        return self


