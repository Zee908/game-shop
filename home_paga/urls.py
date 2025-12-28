from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import index_view
app_name='home_page'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',index_view,name='index')
]
