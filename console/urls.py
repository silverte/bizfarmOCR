from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('domains/', views.DomainCreateView.as_view(), name='domain-list'),
    path('review/', views.document_review, name='review'),
    path('rule/', views.review_register, name='rule'),
    path(
        'domains/<int:domain_id>/delete/',
        views.DomainDeleteView.as_view(),
        name='domain-delete'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('domains/sync/', views.sync_domain_list, name='domain-sync'),
    path('demo/', views.ocr_demo, name='ocr-demo'),
]