from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product, BlogPost


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

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class PostDetailView(DetailView):
    model = BlogPost
    template_name = "catalog/post_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class PostUpdateView(UpdateView):
    model = BlogPost
    template_name = "catalog/post_form.html"
    fields = ('title', 'description', 'image_ph',)
    # success_url = reverse_lazy('shop:blog_post')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('shop:post_detail', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = BlogPost
    template_name = "catalog/blogpost_confirm_delete.html"
    success_url = reverse_lazy('shop:blog_post')
