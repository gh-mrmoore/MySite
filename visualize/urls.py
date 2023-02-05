from django.urls import path
from . import views

"""Something for later consideration, but could the urlpatterns list be generated from multiple lists
   joined together to allow for better visibility between URLs in the same app?"""

urlpatterns = [
    path('', views.index, name='index'), 
    ]