from django.shortcuts import render

# Create your views here.
def index(request):
    # add to context variable
    index_context = {}

    # Render template and pass the context variable
    return render(request, 'home/index.html', context=index_context)