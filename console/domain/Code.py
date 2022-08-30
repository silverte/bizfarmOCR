class Code:
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(Code, cls).__new__(cls)
    #     else:
    #         return cls.instance

    def __init__(self):
        self.code_name = None
        self.code_title = None
        self.code_list = {}

    def put(self, code_name: str, code_title: str, enum_obj):
        self.code_list[code_name] = (code_title, enum_obj)

    def get(self, name):
        json_list = {}
        for item in self.code_list[name][1]:
            json_list[item.key] = item.val
        return json_list

    def get_list(self):
        json_list = {}
        for key, value in self.code_list.items():
            json_list[key] = value[0]
        return json_list
