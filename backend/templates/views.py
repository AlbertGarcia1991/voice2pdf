import logging

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Template
from .serializers import TemplateSerializer

logger = logging.getLogger(__name__)

# Create your views here.


class TemplateCreateView(APIView):
    def post(self, request):
        try:
            serializer = TemplateSerializer(data=request.data)
            if not serializer.is_valid():
                logger.error(f"Validation error: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            obj = serializer.save()
            return Response({"template_id": obj.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception("Error creating template")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TemplateDetailView(APIView):
    def get(self, request, pk):
        try:
            template = get_object_or_404(Template, pk=pk)
            serializer = TemplateSerializer(template)
            return Response(serializer.data)
        except Template.DoesNotExist:
            return Response({"error": "Template not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("Error retrieving template")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
