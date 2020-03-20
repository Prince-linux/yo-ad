from django import forms

from yo.models.aditem import AdItem


class AdForm(forms.Form):
#     remove all other fields I just want us to investigate date time field
    # thus create a new form and a new view to create the empty form and also to receive and process it
    #
    name_of_item = forms.CharField(
        max_length=20,
        widget=forms.TextInput({'class': 'form-control'}),
                                   )
    publisher = forms.CharField(
        max_length=20,
        widget=forms.TextInput({'class': 'form-control'}),
                                )

    date_published = forms.DateTimeField(
        input_formats=['%Y/%m/%d %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }),
    )

    description_of_item = forms.CharField(
        max_length=120,
        widget=forms.TextInput({'class': 'form-control'}),
    )

    price = forms.CharField(
        max_length=20,
        widget=forms.TextInput({'class': 'form-control'}),
    )

    category_of_item = forms.CharField(
        max_length=20,
        widget=forms.TextInput({'class': 'form-control'}),
    )

    brand_name_of_item = forms.CharField(
        max_length=20,
        widget=forms.TextInput({'class': 'form-control'}),
    )

    location = forms.CharField(
        max_length=20,
        widget=forms.TextInput({'class': 'form-control'}),
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
