from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('/aboutus', aboutus, name='aboutus'),
    path('/tests', testpage, name='tests'),
    path('/packages', packages, name='packages'),
    path('/blogs', blogs, name='blogs'),
    path('/gallery', gallery, name='gallery'),
    path('/branches', branches, name='branches'),
    path('/contactus', contact_us, name='contactus'),
    path('/bookappointemnt', book_appontment, name='bookappointemnt'),
    path('/dtpack/<int:id>', detail_packages, name='dtpack'),
    path('/dtblog/<int:id>', detail_blogepage, name='dtblog'),
    path('/detailbranches/<int:id>', branch_detailed, name='detailbranches')
]
