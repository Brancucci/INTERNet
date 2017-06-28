from django.shortcuts import render


def index(request):
    """ Main page for user that allows user to select activity for redirection"""
    return render(request, 'INTERNetApp/index.html')


def events(request):
    return render(request, 'INTERNetApp/events.html')


def intern101(request):
    return render(request, 'INTERNetApp/intern101')


