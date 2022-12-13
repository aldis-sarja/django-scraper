from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Article
from .serializers import ArticleSerializer
from django.core.paginator import Paginator


@api_view(['GET'])
def home(request):
    page_number = request.GET.get('page')
    rows_per_page = request.GET.get('rows-per-page')
    if rows_per_page == None:
        rows_per_page = 10
    paginator = Paginator(Article.objects.all(), rows_per_page)
    articles = paginator.get_page(page_number)

    serializer = ArticleSerializer(articles, many=True)
#    return Response(serializer.data)
    return Response({
        'total_pages': paginator.num_pages,
        'total_rows': paginator.count,
        'articles': serializer.data,
    })
