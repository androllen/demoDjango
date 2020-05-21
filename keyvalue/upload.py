from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from django.core.files import File
from django.core.files.storage import default_storage
from .models import KeyValue
from rest_framework import  status
from .serializers import KeyValueSerializer


class MultipleFilesUpload(APIView):
    """
    curl -X POST -H "Content-Type: multipart/form-data" -F "files=@"D:\Andro\Documents\Gridea\themes\simple\templates\archives.ejs"" -F "files=@"D:\Andro\Documents\Gridea\themes\simple\templates\tags.ejs"" http://127.0.0.1:8080/dicts/file/ -u admin:root
    """
    
    queryset = KeyValue.objects.all()
    serializer_class = KeyValueSerializer
    
    def post(self, request):
        files = dict(request.data.lists())['files']

        try:
            for file in files:
                myfile = File(file)
                default_storage.save(myfile.name, myfile)
        except Exception as e:
            print(e)
            raise ParseError("Could not process file")

        return Response({"status": "success"}, status=status.HTTP_200_OK)
