from django.urls import path

from . import views

urlpatterns = [
    path('shorten/', views.ShortenUrl.as_view(), name='shorten'),
    path('premium/', views.CustomizeUrl.as_view(), name='premium'),
    path('list/', views.ListOfUrls.as_view(), name='list'),
    path('<str:shortened_part>', views.Redirect.as_view(), name='redirect'),
]