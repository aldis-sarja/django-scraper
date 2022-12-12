from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Article
from .serializers import ArticleSerializer
from django.core.paginator import Paginator


@api_view(['GET'])
def home(request):
    paginator = Paginator(Article.objects.all(), 10)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    serializer = ArticleSerializer(articles, many=True)
    return Response({
        'total_pages': paginator.num_pages,
        'articles': serializer.data,
    })
