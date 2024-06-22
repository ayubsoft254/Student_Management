from django.urls import path
from .views import list_student, update_student, delete_student, add_student, search_student

urlpatterns = [
    path('', list_student, name='list_student'),
    path('update_student/<int:id>/', update_student, name='update_student'),
    path('delete_student/<int:id>/', delete_student, name='delete_student'),
    path('add/', add_student, name="add_student"),
    path("search_student", search_student, name="search")
]
