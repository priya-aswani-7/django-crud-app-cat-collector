# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')

def conclusion(request):
    return render(request, 'conclusion.html')

# create a template conclusion.html and render it inside of conclusion function in views.py
# conclusion.html must extend base.html and display the following content in the body
# h1: This is the conclusion
# horizontal rule
# unordered list of three items: thank you, goodbye, see you again
