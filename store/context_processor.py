from .models import Category

def menu_links(req):
    category_links = Category.objects.all()
    return dict(category_links = category_links)