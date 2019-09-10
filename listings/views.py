from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import price_choices, bedroom_choices,state_choices
# Create your views here.
def index(request):
    listings = listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)# show listings 3 per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
        'listings' : paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listingg(request,listingg_id):
    # pk = primary key and get_oject_404  class will produce notfound
    listingg = get_object_or_404(listing, pk = listingg_id)
    context = {
        'listingg': listingg
    }
    return render(request, 'listings/listingg.html',context)


def search(request):
    queryset_list = listing.objects.order_by('-list_date')
    #keywords
    if request.method == 'GET':
        keywords = request.GET.get('keywords')
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords) 
    #city
    if request.method == 'GET':
        city = request.GET.get('city')
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    #state
    if request.method == 'GET':
        state = request.GET.get('state')
        if state:
            queryset_list = queryset_list.filter(state__iexact=state) 
     #bedrooms
    if request.method == 'GET':
        bedrooms = request.GET.get('bedrooms')
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

     #price 
    if request.method == 'GET':
        price= request.GET.get('price')
        if price:
            queryset_list = queryset_list.filter(price__lte=price) 
    
    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings' : queryset_list,
        'values' : request.GET
    }
    return render(request, 'listings/search.html',context)