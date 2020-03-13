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
    name_of_item = forms.CharField(
        max_length=20,
        widget=forms.TextInput({'class': 'form-control'}),
                                   )
    publisher = forms.CharField(
        max_length=20,
        widget=forms.TextInput({'class': 'form-control'}),
                                )
    date_published = forms.DateTimeField(
        widget=forms.TextInput({'class': 'form-control datetimepicker'}),
    )
    description_of_item = forms.CharField(
        max_length=120,
        widget=forms.TextInput({'class': 'form-control'}),
    )
    price = forms.CharField(
        max_length=20,
        widget=forms.TextInput({'class': 'form-control'}),
    )
    category_of_item = forms.ChoiceField(
        required=False,
        label='category',
        widget=forms.Select({'class': 'form-control'}),
        choices=CATEGORY,
    )
    brand_name_of_item = forms.ChoiceField(
        required=False,
        label='brand',
        widget=forms.Select({'class': 'form-control'}),
        choices=BRAND_NAME,
    )
    location = forms.ChoiceField(
        required=False,
        label='location',
        widget=forms.Select({'class': 'form-control'}),
        choices=LOCATION,
    )
    contact = forms.CharField(
        max_length=20,
        widget=forms.TextInput({'class': 'form-control'}),
    )
    available = forms.BooleanField(required=False,  initial=False, label='Available')
    approved = forms.BooleanField(required=False, initial=False, label='Approved')
    item_image = forms.ImageField(
        required=False,
        initial=False,
        label='Item_image',
        widget=forms.FileInput({'class': 'form-control'}),
    )
