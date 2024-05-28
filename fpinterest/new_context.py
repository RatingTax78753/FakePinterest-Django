from .models import Post

def todos_posts(request):
    posts = Post.objects.order_by('-data_criacao').all()
    return {"todos_posts": posts}