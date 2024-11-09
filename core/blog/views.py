from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post

# Create your views here.

def indexView(request):
    name = 'ali' 
    posts = Post.objects.all()
    context = {"name": name, "posts": posts}
    return render(request, 'index.html', context)


class HomePageView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'ali'
        context["posts"] = Post.objects.all()  # Fetch all posts from the database and add it to the context.  # Assuming Post is a model that represents your blog posts.  # Replace this line with your actual database query.  # This is a simple example to demonstrate the concept.  # In a real-world application, you should fetch the posts based on the user's preferences and other criteria.  # Also, you should paginate the posts to avoid
        return context