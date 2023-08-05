from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #pass
    #return None

    # return HttpResponse OBJECT or Error!
    return HttpResponse("""
<!DOCTYPE html>
<html>
    <body>
        <h1>This is my Blog!</h1>
        <p>Welcome to <em>my blog</em>!</p>
        <p>If you want, learn more about me
            <a href="https://learn-pisio.eu5.org/" target="_blank">here</a>
        </p>
    </body>
</html>""")
