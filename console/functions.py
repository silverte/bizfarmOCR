from django.shortcuts import redirect
from allauth.account.utils import send_email_confirmation

from console.domain.DocumentClasses import *
from console.domain.DocumentFactory import DocumentFactory
from console.domain.ReviewFactory import ReviewFactory
from console.domain.Legacy import Legacy
from console.domain.OCR import OCR
from console.domain.CodeFactory import CodeFactory
from console.domain.Classify import Classify
from console.models import Contract, ReviewDocument


def confirmation_required_redirect(self, request):
    send_email_confirmation(request, request.user)
    return redirect('account_email_confirmation_required')


def document_review():
    # OCR 객체 생성
    ocr = OCR()

    # legacy 정보 객체 생성
    legacy = Legacy()

    # 공통코드 생성 - main 에서 실행
    code = CodeFactory.get_instance()
    print("공통코드 등록\n{}".format(code.get_list()))

    # 가장 최근에 등록된 계약ID 조회
    contract = Contract.objects.filter(status='REGISTER').order_by('-contract_created').first()

    # 계약ID, 심사ID 저장
    contract_id = contract.id
    review_id = contract.review_id
    review_name = contract.review.review_name
    print("\ncontract[{}/{}], review[{}/{}]".format(contract_id, contract, review_id, review_name))

    # 계약ID에 첨부된 이미지 리스트 조회
    images = list(contract.contractdocument_set.all().values())

    # 첨부 서류 체크
    for image in images:
        print("\n첨부 이미지 ", image)

        # 서류 분류
        document_id = Classify.run(image['document_image'])
        print(document_id)

        # 심사ID에 정의된 첨부서류 확인
        review_document = ReviewDocument.objects.filter(review_id=review_id, document_id=document_id) \
            .select_related('document').first()

        # 심사ID에 유효한 서류인 경우
        if review_document:
            # review_document key 저장
            review_document_id = review_document.id
            print('review_document_id[{}], document_class[{}]'.format(review_document_id,
                                                                      review_document.document.document_class))

            # 문서유형 알고리즘 생성
            my_class = globals()[review_document.document.document_class]
            algorithm = my_class()

            # 빌더 객체 생성
            factory = DocumentFactory(review_id, document_id, ocr, image['id'], review_document_id)
            # 알고리즘 세팅
            factory.set_algorithm(algorithm)

            # 서류 Rule 객체 생성
            document = factory.build().get_instance()

            # 룰 체크
            result = document.rule_check()
            print(result)

        else:
            print('{} 유효한 서류가 아닙니다.'.format(review_name))
            break

    # 심사 Rule 객체 생성
    factory = ReviewFactory(contract_id, review_id)

    # 심사 Rule 빌더 호출
    review = factory.build()

    # 룰 체크
    result = review.rule_check()
    print(result)
