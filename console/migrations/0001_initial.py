# Generated by Django 4.0.4 on 2022-06-23 02:48

import console.validators
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(error_messages={'unique': '이미 사용중인 닉네임입니다.'}, max_length=15, unique=True, validators=[console.validators.validate_no_special_characters])),
                ('profile_pic', models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics')),
                ('intro', models.CharField(blank=True, max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': '이미 등록된 회사입니다.'}, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('REGISTER', '등록'), ('PROCESSING', '처리중'), ('COMPLETE', '완료')], default='REGISTER', max_length=10)),
                ('contract_created', models.DateTimeField(auto_now_add=True)),
                ('contract_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContractDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_image', models.ImageField(upload_to='document_files')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('name', models.CharField(choices=[('D0001', '사업자등록증'), ('D0002', '가족관계증명서'), ('D0003', '주민등록등본'), ('D0004', '주민등록초본')], default=None, error_messages={'unique': '이미 등록된 서류입니다.'}, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('category', models.CharField(choices=[('PUBLIC', '공공정보'), ('APPLICATION', '신청서')], default=None, max_length=30)),
                ('description', models.TextField()),
                ('document_class', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.document')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.review')),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(error_messages={'unique': '이미 사용중인 도메인명 입니다.'}, max_length=30, unique=True, validators=[console.validators.validate_no_special_characters])),
                ('domain_code', models.CharField(error_messages={'unique': '이미 사용중인 도메인코드 입니다.'}, max_length=30, unique=True, validators=[console.validators.validate_no_special_characters])),
                ('ocr_type', models.CharField(choices=[('01', 'Document'), ('02', 'Template')], default=None, max_length=2)),
                ('price_plan', models.CharField(choices=[('01', 'Basic'), ('02', 'Pro'), ('03', 'Enterprise')], default=None, max_length=2)),
                ('domain_created', models.DateTimeField(auto_now_add=True)),
                ('domain_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentExtractResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extract_items', models.TextField()),
                ('contract_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.contractdocument')),
                ('review_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.reviewdocument')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.review'),
        ),
    ]