from django.test import TestCase
from console.functions import document_review
from console.models import Rule, Document, DocumentRuleValue, Company, Review, Contract, ContractDocument, ReviewDocument, ReviewRule, ReviewRuleValue

# Create your tests here.


class TestDocumentReview(TestCase):
    def setUp(self) -> None:
        Document.objects.create(name='D0001', category='PUBLIC', description='사업자등록증', document_class='BizRegistration')
        Document.objects.create(name='D0002', category='PUBLIC', description='가족관계증명서', document_class='FamilyRelation')
        Document.objects.create(name='D0003', category='PUBLIC', description='주민등록등본', document_class='HouseholdRegisterCopy')
        Document.objects.create(name='D0004', category='PUBLIC', description='주민등록초본', document_class='HouseholdRegisterAbstract')
        Rule.objects.create(rule_name='가족관계증명서 구성원 확인', rule_unit='REVIEW', rule_type='CODE', rule_type_value='Whether',
                            rule_class='FamilyMember')
        Rule.objects.create(rule_name='가족관계증명서 관계 확인', rule_unit='REVIEW', rule_type='CODE', rule_type_value='Whether',
                            rule_class='FamilyRelation')
        Rule.objects.create(rule_name='가족관계증명서 발급 기간 제한', rule_unit='DOCUMENT', rule_type='CODE', rule_type_value='Whether',
                            rule_class='FamilyRelIssuedPeriod')
        Rule.objects.create(rule_name='사업자등록증 진위확인', rule_unit='DOCUMENT', rule_type='CODE', rule_type_value='Whether',
                            rule_class='BizRegAuthenticity')
        Rule.objects.create(rule_name='사업자등록증 상태확인', rule_unit='DOCUMENT', rule_type='CODE', rule_type_value='Whether',
                            rule_class='BizRegStatus')
        Rule.objects.create(rule_name='사업자등록증 설립기간', rule_unit='DOCUMENT', rule_type='PERIOD', rule_class='BizRegOpeningPeriod')
        Rule.objects.create(rule_name='사업자등록증 발급기간', rule_unit='DOCUMENT', rule_type='PERIOD', rule_class='BizRegIssuedPeriod')
        Company.objects.create(name='에스케이텔레콤')
        Review.objects.create(review_name='결합상품 자동심사')
        Contract.objects.create(applicant_name='조경민', status='REGISTER', review_id='1')
        Contract.objects.create(applicant_name='김정현', status='REGISTER', review_id='1')
        ContractDocument.objects.create(contract_id='1', document_image='document_files/주민등록초본.png')
        ContractDocument.objects.create(contract_id='1', document_image='document_files/사업자등록증.jpeg')
        ContractDocument.objects.create(contract_id='2', document_image='document_files/가족관계증명서.png')
        ContractDocument.objects.create(contract_id='2', document_image='document_files/사업자등록증.jpeg')
        ReviewDocument.objects.create(review_id='1', document_id='D0002')
        ReviewDocument.objects.create(review_id='1', document_id='D0003')
        ReviewDocument.objects.create(review_id='1', document_id='D0004')
        DocumentRuleValue.objects.create(review_document_id='1', rule_id='3', value1='2',
                                         value2='02', value3='03')
        DocumentRuleValue.objects.create(review_document_id='2', rule_id='4', value1='01')
        DocumentRuleValue.objects.create(review_document_id='2', rule_id='5', value1='01')
        DocumentRuleValue.objects.create(review_document_id='2', rule_id='6', value1='3',
                                         value2='03', value3='03')
        DocumentRuleValue.objects.create(review_document_id='2', rule_id='7', value1='2',
                                         value2='02', value3='04')
        ReviewRule.objects.create(review_id='1', rule_id='1')
        ReviewRule.objects.create(review_id='1', rule_id='2')
        ReviewRuleValue.objects.create(review_id='1', rule_id='1', value1='01')
        ReviewRuleValue.objects.create(review_id='1', rule_id='2', value1='01')

    def test_document_review(self) -> None:
        document_review()

        # print("\n심사결과")
        # for result in results:
        #     print(result)
