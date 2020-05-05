from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from yo.models.aditem import AdItem, Comment
from django import forms
from yo.forms.yo_form import AdForm, CommentForm # NewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required, login_required

from django.core.mail import send_mail


def index(request):
    all_items = AdItem.objects.filter(approved=True)
    my_range = range(0, len(all_items), 3)
    #print(my_range)
    items = []

    for i in my_range:
        sub_array = all_items[i:i+3]
        items.append(sub_array)

    #print(items)
    # import pdb; pdb.set_trace()
    return render(request, 'yo/index.html', {'items': items})

@login_required(login_url='users:login')
def create_ad(request):
    #declared here pls
    # import pdb; pdb.set_trace()
    item_form = AdForm()


    return render(request, 'yo/create.html', {'form': item_form})


def save(request):

    if request.method == "POST":
        print(request.POST)
        item_form = AdForm(request.POST, request.FILES)

        # import pdb;
        # pdb.set_trace()

        if item_form.is_valid():
            new_item = AdItem()
            new_item.name_of_item = item_form.cleaned_data['name_of_item']
            new_item.publisher = item_form.cleaned_data['publisher']
            new_item.date_published = item_form.cleaned_data['date_published']
            new_item.description_of_item = item_form.cleaned_data['description_of_item']
            new_item.price = item_form.cleaned_data['price']
            new_item.category_of_item = item_form.cleaned_data['category_of_item']
            new_item.brand_name_of_item = item_form.cleaned_data['brand_name_of_item']
            new_item.location = item_form.cleaned_data['location']
            new_item.contact = item_form.cleaned_data['contact']
            new_item.available = item_form.cleaned_data['available']
            new_item.approved = item_form.cleaned_data['approved']
            new_item.item_image = item_form.cleaned_data['item_image']
            new_item.save()

            send_mail()

            return HttpResponseRedirect('/yo/')

    else:
        item_form = AdForm()
    return render(request, 'yo/create.html', {'form': item_form})


@login_required(login_url='users:login')
def approve(request):
    all_items = AdItem.objects.filter(approved=False)
    my_range = range(0, len(all_items), 3)
    # print(my_range)
    items = []
    for i in my_range:
        sub_array = all_items[i:i + 3]
        items.append(sub_array)

    # print(items)
    # import pdb; pdb.set_trace()
    return render(request, 'yo/to_be_approved.html', {'items': items})


def pending_item_detail(request,item_id):
    item = AdItem.objects.get(pk=item_id)
    return render(request, 'yo/pending_item_detail.html', {'item': item})


def mark_as_approved(request, item_id):
    item = AdItem.objects.get(pk=item_id)
    item.approved = True
    item.save()
    #return HttpResponseRedirect('/item_detail/')
    return render(request, 'yo/pending_item_detail.html', {'item': item})


def mark_as_approved_rescinded(request, item_id):
    item = AdItem.objects.get(pk=item_id)
    item.approved = False
    item.save()
    #return HttpResponseRedirect('/item_detail/')
    return render(request, 'yo/pending_item_detail.html', {'item': item})


def item_detail(request, item_id):
    item = AdItem.objects.get(pk=item_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=item
            )
            comment.save()
    comments = Comment.objects.filter(post=item)
    return render(request, 'yo/item_detail.html', {'item': item,
                                                   'comments': comments,
                                                   "form": form})


@login_required(login_url='users:login')
def edit(request, item_id):
    item = AdItem.objects.get(pk=item_id)
    params = {'name_of_item': item.name_of_item,
              'publisher': item.publisher,
              'date_published': item.date_published,
              'description_of_item': item.description_of_item,
              'price': item.price,
              'category_of_item': item.category_of_item,
              'brand_name_of_item': item.brand_name_of_item,
              'location': item.location,
              'contact': item.contact,
              'available': item.available,
              'approved': item.approved,
              'item_image': item.item_image
              }
    item_form = AdForm(initial=params)
    return render(request, 'yo/edit.html', {'item': item, 'form': item_form})


def update(request, item_id):
    item = AdItem.objects.get(pk=item_id)
    item_form = AdForm(request.POST, request.FILES)
    if item_form.is_valid():

        item.name_of_item = item_form.cleaned_data['name_of_item']
        item.publisher = item_form.cleaned_data['publisher']
        item.date_published = item_form.cleaned_data['date_published']
        item.description_of_item = item_form.cleaned_data['description_of_item']
        item.price = item_form.cleaned_data['price']
        item.category_of_item = item_form.cleaned_data['category_of_item']
        item.brand_name_of_item = item_form.cleaned_data['brand_name_of_item']
        item.location = item_form.cleaned_data['location']
        item.contact = item_form.cleaned_data['contact']
        item.available = item_form.cleaned_data['available']
        item.approved = item_form.cleaned_data['approved']
        item.item_image = item_form.cleaned_data['item_image']
        item.save()
        return HttpResponseRedirect('/yo/')
    else:
        return render(request, 'yo/edit.html', {'item':item, 'form': item_form})

@login_required(login_url='users:login')
def mark_as_available(request, item_id):
    item = AdItem.objects.get(pk=item_id)
    item.available = True
    item.save()
    #return HttpResponseRedirect('/item_detail/')
    return render(request, 'yo/item_detail.html', {'item': item})

@login_required(login_url='users:login')
def mark_as_unavailable(request, item_id):
    item = AdItem.objects.get(pk=item_id)
    item.available = False
    item.save()
    #return HttpResponseRedirect('/item_detail/')
    return render(request, 'yo/item_detail.html', {'item': item})


@login_required(login_url='users:login')
def delete(request, item_id):
    item = AdItem.objects.get(pk=item_id)
    item.delete()
    return HttpResponseRedirect('/yo/')


@login_required(login_url='users:login')
def delete_all(self):
    AdItem.objects.all().delete()
    return HttpResponseRedirect('/yo/')



def send_mail():
    #import pdb; pdb.set_trace()
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase

    msg = MIMEMultipart()
    msg['From'] = 'peedorNetwork@gmail.com'
    msg['To'] = 'regioths@gmail.com'
    msg['Subject'] = 'New Ad'

    body = 'This is a new Ad awaiting your approval'
    msg.attach(MIMEText(body, 'plain'))

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login('peedorNetwork@gmail.com', 'mayais123_pee')
        server.sendmail('peedorNetwork@gmail.com', 'regioths@gmail.com', text)
    except:
        pass
    server.quit()





