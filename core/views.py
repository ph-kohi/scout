from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def register_candidate(request):
    return render(request, 'register_candidate.html', {'hide_nav_links': True})