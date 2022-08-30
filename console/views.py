import json

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.views.generic import(
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.models import EmailAddress
from allauth.account.views import PasswordChangeView, PasswordResetView
from console.models import Domain, User
from console.forms import DomainForm, ProfileForm
from console.functions import confirmation_required_redirect
import easyocr

reader = easyocr.Reader(['ko', 'en'], gpu=False, verbose=False)


# Create your views here.
def index(request):
    return render(request, 'console/index.html')


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self):
        return reverse('index')


class CustomPasswordResetView(PasswordResetView):
    def get_success_url(self):
        return reverse('account_reset_password_done')


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'console/profile.html'

    redirect_unauthenticated_users = True
    raise_exception = True

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('index')

    def test_func(self, user):
        db_user = self.get_object()
        return db_user.id == user.id


class DomainDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Domain
    pk_url_kwarg = 'domain_id'

    redirect_unauthenticated_users = False
    raise_exception = True

    def get_success_url(self):
        return reverse('domain-list')

    # get method 요청시 post method 를 바로 호출함
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def test_func(self, user):
        domain = self.get_object()
        return domain.user == user


class DashboardView(LoginRequiredMixin, ListView):
    model = Domain
    template_name = 'console/dashboard.html'


@login_required
def sync_domain_list(request):
    user_id = request.user.id
    domains = Domain.objects.filter(user__id=user_id)
    json_domains = []

    # converting 'QuerySet' to Dictionary
    for i in range(len(domains)):
        json_domains.append(domain_to_dictionary(domains[i]))

    print(json_domains)
    return HttpResponse(json.dumps(json_domains), content_type="application/json")


@login_required
def ocr_demo(request):
    if request.method == 'POST' and request.FILES.get('demo_file', False):
        myfile = request.FILES.get('demo_file', False)
        fs = FileSystemStorage(location='console/media/test_files', base_url='/uploads/test_files')
        # FileSystemStorage.save(file_name, file_content)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        text_result = reader.readtext('console/media/test_files/'+filename, detail=0)
        #json_result = reader.readtext('console/media/test_files/'+filename)

        context = {
            'uploaded_file_url': uploaded_file_url,
            'text_result': text_result,
            # 'json_result': json_result
        }

        return render(request, 'console/ocr_demo.html', context)
    return render(request, 'console/ocr_demo.html')


class DomainCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Domain
    form_class = DomainForm
    template_name = 'console/domain_list.html'

    redirect_unauthenticated_users = True
    raise_exception = confirmation_required_redirect

    def get_success_url(self):
        return reverse('domain-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self, user):
        return EmailAddress.objects.filter(user=user, verified=True).exists()


def domain_to_dictionary(domain):
    """
    A utility function to convert object of type Doamin to a Python Dictionary
    """
    output = {}
    output["id"] = domain.id
    output["domain_name"] = domain.domain_name
    output["domain_code"] = domain.domain_code
    output["ocr_type"] = domain.get_ocr_type_display()
    output["price_plan"] = domain.get_price_plan_display()
    output["domain_created"] = domain.domain_created.strftime("%Y/%m/%d, %H:%M:%S")
    output["domain_updated"] = domain.domain_updated.strftime("%Y/%m/%d, %H:%M:%S")
    output["user_id"] = domain.user_id

    return output


@login_required
def document_review(request):
    return render(request, 'console/review.html')


@login_required
def review_register(request):
    return render(request, 'console/rule.html')
