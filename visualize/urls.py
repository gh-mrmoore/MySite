from django.urls import path
from . import views

"""Something for later consideration, but could the urlpatterns list be generated from multiple lists
   joined together to allow for better visibility between URLs in the same app?"""

app_name = 'visualize'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<str:state>', views.state_detail), 
    ]