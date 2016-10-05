from wordbook.models import Word
from wordbook.serializers import WordSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def post(self, request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def put(self, request, pk, format=None):
        wordObj = Word.objects.get(pk=pk)
        serializer = WordSerializer(wordObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        wordObj = Word.objects.get(pk=pk)
        # 파일 경로에 있는 사진 제거
        wordObj.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
