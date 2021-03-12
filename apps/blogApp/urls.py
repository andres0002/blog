from django.urls import path
from .views import home, generals, programation, videogames, tecnologi, detailPost

urlpatterns = [
    path('', home, name='index'),
    path('general/', generals, name='general'),
    path('programation/', programation, name='programation'),
    path('videogames/', videogames, name='videogames'),
    path('tecnologi/', tecnologi, name='tecnologi'),
    path('<slug:slug>', detailPost, name='detailPost')
]