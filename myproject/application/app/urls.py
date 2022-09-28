
from django.urls import path
from.views import article_list,art_detail



urlpatterns = [
    path('art/',article_list),
    path('detail/<int:pk>/',art_detail),
]
