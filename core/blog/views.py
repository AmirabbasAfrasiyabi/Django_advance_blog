from django.shortcuts import render 
from django.views.generic.base import TemplateView
from .models import Post
from django.views.generic.base import RedirectView
from django.views.generic import ListView , DetailView
# Create your views here.

# fbv Show a Template

"""
def indexView(request):

    # the function base views to show index page
    
    name = 'ali' 
    posts = Post.objects.all()
    context = {"name": name, "posts": posts}
    return render(request, 'index.html', context)
"""

class HomePageView(TemplateView):

    """
    the class base views to show index page
    """

    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'ali'
        context["posts"] = Post.objects.all()  # Fetch all posts from the database and add it to the context.  # Assuming Post is a model that represents your blog posts.  # Replace this line with your actual database query.  # This is a simple example to demonstrate the concept.  # In a real-world application, you should fetch the posts based on the user's preferences and other criteria.  # Also, you should paginate the posts to avoid
        return context
    

# fbv for redirect

"""
 def RedirectToLinkedIn(request):

    # the function base views to redirect to another page
    
    return redirect('https://linkedin.com/feed/')
"""

class RedirectToLinkedIn(RedirectView):

    """
    the class base views to redirect to another page
    """

    url = "https://linkedin.com/in/amirabbas-afrasiyabi-a6a230259/"


# cbv for list

class PostList(ListView):

    """
    the class base views to show all posts
    """
    # models1
    # queryset = Post.objects.all()

    # models2
    model = Post

    # same for all three models
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 2  # Set the number of posts to show per page.
    ordering = "-published_date"  # Set the order of posts to be displayed. You can also use "-created_date" or any other field.
    queryset = Post.objects.filter(status=True)  # Filter posts to only show published ones. You can also use "-created_date" or any other field.
    
    #models3
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    