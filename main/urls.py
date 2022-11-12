from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>', views.category_page, name="category_page"),
    path('<slug:category>/<slug:slug>', views.post_page, name="post_page")
]
