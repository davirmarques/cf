from django.urls import path, include # new

from .views import BlogListView # new

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    ]



