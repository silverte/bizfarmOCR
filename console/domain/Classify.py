class Classify:
    @classmethod
    def run(cls, image_path):
        if '사업자등록증' in image_path:
            return 'D0001'
        elif '가족관계' in image_path:
            return 'D0002'
        elif '주민등록등본' in image_path:
            return 'D0003'
        elif '주민등록초본' in image_path:
            return 'D0004'
        else:
            return 'the others'
