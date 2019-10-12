from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

from wimperg.views import *

app_name = 'wimperg'


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='wimperg:news'), name='index'),
    path('news/', login_required(News.as_view()), name='news'),
    path('register/', Registration.as_view(), name='registration'),
]
