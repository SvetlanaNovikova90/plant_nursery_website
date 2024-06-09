from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm, ProductIsPublishedForm, ProductDescriptionForm, ProductCategoryForm
from catalog.models import Product, BlogPost, Version


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

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            active_versions = versions.filter(is_active=True)
            if active_versions:
                product.active_version = active_versions.last().title
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = products
        return context_data


class ProductsDetailView(DetailView):
    model = Product
    template_name = "catalog/products_detail.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy('shop:products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):

        product = form.save()
        product.creator = self.request.user
        product.save()

        context_data = self.get_context_data()
        formset = context_data['formset']

        if formset.is_valid():
            formset.instance = product
            formset.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy('shop:products')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return product.creator == user or user.is_superuser

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data["formset"] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    # def get_form_class(self):
    #     user = self.request.user
    #     if user == self.object.owner:
    #         return ProductForm
    #     if user.has_perm("catalog.can_edit_description") and user.has_perm("catalog.can_edit_category"):
    #         return ProductModeratorForm
    #     return PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy('shop:products')


class ProductUpdateIsPublishedView(UpdateView, PermissionRequiredMixin):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductIsPublishedForm
    permission_required = ('Can change product published status',)

    success_url = reverse_lazy('shop:products')


class ProductUpdateDescriptionView(UpdateView, PermissionRequiredMixin):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductDescriptionForm
    permission_required = ('Can change product description',)

    success_url = reverse_lazy('shop:products')


class ProductUpdateCategoryView(UpdateView, PermissionRequiredMixin):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductCategoryForm
    permission_required = ('Can change product category',)

    success_url = reverse_lazy('shop:products')


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
