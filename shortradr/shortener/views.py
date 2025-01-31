from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import URLShortener
from django.contrib.auth.models import User


def home(request):
    return render(request, 'shortener/home.html')

@login_required
def profile(request):
    user_urls = URLShortener.objects.filter(user=request.user)
    fname = request.user.first_name
    print("fname",fname)
    return render(request, 'shortener/profile.html', { 'fname': fname ,'user_urls': user_urls})


@login_required
def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('url')
        if original_url:
            try:
                # Try to create a new shortened URL
                shortened_obj = URLShortener.objects.create(
                    actual_url=original_url, 
                    user=request.user
                )
                short_url = f"{request.scheme}://{request.get_host()}/{shortened_obj.shortened_url}"
                return HttpResponse(f"Shortened URL: {short_url}")
            
            except IntegrityError:
                # If URL already exists for this user, retrieve the existing one
                existing_url = URLShortener.objects.get(
                    actual_url=original_url, 
                    user=request.user
                )
                short_url = f"{request.scheme}://{request.get_host()}/{existing_url.shortened_url}"
                return HttpResponse(f"URL already exists. Existing shortened URL: {short_url}")
    
    return HttpResponse("Invalid request", status=400)



def redirect_url(request, short_code):
    url_obj = get_object_or_404(URLShortener, shortened_url=short_code)
    url_obj.increment_clicks()
    return redirect(url_obj.actual_url)