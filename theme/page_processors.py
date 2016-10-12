from mezzanine.pages.page_processors import processor_for
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import PortfolioItem
from .models import HomePage


@processor_for(PortfolioItem)
def portfolioitem_processor(request, page):
    '''
    Adds a portfolio's portfolio items to the context
    '''
    portfolioitem = PortfolioItem.objects.published(
        for_user=request.user).prefetch_related(
        'categories', 'images').get(id=page.portfolioitem.id)
    return {'portfolioitem': portfolioitem}


@processor_for(HomePage)
def home_processor(request, page):
    items = PortfolioItem.objects.published(for_user=request.user).prefetch_related('categories')
    items = items.filter(featured=True)  # only keep featured ones.
    paginator = Paginator(items, 1)
    page_no = request.GET.get('page')
    try:
        items = paginator.page(page_no)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)
    return {'items': items}
