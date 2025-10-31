from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.static import serve 

urlpatterns = [ 
    path('',views.empty,name='home'),
    path('home/',views.home,name='home'),
    path('about_us/',views.about_us,name='about_us'),
    path('donate/',views.donate,name='donate'),
    path('connect-wallet/', views.connect_wallet, name='connect_wallet'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
