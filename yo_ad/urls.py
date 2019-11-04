from django.conf.urls import include, url
from django.contrib import admin
from yo.views import index, create_ad, save, approve, pending_item_detail, mark_as_approved, mark_as_approved_rescinded, item_detail, edit, update, mark_as_available, mark_as_unavailable, delete, delete_all, register
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from yo import views

from django.contrib.auth.decorators import login_required

#from yo.views import UserView





from django.views.generic.base import TemplateView


urlpatterns = [
    # Examples:
    # url(r'^$', 'yo_ad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^yo/$', index, name="main-view"),
    url(r'^new/$', save, name="addAd"),
    url(r'^create/$', create_ad, name="ad-view"),
    url(r'^approve/$', approve),
    url(r'^pending_item_detail/(?P<item_id>\d+)/$', pending_item_detail),
    url(r'^mark/(?P<item_id>\d+)/approved/$', mark_as_approved),
    url(r'^mark/(?P<item_id>\d+)/unapproved/$', mark_as_approved_rescinded),
    url(r'^item_detail/(?P<item_id>\d+)/$', item_detail),
    url(r'^edit/(?P<item_id>\d+)/$', edit),
    url(r'^update/(?P<item_id>\d+)/$', update),
    url(r'^mark/(?P<item_id>\d+)/available/$', mark_as_available),
    url(r'^mark/(?P<item_id>\d+)/unavailable/$', mark_as_unavailable),
    url(r'^delete/(?P<item_id>\d+)/$', delete),
    url(r'^delete_all/$', delete_all),
    url(r'^login/$', auth_views.login, {'template_name': 'yo/login.html'}),
    url(r'^logout/$', auth_views.logout, {'template_name': 'yo/logout.html'}),
   # url('profile/',  login_required(UserView.as_view()), name='profile'),
    url(r'^register/', register)
    #url(r'^se/$', views.send_mail),


]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

