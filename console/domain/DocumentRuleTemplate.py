import asyncio
from console.domain.Visitor import Visitable
from console.domain.DocumentRules import *
from console.models import DocumentRuleResult


class DocumentRuleTemplate(Visitable):
    def __init__(self):
        self.extract_items = None
        self.compare_items = None
        self.rule_list = None
        self.image_id = None
        self.review_document_id = None
        self.review_id = None

    def rule_check(self):
        print("\nrule check {}".format(__class__))

        if self.rule_list:
            # 리플렉션을 활용하여 등록된 클래스를 동적호출(방문자 패턴으로 실제로직은 해당 클래스에 구현)
            for idx, rule in enumerate(self.rule_list):
                # 클래스 세팅
                my_class = globals()[rule['rule_class']]
                # 객체 생성
                my_inst = my_class(idx)
                # 메소드 세팅
                func = getattr(my_inst, 'check')
                # 메소드 호출
                func(self)

            # 심사결과 등록
            for result in self.rule_list:
                DocumentRuleResult.objects.create(contract_document_id=self.image_id,
                                                  rule_id=result['rule_id'],
                                                  result=result['result'],
                                                  message=result['message'],
                                                  )

        return self.rule_list
