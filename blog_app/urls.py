from django.urls import path
from .views import HomePage, SignUpView, LoginView, AboutView, PostCreateView, PostUpdateView, AllPostsView, PostDetailView, CommentCreationView, CommentDeleteView, CommentEditView, PostDeleteView, SearchView
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('', HomePage.as_view() , name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('about-us/', AboutView.as_view(), name='about-us'),
    path('post-create/', PostCreateView.as_view(), name='post-create'),
    path('post-update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post-delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('allposts/', AllPostsView.as_view(), name='all-posts'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comment/<int:pk>', CommentCreationView.as_view(), name='add-comment'),
    path('delete-comment/<int:pk>', CommentDeleteView.as_view(), name='delete-comment'),
    path('edit-comment/<int:pk>', CommentEditView.as_view(), name='edit-comment'),
    path('search/', SearchView.as_view(), name="search"),
    path('password-reset/', PasswordResetView.as_view(template_name='passwordreset.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="passwordresetdone.html"), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="passwordresetconfirm.html"), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name="passwordresetcomplete.html"), name='password_reset_complete')
]
