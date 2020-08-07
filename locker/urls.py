from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.AccountListView.as_view(), name='account-list'),
    path('<int:pk>/', views.AccountDetailView.as_view(), name='account-detail'),
    path('create/', views.AccountCreate.as_view(), name='account-create'),
    path('<int:pk>/update/', views.AccountUpdate.as_view(), name='account-update'),
    path('<int:pk>/delete/', views.AccountDelete.as_view(), name='account-delete'),
]
