from django.shortcuts import render

from mywatchlist.models import Movie

# TODO: Create your views here.

data_barang_katalog = Movie.objects.all()
context = {
    'list_barang': data_barang_katalog,
    'nama': 'Adam'
}

def show_mywishlist(request):
    return render(request, "mywishlist.html", context)