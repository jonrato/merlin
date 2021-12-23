from django.shortcuts import redirect, render
from stripe.api_resources import coupon, price, subscription
from .forms import IceForm, MultipleIceForm
from django.forms import formset_factory
from django.urls import reverse_lazy
from .models import Icecream
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import stripe

stripe.api_key = 'sk_test_51Ixem2AjWsDHngBzTLVjXKp4XcUgm1N6ji0okggVu7Mua0SL2lu55unuBP1O01YuDPJPfWEKJ9PwgVJCL8gq3luB00stlvkTnH'
def home(request):
    return render(request,'stripe/home.html')
    
def order(request):
    multiple_form = MultipleIceForm()
    if(request.method == 'POST'):
        filled_form = IceForm(request.POST)
        if(filled_form.is_valid()):
            prepared_icecream = filled_form.save()
            prepared_icecream_pk = prepared_icecream.id
            note = "Thanks for Ordering! Your %s %s and %s Icecream is on its way!" %(filled_form.cleaned_ta['size'],
            filled_form.cleaned_data['topping1'],
            filled_form.cleaned_data['topping2'],)
            filled_form = IceForm()
        else:
            prepared_icecream_pk = None
            note = "Icecream Order has Failed. Please Try Again!!!"
        return render(request, 'icecreams/order.html', {'prepared_icecream_pk':prepared_icecream_pk,'IceForm': filled_form,'note':note,'multiple_form':multiple_form})

    else:
        form = IceForm()
        return render(request, 'stripe/order.html', {'Iceform': form})

def join(request):
    return render(request, 'stripe/join.html')


def icecreams(request):
    num_of_icecreams = 2
    filled_multi_ice_form = MultipleIceForm(request.GET)
    if(filled_multi_ice_form.is_valid()):
        num_of_icecreams = filled_multi_ice_form.cleaned_data['numofice']
    IceFormSet = formset_factory(IceForm, extra = num_of_icecreams)
    formset = IceFormSet()
    if(request.method == 'POST'):
        filled_formset = IceFormSet(request.POST)
        if(filled_formset.is_valid()):
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
                note = 'Icecreams have been ordered'

        else:
            note = 'Oder has not been created. Please Try Again!!!'
        return render(request, 'stripe/icecreams.html', {'note':note,'formset':formset})

    else:
        return render(request, 'stripe/icecreams.html',{'formset':formset})

def edit_order(request, pk):
    icecream = Icecream.objects.get(pk=pk)
    form = IceForm(instance = icecream)
    if(request.method == 'POST'):
        filled_form = IceForm(request.POST, instance=icecream)
        if(filled_form.is_valid()):
            filled_form.save()
            form = filled_form
            note = 'Order has been updated'
            return render(request, 'stripe/edit_order.html', {'note':note})
    return render(request, 'stripe/edit_order.html', {'IceForm': form,'icecream':icecream})
@login_required
def checkout(request):
    coupons = {"diwali":15,"christmas":20}
    if request.method == 'POST':
        stripe_customer = stripe.Customer.create(email=request.user.email, 
        source=request.POST['stripeToken'])
        price='prod_Jar64zTuC2IMdE'
        if request.POST['price'] == 'Medium':
            price='prod_Jar4mwXGucBfuD'
        if request.POST['price'] == 'Large':
            price='prod_Jar6sP65iCJ3UI'
        if request.POST['coupon'] in coupons:
            percentage = coupons[request.POST['coupons'].lower()]
            try:
                coupon = stripe.Coupon.create(duration='once',
                                id=request.POST['coupon'].lower(),
                                percent_off=percentage)
            except:
                pass
            #subscription = stripe.Subscription.create(costumer=stripe_customer.id,
            #items=[{'price':price}])    
        #else:
            #subscription = stripe.Subscription.create(costumer=stripe_customer.id,
            #items=[{'price':price}],
            #coupon=request.POST['coupon'].lower())
        return redirect('join')
    else:
        price = 'Cup'
        coupon = 'none'
        amount = 200
        original_amt = 200
        coupon_amt = 0
        final_amt = 200
        if request.method == 'GET' and "price" in request.GET:
            if request.GET['price'] == 'Medium':
                price = 'Medium'
                amount = 100
                original_amt = 100
                final_amt = 100

            if request.GET['price'] == 'Large':
                price = 'Large'
                amount = 250
                original_amt = 250
                final_amt = 250
        if request.method == 'GET' and "coupon" in request.GET:
            if request.GET['coupon'].lower() in coupons:
                coupon = request.GET['coupon'].lower()
                percentage = coupons[request.GET['coupon'].lower()]
                coupon_price = float((percentage/100)*amount)
                amount = amount - coupon_price
                coupon_amt = str(coupon_price)
                final_amt = str(amount)
                amount = amount*100

        return render(request, 'stripe/checkout.html', {'price':price,'coupon':coupon,
                'amount':amount, 'original_amt':original_amt,'final_amt':final_amt,
                'coupon_amt':coupon_amt})

def settings(request):
    return render(request, 'stripe/settings.html')