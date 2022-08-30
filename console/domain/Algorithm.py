from abc import ABC, abstractmethod
from asgiref.sync import sync_to_async
from console.models import DocumentRuleValue, DocumentExtractResult
from console.domain.DocumentRuleTemplate import DocumentRuleTemplate


class Algorithm:
    OCR_Format = None

    def __init__(self):
        self.composite = DocumentRuleTemplate()

    def set_extract_items(self, review_id, document_id, ocr, image_id, review_document_id):
        self.composite.image_id = image_id
        self.composite.review_document_id = review_document_id
        self.composite.review_id = review_id

        print("set extract_items from OCR")

        # OCR
        self.composite.extract_items = ocr.extract_items(document_id, Algorithm.OCR_Format)
        print(self.composite.extract_items)

        # OCR 추출결과 저장
        DocumentExtractResult.objects.create(contract_document_id=self.composite.image_id,
                                             review_id=self.composite.review_id,
                                             extract_items=self.composite.extract_items
                                             )

    # @sync_to_async
    def set_rule_list(self, review_document_id):
        print("\nset rule_list from Database")
        temp_list = []

        # model
        # domain_rule = DocumentRule.objects.all().values().filter(document_id=self.document_type)
        rule_values = DocumentRuleValue.objects.filter(review_document_id=review_document_id).select_related('rule')

        for rule_value in rule_values:
            temp = {}
            temp['rule_id'] = rule_value.rule_id
            temp['rule_name'] = rule_value.rule.rule_name
            temp['rule_unit'] = rule_value.rule.rule_unit
            temp['rule_class'] = rule_value.rule.rule_class
            temp['rule_type'] = rule_value.rule.rule_type
            temp['rule_type_value'] = rule_value.rule.rule_type_value
            temp['value1'] = rule_value.value1
            temp['value2'] = rule_value.value2
            temp['value3'] = rule_value.value3
            temp['value4'] = rule_value.value4
            temp['value5'] = rule_value.value5
            temp_list.append(temp)

        self.composite.rule_list = temp_list
        for rule in self.composite.rule_list:
            print(rule)

    def get_instance(self):
        return self.composite
