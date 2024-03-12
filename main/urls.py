from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('all-news', views.all_news, name='all-news'),
    path('details/<int:id>', views.details, name='details'),
    path('all-categories', views.all_categories, name='all-categories'),
    path('category/<int:id>', views.category, name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
