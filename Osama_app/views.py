from django.shortcuts import get_object_or_404, render,redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from .forms import MessageForm

def message(request):
    if request.method=='POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Osama_app:sent')
    else:
        form=MessageForm()
    context={'form':form}
    return render(request,'Osama_app/message.html',context)

def sent(request):
    return render(request,'Osama_app/sent.html')

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context={
    'category': category,
    'categories': categories,
    'products': products
    }
    return render(request,'Osama_app/product/list.html',context)

@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(
    Product, id=id, slug=slug, available=True
    )
    cart_product_form = CartAddProductForm()
    context={'product': product,
             'cart_product_form':cart_product_form}
    return render(request,'Osama_app/product/detail.html',context)


