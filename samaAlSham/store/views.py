from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from django import forms


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {"product": product})


def category(request, cat):
    cat = cat.replace("-", " ")
    try:
        if cat == "نسائي" or cat == "رجالي" or cat == "ولادي" or cat == "بناتي":
            category = Category.objects.filter(parent_category=cat)
            products = []
            for categ in category:
                products.extend(Product.objects.filter(category=categ))
            return render(
                request, "category.html", {"products": products, "category": cat}
            )
        else:
            category = Category.objects.get(name=cat)
            products = Product.objects.filter(category=category)
            return render(
                request, "category.html", {"products": products, "category": category}
            )

    except:
        messages.success(request, ("الصنف غير موجود"))
        return redirect("home")


def login_user(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول")
            return redirect("home")
        else:
            messages.success(request, "حدث خطأ اثناء تسجيل الدخول")
            return redirect("login")

    else:
        return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("تم تسجيل الخروج"))
    return redirect("home")


def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("تم انشاء حسابك يمكنك ملئ معلومات الشخصية"))
            return redirect("update_info")
        else:
            messages.success(request, ("حدث خطأ ,الرجاء المحاولة لاحقا"))
            return redirect("register")

    return render(request, "register.html", {"form": form})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "تم تعديل معلومات المستخدم")
            return redirect("home")

        return render(request, "update_user.html", {"user_form": user_form})

    else:
        messages.success(request, "يجب ان تقوم بتسجيل الدخول")
        return redirect("home")


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user

        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "تم تعديل كلمة المرور")
                login(request, current_user)
                return redirect("update_user")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect("update_password")
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {"form": form})

    else:
        messages.success(request, "يجب ان تقوم بتسجيل الدخول")
        return redirect("home")


def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()

            messages.success(request, "تم تعديل معلوماتك")
            return redirect("home")

        return render(request, "update_info.html", {"form": form})

    else:
        messages.success(request, "يجب ان تقوم بتسجيل الدخول")
        return redirect("home")
