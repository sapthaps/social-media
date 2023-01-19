from django.urls import path
from .views import *
urlpatterns = [
    path("register/",SignUpView.as_view(),name="signup"),
    path("login/",SignInView.as_view(),name="signin"),
    path("index/",IndexView.as_view(),name="index"),
    path("posts/<int:id>/comment/add",add_comment,name="add-comment"),
    path("post/<int:id>/like/add",like_post_view,name="add-like"),
    path("profile/", Profile.as_view(), name='profile'),
    path("user/<int:id>/follower/add", add_follower, name="add-follower"),
    path("logout",signout_view,name="sign-out"),
    path("comment/<int:id>/delete",delete_comment,name="comment-delete"),
    path("people/", ListPeopleView.as_view(), name="people"),
    
    path("add/profile",AddProfile.as_view(),name="addprofile")
]
