
from django.urls import path
from . import views

urlpatterns=[

    #category urls-------------->>>>>>>>>>>>>>
    path('add_category/',views.add_category,name='add_category'),
    path('show_category/',views.category,name='show_category'),
    path('edit_category/<int:pk>',views.edit_cat,name='edit_category'),
    path('delete_category/<int:id>/',views.cat_delete,name='delete_category'),


    ###########post by catgeory url
    path('<int:category_id>/',views.post_by_category,name='post_by_category'),
    ######single_blog------------->>m
    path('blogs<slug:slug_field>/',views.blog,name='blogs'),

 #########dashboard
    path('dash/',views.dashboard,name='dashboard'),

    #########user adding POST######
    path('add_post/',views.add_post,name='add_post'),
    path('post_view/',views.post_view,name='post_view'),
    path('edit_post/<int:pk>',views.edit_post,name='edit_post'),
    path('delete_post/<int:pk>',views.post_delete,name='delete_post'),

    ###########Users

    path('users/',views.users_list,name='users'),
    path('edit_users/<int:pk>',views.edit_user,name='edit_users'),
    path('delete_user/<int:pk>',views.delete_user,name='delete_user')

]

