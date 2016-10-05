from django.conf.urls import url
from wordbook import views

from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^wordbook/$', views.WordList.as_view()),
    url(r'^wordbook/(?P<pk>[0-9]+)/$', views.WordDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
