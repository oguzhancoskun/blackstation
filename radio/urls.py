from django.conf.urls import patterns, include, url
from django.conf import settings

from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

from soulradio import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'radio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home),
)


