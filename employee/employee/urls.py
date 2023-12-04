"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from work.views import Employee,BookView,Booklist,Book_detailView,Book_delete,DetailsView,Detailslist,StudentsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',Employee.as_view()),
    path('details/',DetailsView.as_view()),
    path('details/all/',Detailslist.as_view()),
    path('details/',DetailsView.as_view()),
    path('students/',StudentsView.as_view()),
    path('book/',BookView.as_view()),
    path('books/all/',Booklist.as_view(),name="book-al"),
    path('books/<int:pk>',Book_detailView.as_view(),name="book-det"),
    path('books/<int:pk>/remove/',Book_delete.as_view(),name="book-del"),

]
