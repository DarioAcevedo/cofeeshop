from .models import Link

def context_dict(request):
    ctx_dict = {}
    links = Link.objects.all()
    for link in links:
        ctx_dict[link.key] = link.url
    return ctx_dict