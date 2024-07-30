from django.shortcuts import render

def index(request):
    return render(request, 'flappybird_app/index.html')