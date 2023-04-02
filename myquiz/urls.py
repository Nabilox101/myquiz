from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dictio import views as dictio_views
from quiz import views as quiz_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dictio_views.home, name='home'),
    path('search/', dictio_views.search, name='search'),
    path('autocomplete/', dictio_views.autocomplete, name='autocomplete'),
    path('summernote/', include('django_summernote.urls')),
    path('quiz/', quiz_views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', quiz_views.question_quiz_list, name='question_quiz_list'),
    path('quiz/<int:quiz_id>/result/', quiz_views.result, name='result'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
