from django.shortcuts import render

def list(request):
    return render(request, 'createpost/list.html')


def acc(request):
    return render(request, 'createpost/acc.html')



# Create your views here.
#
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse('Hello world!')
#
# def test(request):
#     return HttpResponse('TESTTTTT')