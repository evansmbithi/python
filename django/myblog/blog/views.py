from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 1) #paginate every 1 post or any number of posts
    
    page = request.GET.get('page') #extract the page variable from the url in our view

# if page is NOT an integer, return page 1
    try:
        posts = paginator.page(page)
    except (PageNotAnInteger):
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) # return last page by counting number of pages


    return render(request, 'pages/home.html', {'posts' : posts}) # ?page=2

def single(request, single):
    single = Post.objects.get(id=single)
    context = {
        'post' : single
    }
    return render(request, 'pages/single.html', context)
