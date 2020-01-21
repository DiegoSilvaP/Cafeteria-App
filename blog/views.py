from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Category, Cover
from django.urls import reverse, reverse_lazy
from .forms import BlogForm

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
class BlogPageView(ListView):
    model = Post
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['cover'] = Cover.objects.first()
        return context

class CategoryPageView(DetailView):
    model = Category
    template_name = "blog/category.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['cover'] = Cover.objects.first()
        return context

@method_decorator(staff_member_required, name='dispatch')
class BlogPageCreate(CreateView):
    model = Post
    # fields = ['title', 'content', 'image', 'author', 'categories']
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['cover'] = Cover.objects.first()
        return context
        
    def get_success_url(self):
        return reverse('blogPage')


@method_decorator(staff_member_required, name='dispatch')
class BlogPageUpdate(UpdateView):
    model = Post
    # fields = ['title', 'content', 'image', 'author', 'categories']
    form_class = BlogForm
    template_name = 'blog/blog_update_form.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['cover'] = Cover.objects.first()
        return context
        
    def get_success_url(self):
        return reverse('blogPage')
