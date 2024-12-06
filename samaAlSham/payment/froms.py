from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):

    shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "الاسم كامل"},
        ),
        required=True,
    )
    shipping_email = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "الايميل"},
        ),
        required=True,
    )
    shipping_address1 = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "العنوان الاول للتوصيل"},
        ),
        required=True,
    )
    shipping_address2 = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "العنوان الثاني للتوصيل"},
        ),
        required=False,
    )
    shipping_city = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "المدينة"},
        ),
        required=True,
    )
    shipping_state = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "الدولة"},
        ),
        required=False,
    )
    shipping_zipcode = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "الرمز البريدي"},
        ),
        required=False,
    )
    shipping_country = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "البلد"},
        ),
        required=True,
    )

    class Meta:
        model = ShippingAddress
        fields = [
            "shipping_full_name",
            "shipping_email",
            "shipping_address1",
            "shipping_address2",
            "shipping_city",
            "shipping_state",
            "shipping_zipcode",
            "shipping_country",
        ]
        exclude = [
            "user",
        ]


class PaymentForm(forms.Form):
    card_name = shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "الاسم على البطاقة"},
        ),
        required=True,
    )
    card_number = shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "رقم البطاقة"},
        ),
        required=True,
    )
    card_exp_date = shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "تاريخ انتهاء صلاحية البطاقة",
            },
        ),
        required=True,
    )
    card_cvv_number = shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "cvv"},
        ),
        required=True,
    )
    card_address1 = shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "العنوان الاول"},
        ),
        required=True,
    )
    card_address2 = shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "العنوان الثاني"},
        ),
        required=True,
    )
    card_city = shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "المدينة"},
        ),
        required=True,
    )
    card_state = shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "الدولة"},
        ),
        required=True,
    )
    card_zipcode = shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "الرمز البريدي"},
        ),
        required=True,
    )
    card_country = shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "البلد"},
        ),
        required=True,
    )
