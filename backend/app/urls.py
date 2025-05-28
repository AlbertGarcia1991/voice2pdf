from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('upload/', views.PDFUploadView.as_view(), name='pdf_upload'),
] 