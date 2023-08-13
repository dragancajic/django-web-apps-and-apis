from django.shortcuts import render
from .models import Post
# '.' is the shortcut for current app, instead of writing
#from blog_app.models import Post

# Create your views here.
def index(request):
    # in views you can put some logic,
    # e.g. make a call to the database ;-)

    # posts - query object that contains all posts pulled from the database
    posts = Post.objects.all()
    print(posts)

    # create context dictionary to fill with query object values
    # context_dict = {'key': query_object}
    context = {'posts': posts}

    for key, value in context.items():
        print(f"key: {key}, value: {value}")

    # pass context dictionary as third argument to the render function
    return render(request, 'blog_app/index.html', context)

    # Now, `index` template has access to the information saved into context dictionary.
