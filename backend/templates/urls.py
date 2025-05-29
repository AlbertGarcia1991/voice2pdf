from django.urls import path

from .views import TemplateCreateView, TemplateDetailView

app_name = "templates"

urlpatterns = [
    path("templates/", TemplateCreateView.as_view(), name="template-create"),
    path("templates/<int:pk>/", TemplateDetailView.as_view(), name="template-detail"),
]
