from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
    return render(request, "chat/index.html")