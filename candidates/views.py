from django.shortcuts import render

def home_candidate(request):
    return render(request, 'home_candidate.html', {'user_is_candidate': True})
