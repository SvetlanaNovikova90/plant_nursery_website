from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.models import Product, BlogPost


class ContactTemplateView(TemplateView):
    template_name = "catalog/contact.html"

    def get(self, request, **kwargs):
        if request.method == "POST":
            name = request.get("name")
            phone = request.get("phone")
            message = request.POST.get("message")
            print(f"{name} ({phone}): {message}")
        return request


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, "catalog/contact.html")


class ProductsListView(ListView):
    model = Product
    template_name = "catalog/products_list.html"


class ProductsDetailView(DetailView):
    model = Product
    template_name = "catalog/products_detail.html"


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "catalog/blog_post_list.html"


class PostCreateView(CreateView):
    model = BlogPost
    template_name = "catalog/post_form.html"
    fields = ('title', 'description', 'image_ph',)
    success_url = reverse_lazy('shop:blog_post')


class PostDetailView(DetailView):
    model = BlogPost
    template_name = "catalog/post_detail.html"


class PostUpdateView(UpdateView):
    model = BlogPost
    template_name = "catalog/post_form.html"
    fields = ('title', 'description', 'image_ph',)
    success_url = reverse_lazy('shop:blog_post')


class PostDeleteView(DeleteView):
    model = BlogPost
    template_name = "catalog/blogpost_confirm_delete.html"
    success_url = reverse_lazy('shop:blog_post')