from django.shortcuts import render

# Create your views here.
def index(request):
    #this is your new views
    images = [
    {'click': "my.play()", 'source':"/images/my.jpg"},
    {'click': "please.play()", 'source':"/images/please.jpg"},
    {'click': "that.play()", 'source':"/images/that.jpg"},
    {'click': "and.play()", 'source':"/images/and.jpg"},
    {'click': "what.play()", 'source':"/images/what.jpg"},
    {'click': "a.play()", 'source':"/images/a.jpg"},
    {'click': "there.play()", 'source':"/images/there.jpg"},
    {'click': "i.play()", 'source':"/images/i.jpg"},
    {'click': "we.play()", 'source':"/images/we.jpg"},
    {'click': "are.play()", 'source':"/images/are.jpg"},
    {'click': "is.play()", 'source':"/images/is.jpg"},
    {'click': "were.play()", 'source':"/images/were.jpg"},
    {'click': "was.play()", 'source':"/images/was.jpg"},
    {'click': "you.play()", 'source':"/images/you.jpg"},
    {'click': "they.play()", 'source':"/images/they.jpg"},
    {'click': "play.play()", 'source':"/images/play.jpg"},
    {'click': "like.play()", 'source':"/images/like.jpg"},
    {'click': "work.play()", 'source':"/images/work.jpg"},
    {'click': "have.play()", 'source':"/images/have.jpg"},
    {'click': "feel.play()", 'source':"/images/feel.jpg"},
    {'click': "read.play()", 'source':"/images/read.jpg"},
    {'click': "more.play()", 'source':"/images/more.jpg"},
    {'click': "stop.play()", 'source':"/images/stop.jpg"},
    {'click': "it.play()", 'source':"/images/it.jpg"},
    {'click': "he.play()", 'source':"/images/he.jpg"},
    {'click': "want.play()", 'source':"/images/want.jpg"},
    {'click': "come.play()", 'source':"/images/come.jpg"},
    {'click': "go.play()", 'source':"/images/go.jpg"},
    {'click': "say.play()", 'source':"/images/say.jpg"},
    {'click': "color.play()", 'source':"/images/color.jpg"},
    {'click': "help.play()", 'source':"/images/help.jpg"},
    {'click': "she.play()", 'source':"/images/she.jpg"},
    {'click': "dont.play()", 'source':"/images/dont.jpg"},
    {'click': "eat.play()", 'source':"/images/eat.jpg"},
    {'click': "make.play()", 'source':"/images/make.jpg"},
    {'click': "need.play()", 'source':"/images/need.jpg"},
    {'click': "drink.play()", 'source':"/images/drink.jpg"},
    {'click': "turn.play()", 'source':"/images/turn.jpg"},
    {'click': "put.play()", 'source':"/images/put.jpg"}
    ]
    return render(request, 'index.html', {'images': images})

#TODO populate images dictionary with records from database via Model

#TODO add an upload view and corresponding template

#TODO allow user to choose which icon and voice sets to load
