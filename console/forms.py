from django import forms
from .models import User, Domain


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]

    def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.save()


class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = [
            'domain_name',
            'domain_code',
            'ocr_type',
            'price_plan',
        ]
        widgets = {
            'ocr_type': forms.RadioSelect,
            'price_plan': forms.RadioSelect
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'nickname',
            'profile_pic',
            'username',
            'intro',
        ]