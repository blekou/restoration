from django.shortcuts import render

# Create your views here.
def index(request):
    datas = {

    }
    return render(request, "pages/index.html", datas)

def elements(request):
    datas = {

    }
    return render(request, "pages/elements.html", datas)

def generic(request):
    datas = {

    }
    return render(request, "pages/generic.html", datas)