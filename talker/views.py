from django.shortcuts import render

# Create your views here.
def index(request):
    #this is your new views
    return render(request, 'index.html')
