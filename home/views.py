from django.shortcuts import render
from visualize.other import my_weather

# Create your views here.
def index(request):
    index_context = {}  # add to context variable

    index_context['current_weather'] = my_weather()

    # Render template and pass the context variable
    return render(request, 'home/index.html', context=index_context)