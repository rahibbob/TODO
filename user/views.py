from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'user/index.html')
def user_signup(request):
    return render(request, 'user/signup.html')
def user_login(request):
    return render(request, 'user/login.html')

