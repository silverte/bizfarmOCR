from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters


# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=False,
        validators=[validate_no_special_characters],
        error_messages={'unique': '이미 사용중인 닉네임입니다.'},
    )

    profile_pic = models.ImageField(
        default='default_profile_pic.jpg', upload_to='profile_pics'
    )

    intro = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.email


class Domain(models.Model):
    domain_name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        validators=[validate_no_special_characters],
        error_messages={'unique': '이미 사용중인 도메인명 입니다.'},
    )
    domain_code = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        validators=[validate_no_special_characters],
        error_messages={'unique': '이미 사용중인 도메인코드 입니다.'},
    )

    OCR_TYPE = [
        ('01', 'Document'),
        ('02', 'Template'),
    ]
    ocr_type = models.CharField(max_length=2, choices=OCR_TYPE, null=False, default=None)

    PRICE_PLAN = [
        ('01', 'Basic'),
        ('02', 'Pro'),
        ('03', 'Enterprise')
    ]
    price_plan = models.CharField(max_length=2, choices=PRICE_PLAN, null=False, default=None)
    domain_created = models.DateTimeField(auto_now_add=True)
    domain_updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.domain_name


class Document(models.Model):
    DOCUMENT_CD = [
        ('D0001', '사업자등록증'),
        ('D0002', '가족관계증명서'),
        ('D0003', '주민등록등본'),
        ('D0004', '주민등록초본'),
    ]

    name = models.CharField(max_length=10,
                            primary_key=True,
                            null=False,
                            choices=DOCUMENT_CD,
                            unique=True,
                            error_messages={'unique': '이미 등록된 서류입니다.'},
                            default=None)

    DOCUMENT_CATEGORY = [
        ('PUBLIC', '공공정보'),
        ('APPLICATION', '신청서'),
    ]

    category = models.CharField(max_length=30,
                                null=False,
                                choices=DOCUMENT_CATEGORY,
                                default=None)

    description = models.TextField()
    document_class = models.CharField(max_length=50,
                                      null=True)


class Rule(models.Model):
    rule_name = models.CharField(max_length=30,
                                 null=False,
                                 unique=True,
                                 error_messages={'unique': '이미 등록된 규칙입니다.'},)

    RULE_UNIT = [
        ('REVIEW', '심사'),
        ('DOCUMENT', '서류'),
    ]
    rule_unit = models.CharField(max_length=10,
                                 null=False,
                                 choices=RULE_UNIT,
                                 default='REVIEW')

    RULE_TYPE = [
        ('PERIOD', '기간'),
        ('CODE', '코드'),
    ]

    rule_type = models.CharField(max_length=10,
                                 null=False,
                                 choices=RULE_TYPE,
                                 default=None)

    rule_type_value = models.CharField(max_length=50,
                                       null=True,
                                       blank=True)

    rule_class = models.CharField(max_length=30,
                                  null=False,)


class Company(models.Model):
    name = models.CharField(max_length=100,
                            null=False,
                            unique=True,
                            error_messages={'unique': '이미 등록된 회사입니다.'},
                            )


class Review(models.Model):
    review_name = models.CharField(max_length=100, null=False)


class Contract(models.Model):
    applicant_name = models.CharField(max_length=50)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    STATUS = [
        ('REGISTER', '등록'),
        ('PROCESSING', '처리중'),
        ('COMPLETE', '완료')
    ]
    status = models.CharField(max_length=10,
                              null=False,
                              choices=STATUS,
                              default='REGISTER')
    contract_created = models.DateTimeField(auto_now_add=True)
    contract_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.applicant_name


class ContractDocument(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    document_image = models.ImageField(upload_to='document_files')


class ReviewDocument(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)


class DocumentExtractResult(models.Model):
    contract_document = models.ForeignKey(ContractDocument, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    extract_items = models.TextField()


class DocumentRuleValue(models.Model):
    review_document = models.ForeignKey(ReviewDocument, on_delete=models.CASCADE)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    value1 = models.CharField(max_length=100, null=True, blank=True)
    value2 = models.CharField(max_length=100, null=True, blank=True)
    value3 = models.CharField(max_length=100, null=True, blank=True)
    value4 = models.CharField(max_length=100, null=True, blank=True)
    value5 = models.CharField(max_length=100, null=True, blank=True)


class DocumentRuleResult(models.Model):
    contract_document = models.ForeignKey(ContractDocument, on_delete=models.CASCADE)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    RESULT = [
        ('SUCCESS', '성공'),
        ('FAILURE', '실패'),
    ]
    result = models.CharField(max_length=10,
                              null=False,
                              choices=RESULT,
                              default='FAILURE')
    message = models.TextField(null=True)


class ReviewRule(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)


class ReviewRuleValue(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    value1 = models.CharField(max_length=100, null=True, blank=True)
    value2 = models.CharField(max_length=100, null=True, blank=True)
    value3 = models.CharField(max_length=100, null=True, blank=True)
    value4 = models.CharField(max_length=100, null=True, blank=True)
    value5 = models.CharField(max_length=100, null=True, blank=True)


class ReviewRuleResult(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    RESULT = [
        ('SUCCESS', '성공'),
        ('FAILURE', '실패'),
    ]
    result = models.CharField(max_length=10,
                              null=False,
                              choices=RESULT,
                              default='FAILURE')
    message = models.TextField(null=True)
