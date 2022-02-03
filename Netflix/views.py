from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'Index.html')

def Register(request):
    return render(request, 'Register.html')

def Login(request):
    return render(request, 'Login.html')