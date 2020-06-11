from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
]
