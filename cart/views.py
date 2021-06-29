from django.shortcuts import redirect, render
from .models import Cart
from django_app.models import Post_Assinaturas

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    
    return render(request, "carts/home.html", {"cart":cart_obj})

def cart_update(request):
    print(request.POST)
    product_id=request.POST.get("product_id")
    if product_id is not None:
        try:
            product_obj=Post_Assinaturas.objects.get(id=product_id)
        except Post_Assinaturas.DoesNotExist:
            print("Mostrar mensagem ao usuario, esse produto acabou")
            return redirect("cart:home")
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)
    request.session['cart_items']=cart_obj.products.count()

    return redirect("cart:home")