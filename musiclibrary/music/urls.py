#This is only file that will be present in both music AND musiclibrary directories. DON'T CONFUSE THEM!


from django.urls import path
from . import views #importing views.py so we can register our class-based views in a path

urlpatterns = [
  path('music', views.SongList.as_view()), #as_view calling underlying method inside APIView that class-based views inherit from
]

#“as_view()” method determines what method inside our class-based view should be called based on the request’s type and parameters.

##Now register new music/urls.py file in musiclibrary/urls.py