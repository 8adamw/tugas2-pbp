from django.urls import path
from katalog.views import show_katalog

app_name = 'wishlist'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
    path('katalog/', include('katalog.urls')),
]