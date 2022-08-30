from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from console.models import (User,
                            Domain,
                            Document,
                            Rule,
                            DocumentRuleValue,
                            Company,
                            Contract,
                            ContractDocument,
                            Review,
                            ReviewDocument,
                            DocumentExtractResult,
                            DocumentRuleResult,
                            ReviewRule,
                            ReviewRuleValue,
                            ReviewRuleResult,
                            )

# Register your models here.
admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname",)}),)

admin.site.register(Domain)
admin.site.register(Document)
admin.site.register(Rule)
admin.site.register(DocumentRuleValue)
admin.site.register(Company)
admin.site.register(Contract)
admin.site.register(ContractDocument)
admin.site.register(Review)
admin.site.register(ReviewDocument)
admin.site.register(DocumentExtractResult)
admin.site.register(DocumentRuleResult)
admin.site.register(ReviewRule)
admin.site.register(ReviewRuleValue)
admin.site.register(ReviewRuleResult)
