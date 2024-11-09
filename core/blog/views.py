from django.shortcuts import render 
from django.views.generic.base import TemplateView
from .models import Post
from django.views.generic.base import RedirectView

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