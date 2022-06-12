from django.urls import path, include

from users.views import detail, results, vote, index
from users.views import Register

urlpatterns = [
    path('users/', include('django.contrib.auth.urls')),
    path('', index, name='home'),
    path('polls/<int:question_id>', detail, name='detail'),
    path('polls/<int:question_id>/results', results, name='results'),
    path('polls/<int:question_id>/vote>', vote, name='vote'),
    path('users/register/', Register.as_view(), name='register'),
]
