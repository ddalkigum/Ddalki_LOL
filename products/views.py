from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from users import mixins
from products import models


class ProductView(ListView):
    model = models.Product
    template_name = "products/home.html"
    context_object_name = "products"
    paginate_by = 30


class ProductDetail(mixins.LoginOnlyView, DetailView):
    model = models.Product
    template_name = "products/detail.html"
    context_object_name = "product"


def search_view(request):
    product = models.Product.objects.all()
    word = request.GET.get("word")
    product_search = product.filter(name__icontains=word)
    return render(
        request,
        "products/search.html",
        {
            "product_search": product_search,
        },
    )
