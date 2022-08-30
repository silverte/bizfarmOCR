"""bizfarmOCR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from console.views import CustomPasswordChangeView, CustomPasswordResetView

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # OCR
    path('', include('console.urls')),
    # 이메일 인증요청 별도 페이지 적용
    path(
        'email-confirmation-required/',
        TemplateView.as_view(template_name='account/email_confirmation_required.html'),
        name='account_email_confirmation_required',
    ),
    # 이메엘 인증완료 별도 페이지 적용
    path(
        'eamil-confirmation-done/',
         TemplateView.as_view(template_name='console/email_confirmation_done.html'),
         name='account_email_confirmation_done'
    ),
    # allauth 에서 정의한 View 보다 먼저 호출함
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_password_change'),
    path('password/reset/', CustomPasswordResetView.as_view(), name='account_reset_password'),
    path('', include('allauth.urls')),
    #path('users/<int:user_id>/', views.ProfileView.as_view(), name='profile'),
]

# static 파일 경로 설정(DEBUG=True 일 때만)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)