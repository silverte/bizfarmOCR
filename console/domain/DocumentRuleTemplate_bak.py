from console.domain.Visitor import Visitable, Visitor


class DocumentRuleTemplate(Visitable):
    def __init__(self):
        self.extract_items = None
        self.compare_items = None
        self.rule_list = None

    def rule_check(self, visitor: Visitor) -> dict:
        return visitor.check(self)

        print("\nrule check {}".format(__class__))

        self.get_class()

        for idx, _ in enumerate(self.rule_list):
            self.rule_list[idx]['result'] = 'success'

        return self.rule_list

    def get_class(self):
        for rule in self.rule_list:
            rule_class = rule['rule_class']
            print(rule_class+" 객체생성 & Rule 체크 실행")

