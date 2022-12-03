from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<category_slug>', views.category_page, name="category_page"),
    path('<date_added>/<post_slug>', views.post_page, name="post_page")
]
