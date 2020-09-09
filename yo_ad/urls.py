from django.conf.urls import include, url
from django.contrib import admin
from yo.views import index, create_ad, save, approve, pending_approval_item_detail, mark_as_approved, mark_as_approved_rescinded, item_detail, edit, update, mark_as_available, mark_as_unavailable, delete, delete_all
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from yo import views

from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView


urlpatterns = [
    # Examples:
    # url(r'^$', 'yo_ad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name="main-view"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('users.urls', namespace="users")),
    url(r'^new/$', save, name="addAd"),
    url(r'^create/$', create_ad, name="ad-view"),
    url(r'^pending_approval_item_detail/(?P<item_id>\d+)/$', pending_approval_item_detail),
    # url(r'^pending_approval_item_detail/(?P<item_id>\d+)/$', pending_approval_item_detail),
    url(r'^approve/$', approve),
    url(r'^mark/(?P<item_id>\d+)/approved/$', mark_as_approved),
    url(r'^mark/(?P<item_id>\d+)/unapproved/$', mark_as_approved_rescinded),
    url(r'^item_detail/(?P<item_id>\d+)/$', item_detail),
    url(r'^edit/(?P<item_id>\d+)/$', edit),
    url(r'^update/(?P<item_id>\d+)/$', update),
    url(r'^mark/(?P<item_id>\d+)/available/$', mark_as_available),
    url(r'^mark/(?P<item_id>\d+)/unavailable/$', mark_as_unavailable),
    url(r'^delete/(?P<item_id>\d+)/$', delete),
    url(r'^delete_all/$', delete_all),




#
# # Url for password reset.
#     url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
#     url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
#     url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#         auth_views.password_reset_confirm, name='password_reset_confirm'),
#     url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),


    #url(r'^se/$', views.send_mail),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

