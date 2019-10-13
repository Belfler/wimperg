from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from wimperg.views import *

app_name = 'wimperg'


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='wimperg:news'), name='index'),
    path('register/', Registration.as_view(), name='registration'),
    path('news/', login_required(News.as_view()), name='news'),
    path('edit/', login_required(ChangingProfile.as_view()), name='edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
