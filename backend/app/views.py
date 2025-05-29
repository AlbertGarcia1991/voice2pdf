from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from django.conf import settings
import uuid
import os
from .serializers import PDFUploadSerializer, UploadSerializer
from rest_framework import status

@api_view(['GET'])
def health_check(request):
    return Response({'status': 'healthy'})

@api_view(['POST'])
def upload_file(request):
    serializer = UploadSerializer(data=request.data)
    if serializer.is_valid():
        # Process the file here
        return Response({'message': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PDFUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = PDFUploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        file = serializer.validated_data['file']
        upload_id = str(uuid.uuid4())
        filename = f"{upload_id}.pdf"
        filepath = os.path.join(settings.PDF_TMP_DIR, filename)

        # Save the file
        with open(filepath, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return Response({
            "upload_id": upload_id,
            "pages": []
        }) 