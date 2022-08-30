from django.shortcuts import redirect
from allauth.account.utils import send_email_confirmation

from console.domain.BizRegistration import BizRegistration
from console.domain.FamilyRelation import FamilyRelation
from console.domain.Factory import Factory
from console.domain.Legacy import Legacy
from console.domain.OCR import OCR
from console.domain.CodeFactory import CodeFactory


def confirmation_required_redirect(self, request):
    send_email_confirmation(request, request.user)
    return redirect('account_email_confirmation_required')


def document_review(image_path: str) -> dict:
    # 문서유형
    functions = {
        'D0001': BizRegistration,
        'D0002': FamilyRelation,
                 }

    # 이미지 분류 객체 생성
    # document_type = Classify(image_path)
    document_type = 'D0001'

    # OCR 객체 생성
    ocr = OCR()
    # legacy 정보 객체 생성
    legacy = Legacy()
    # 공통코드 생성 - main 에서 실행
    code = CodeFactory.get_instance()
    print("공통코드 등록\n{}".format(code.get_list()))

    # 문서유형 알고리즘 생성
    func = functions[document_type]
    algorithm = func(ocr, legacy)

    # 빌더 객체 생성
    factory = Factory(document_type)
    # 알고리즘 세팅
    factory.set_algorithm(algorithm)

    # 생성 요청
    review = factory.build().get_instance()

    # 룰 체크
    result = review.rule_check()

    return result
