
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('movies/', include('movies.urls')),
    path('admin/', admin.site.urls),
]
