from django.urls import path

from blog.views import postdetails, showtitle

urlpatterns = [
    path('title/', showtitle, name = 'hello'),
    path('title/<post_name>', postdetails , name = 'info')
]