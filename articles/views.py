from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)  
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors,)
