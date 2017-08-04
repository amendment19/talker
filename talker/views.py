from django.shortcuts import render

# Create your views here.
def index(request):
    #this is your new views
    images = [{'click': "help.play()", 'source':"/images/help.jpg"}, {'click': "come.play()", 'source':"/images/come.jpg"}]
    return render(request, 'index.html', {'images': images})
