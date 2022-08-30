from console.domain.Builder import Builder
from console.domain.ReviewRuleTemplate import ReviewTemplate
from console.models import ReviewRuleValue
from console.domain.Legacy import Legacy
from console.models import DocumentExtractResult


class ReviewFactory:
    def __init__(self, contract_id, review_id):
        super().__init__()
        self.contract_id = contract_id
        self.review_id = review_id
        self.composite = ReviewTemplate()

    def build(self):
        self.composite.contract_id = self.contract_id

        # OCR 추출항목 세팅
        self.set_extract_items()

        # Legacy 비교항목 세팅
        self.set_compare_items()

        # 심사 Rule 목록 세팅
        self.set_rule_list()

        return self.composite

    def set_extract_items(self):
        ocr_result = list(DocumentExtractResult.objects.filter(review_id=self.review_id).values('extract_items'))
        self.composite.extract_items = ocr_result
        print('\n select from DocumentExtractResult')
        print(self.composite.extract_items)

    def set_compare_items(self):
        legacy = Legacy()
        self.composite.compare_items = legacy.get_compare_items(self.review_id)
        print('\n get compare_items from Legacy')
        print(self.composite.compare_items)

    def set_rule_list(self):
        temp_list = []

        # model
        rule_values = ReviewRuleValue.objects.filter(review_id=self.review_id).select_related('rule')

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

        print('\n select from ReviewRuleValue')
        for rule in self.composite.rule_list:
            print(rule)
