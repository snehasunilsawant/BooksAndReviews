from django.conf.urls import url , include

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^books/$', views.books),
    url(r'^books/add/$', views.add),
    url(r'^books/addbookandreview/$', views.addbookandreview),
    url(r'^books/(?P<bookid>\d+)/$', views.bookdisplay),
    url(r'^user/(?P<userid>\d+)/$', views.userdisplay),
    url(r'^books/(?P<bookid>\d+)/onlyreview/$', views.onlyreview),



     
]