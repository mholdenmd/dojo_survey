from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
def index(request):
    print("************")
    print(request.method)
    print("************")
    # return HttpResponse("Hello Mark")
    return render(request, 'mark.html')

def result(request):
    print("************")
    print(request.POST)
    print("************")
    # return HttpResponse("thank you for submitting your form.")
    context = {
        'forminfo': request.POST
    }

    return render(request, "orderdetails.html", context)

# def details(request):
#     print("In the details function reqeust")