from django import forms


CATEGORY = (
    ('ELECTRONICS', 'electronics'),
    ('HOUSING & REAL ESTATES', 'housing & real estates'),
    ('FURNITURE', 'furniture'),
    ('FOOD', 'food'),
    ('CLOTHING', 'clothing'),
    ('VEHICLES & BIKES', 'vehicles & bikes'),
    ('BOOKS', 'books'),
    ('OTHER', 'other'),
    )

BRAND_NAME = (
    ('HP', 'hp'),
    ('SAMSUNG', 'samsung'),
    ('APPLE', 'apple'),
    ('LG', 'lg'),
    ('TOSHIBA', 'toshiba'),
    ('LAND ROVER', 'land rover'),
    ('MERCEDES', 'mercedes'),
    ('OTHER', 'other'),
    )

LOCATION = (

    ('ACCRA', 'accra'),
    ('KUMASI', 'kumasi'),
    ('TEMA', 'tema'),
    ('KOFORIDUA', 'koforidua'),
    ('TAKORADI', 'takoradi'),
    ('WINNEBA', 'winneba'),
    ('TAMALE', 'tamale'),
    ('WA', 'wa'),
    ('BOLGATANGA', 'bolgatanga'),
    ('SUNYANI', 'sunyani'),
    ('SEKONDI', 'sekondi'),
    ('CAPE-COAST', 'cape-coast'),
    ('HO', 'ho'),

    )


class AdForm(forms.Form):
    name_of_item = forms.CharField(max_length=20)
    publisher = forms.CharField(max_length=20)
    date_published = forms.DateTimeField()
    description_of_item = forms.CharField(max_length=120)
    price = forms.CharField(max_length=20)
    category_of_item = forms.ChoiceField(
        required=False,
        label='category',
        widget=forms.Select,
        choices=CATEGORY,
    )
    brand_name_of_item = forms.ChoiceField(
        required=False,
        label='brand',
        widget=forms.Select,
        choices=BRAND_NAME,
    )
    location = forms.ChoiceField(
        required=False,
        label='location',
        widget=forms.Select,
        choices=LOCATION,
    )
    contact = forms.CharField(max_length=20)
    available = forms.BooleanField(required=False,  initial=False, label='Available')
    approved = forms.BooleanField(required=False, initial=False, label='Approved')
    item_image = forms.ImageField(required=False, initial=False, label='Item_image')

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    email = forms.CharField(
        required=True,
        label='Email',
        max_length=32,
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )