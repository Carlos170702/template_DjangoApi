from django.urls import path

from apps.users.api.view import user_view, user_detail_view

urlpatterns = [
    path('', user_view.as_view(), name='users'),
    path('detail/<int:pk>', user_detail_view.as_view(), name='users'),
]
