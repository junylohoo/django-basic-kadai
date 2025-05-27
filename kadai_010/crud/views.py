from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import DetailView
from .models import Product


class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product
    paginate_by = 3

class ProductDetailView(DetailView):
    model = Product

