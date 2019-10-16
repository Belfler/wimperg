from django.urls import path
from django.contrib.auth.decorators import login_required

from images.views import CreateImage

app_name = 'images'

urlpatterns = [
    path('create/', login_required(CreateImage.as_view()), name='create'),
]
