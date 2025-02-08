from django.urls import path
from .views import user_login, user_register, user_logout, record_list, edit_record, delete_record

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('register/', user_register, name='user_register'),
    path('logout/', user_logout, name='user_logout'),
    path('records/', record_list, name='record_list'),
    path('records/edit/<int:record_id>/', edit_record, name='edit_record'),
    path('records/delete/<int:record_id>/', delete_record, name='delete_record'),
]