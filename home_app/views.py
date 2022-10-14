from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import testimony

# Create your views here.

def home_app(request):
    nav_pro = False
    testi = testimony.objects.all().order_by('-date_posted')[:3]

    context={'nav_pro':nav_pro, 'testi':testi}
    return render(request, 'home_app/main_home.html', context)

def profesional_bg(request):
    nav_pro = True
    context={'nav_pro':nav_pro}
    return render(request, 'home_app/professional_bg.html', context)

def testimonies(request):
    testi = testimony.objects.all().order_by('-date_posted')

    p = Paginator(testi, 5) # this is how the paginator is used
    page = request.GET.get('page') # this is how the page is got
    p_posts = p.get_page(page) #all works now with this variable

    context={'testi':testi, 'p_posts':p_posts}
    return render(request, 'home_app/testimonies.html', context)