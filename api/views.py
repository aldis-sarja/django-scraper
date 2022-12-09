from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Article
from .serializers import ArticleSerializer


@api_view(['GET'])
def home(request):
    article = Article.objects.all()
    serializer = ArticleSerializer(article, many=True)
    return Response(serializer.data)
