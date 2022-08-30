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


class DocumentRule(models.Model):
    rule_name = models.CharField(max_length=30,
                                 null=False,
                                 unique=True,
                                 error_messages={'unique': '이미 등록된 규칙입니다.'},)

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

    document = models.ForeignKey(Document, on_delete=models.CASCADE)


class Company(models.Model):
    name = models.CharField(max_length=100,
                            null=False,
                            unique=True,
                            error_messages={'unique': '이미 등록된 회사입니다.'},
                            )


class DocumentRuleValue(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    document_rule = models.ForeignKey(DocumentRule, on_delete=models.CASCADE)
    value1 = models.CharField(max_length=100, null=True, blank=True)
    value2 = models.CharField(max_length=100, null=True, blank=True)
    value3 = models.CharField(max_length=100, null=True, blank=True)
    value4 = models.CharField(max_length=100, null=True, blank=True)
    value5 = models.CharField(max_length=100, null=True, blank=True)


class Review(models.Model):
    review_name = models.CharField(max_length=100, null=False)


class Contract(models.Model):
    applicant_name = models.CharField(max_length=50)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)


class ContractDocument(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    document_image = models.ImageField(upload_to='document_files')

