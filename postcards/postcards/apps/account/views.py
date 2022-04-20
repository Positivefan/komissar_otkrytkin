from django.shortcuts import render, redirect

def account_login(request):
    return redirect('accounts/login')


def account(request):
    return render(request, 'account/login.html')




# Create your views here.
#
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse('Hello world!')
#
# def test(request):
#     return HttpResponse('TESTTTTT')

