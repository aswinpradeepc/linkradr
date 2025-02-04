from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import URLShortener
from django.contrib.auth.models import User
import json

def home(request):
    return render(request, 'shortener/home.html')

@login_required
def profile(request):
    user_urls = URLShortener.objects.filter(user=request.user).order_by('-id')
    fname = request.user.first_name
    latest_url_id = request.GET.get('latest_url_id')
    return render(request, 'shortener/profile.html', { 'fname': fname, 'user_urls': user_urls, 'latest_url_id': latest_url_id })

@login_required
def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('url')
        if original_url:
            try:
                shortened_obj = URLShortener.objects.create(
                    actual_url=original_url, 
                    user=request.user
                )
                return redirect(f'/profile/?latest_url_id={shortened_obj.id}')
            except IntegrityError:
                existing_url = URLShortener.objects.get(
                    actual_url=original_url, 
                    user=request.user
                )
                return redirect(f'/profile/?latest_url_id={existing_url.id}')
    return HttpResponse("Invalid request", status=400)

def redirect_url(request, short_code):
    url_obj = get_object_or_404(URLShortener, shortened_url=short_code)
    url_obj.increment_clicks()
    return redirect(url_obj.actual_url)

@login_required
def update_shortened_url(request, url_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_shortened_url = data.get('shortened_url')
            url_obj = get_object_or_404(URLShortener, id=url_id, user=request.user)
            url_obj.shortened_url = new_shortened_url
            url_obj.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)