from django.urls import path
from . import views
from .views import UpdatePostView

urlpatterns = [
    #path('', views.index, name='index'),
    #blogs
    path("", views.blogs, name="blogs"),
    path("blog/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),
    path("search/", views.search, name="search"),

    #profile
    path("profile/", views.Profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("user_profile/<int:my_id>/", views.user_profile, name="user_profile"),

    #user_authentication
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="Login"),
    path("logout/", views.Logout, name="Logout"),   
]
