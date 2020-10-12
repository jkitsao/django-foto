from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^location/(\d+)',views.display_location,name='displayLocation'),
    url(r'^search/',views.search_category,name='search_category'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
