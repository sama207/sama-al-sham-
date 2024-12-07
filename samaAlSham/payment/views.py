from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.froms import ShippingForm, PaymentForm
from payment.models import ShippingAddress, Order, OrderItem
from store.models import Product,Profile
from django.contrib import messages
from django.contrib.auth.models import User
import datetime

# Create your views here.
def payment_success(request):
    return render(request, "payment/payment_success.html", {})


def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(
            request,
            "payment/checkout.html",
            {
                "cart_products": cart_products,
                "quantities": quantities,
                "totals": totals,
                "shipping_form": shipping_form,
            },
        )
    else:
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(
            request,
            "payment/checkout.html",
            {
                "cart_products": cart_products,
                "quantities": quantities,
                "totals": totals,
                "shipping_form": shipping_form,
            },
        )


def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()
        shipping_info = request.POST

        my_shipping = request.POST
        request.session["my_shipping"] = my_shipping

        if request.user.is_authenticated:
            billing_form = PaymentForm()
            return render(
                request,
                "payment/billing_info.html",
                {
                    "cart_products": cart_products,
                    "quantities": quantities,
                    "totals": totals,
                    "shipping_info": shipping_info,
                    "billing_form": billing_form,
                },
            )
        else:
            return render(
                request,
                "payment/billing_info.html",
                {
                    "cart_products": cart_products,
                    "quantities": quantities,
                    "totals": totals,
                    "shipping_info": shipping_info,
                    "billing_form": billing_form,
                },
            )
    else:
        messages.success(request, ("لايوجد صلاحية"))
        return redirect("home")


def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        payment_form = PaymentForm(request.POST or None)
        my_shipping = request.session.get("my_shipping")

        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
        full_name = my_shipping["shipping_full_name"]
        email = my_shipping["shipping_email"]
        amount_paid = totals
        if request.user.is_authenticated:
            user = request.user
            create_order = Order(
                user=user,
                order_full_name=full_name,
                order_email=email,
                shipping_address=shipping_address,
                amount_paid=amount_paid,
            )
            create_order.save()
            order_id = create_order.pk
            for product in cart_products():
                product_id = product.id
                if product.is_on_sale:
                    price = product.sale_price
                else:
                    price = product.price

                for key, value in quantities().items():
                    if int(key) == product.id:
                        creat_order_itme = OrderItem(
                            order_id=order_id,
                            product_id=product_id,
                            user=user,
                            quantity=value,
                            price=price,
                        )
                        creat_order_itme.save()

            for key in list(request.session.keys()):
                if key == "session_key":
                    del request.session[key]

            # delete shopping cart
            current_user=Profile.objects.filter(user_id=request.user.id)
            current_user.update(old_cart="")

            
            messages.success(request, "تم تثبيت الطلب")
            return redirect("home")
        else:
            user = request.user
            create_order = Order(
                user=user,
                full_name=full_name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=amount_paid,
            )
            create_order.save()
            order_id = create_order.pk
            for product in cart_products():
                product_id = product.id
                if product.is_on_sale:
                    price = product.sale_price
                else:
                    price = product.price

                for key, value in quantities().items():
                    if int(key) == product.id:
                        creat_order_itme = OrderItem(
                            order_id=order_id,
                            product_id=product_id,
                            quantity=value,
                            price=price,
                        )
                        creat_order_itme.save()

            for key in list(request.session.keys()):
                if key == "session_key":
                    del request.session[key]

            messages.success(request, "تم تثبيت الطلب")
            return redirect("home")
    else:
        messages.success(request, ("لايوجد صلاحية"))
        return redirect("home")


def not_shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=False)

        if request.POST:
            status = request.POST["shipping_status"]
            num=request.POST['num']
            order = Order.objects.filter(id=num)
            now = datetime.datetime.now()
            order.update(shipped=True)
            messages.success(request, ("تم تحديث حالة التوصيل"))

        return render(request, "payment/not_shipped_dash.html", {"orders": orders})
    else:
        messages.success(request, ("لايوجد صلاحية"))
        return redirect("home")


def shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=True)

        if request.POST: 
            status = request.POST["shipping_status"]
            num=request.POST['num']
            order = Order.objects.filter(id=num)
            now = datetime.datetime.now()
            order.update(shipped=Fal,date_shipped=now)
            messages.success(request, ("تم تحديث حالة التوصيل"))
        
        return render(request, "payment/shipped_dash.html", {"orders": orders})
    else:
        messages.success(request, ("لايوجد صلاحية"))
        return redirect("home")


def orders(request, pk):
    if request.user.is_authenticated and request.user.is_authenticated:
        order = Order.objects.get(id=pk)
        items = OrderItem.objects.filter(order=pk)

        if request.POST:
            status = request.POST["shipping_status"]
            now = datetime.datetime.now()
            if status == "true":
                order = Order.objects.filter(id=pk)
                order.update(shipped=True,date_shipped=now)
            else:
                order = Order.objects.filter(id=pk)
                order.update(shipped=False,date_shipped=now)
            messages.success(request, ("تم تحديث حالة التوصيل"))
        return render(request, "payment/orders.html", {"order": order, "items": items})

    else:
        messages.success(request, ("لايوجد صلاحية"))
        return redirect("home")
