from django.urls import path
from . import views

urlpatterns = [
    path('', views.UrunListCreateView.as_view(), name='urun-list-create'),
    path('<int:pk>/', views.UrunRetrieveUpdateDestroyView.as_view(), name='urun-detail'),
    path('suppliers/', views.SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', views.SupplierRetrieveUpdateDestroyView.as_view(), name='supplier-detail'),
]
