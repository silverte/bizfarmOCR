from console.domain.Visitor import Visitor, Visitable


class DocumentRule(Visitor):
    def __init__(self):
        self.extract_items = None
        self.compare_items = None
        self.rule_list = None

    def check(self, visitable: Visitable) -> dict:
        self.extract_items = visitable.extract_items
        self.compare_items = visitable.compare_items
        self.rule_list = visitable.rule_list

        print("\nrule check {}".format(__class__))
        # print(self.extract_items)
        # print(self.compare_items)
        # print(self.rule_list)

        self.get_class()

        for idx, _ in enumerate(self.rule_list):
            self.rule_list[idx]['result'] = 'success'

        return self.rule_list

    def get_class(self):
        for rule in self.rule_list:
            rule_class = rule['rule_class']
            print(rule_class+" 객체생성 & Rule 체크 실행")
