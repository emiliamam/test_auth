from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from users.views import detail, results, vote, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),

]
