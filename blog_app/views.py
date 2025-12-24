from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Blog, Comment
from .forms import UserCreationForm, LoginForm, PostCreationForm, PostUpdateForm, CommentCreateForm, CommentEditForm
from django.contrib.auth import login
from django.contrib import messages
from .mixins import AdminRequiredMixin, UserRequiredMixin
from django.db.models import Q

# Create your views here.
class AboutView(generic.TemplateView):
    template_name = 'about.html'

class SearchView(generic.ListView):
    model = Blog
    template_name = "search_result.html"
    context_object_name = "results"

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Blog.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-created_at')
        return Blog.objects.none()

class HomePage(generic.ListView):
    template_name = "home.html"
    context_object_name = "blog"

    def get_queryset(self):
        posts = Blog.objects.all().order_by('-created_at')[:10]
        return posts
    
class SignUpView(generic.CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)    
        return redirect(self.success_url)
    

class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
    
class PostCreateView(AdminRequiredMixin, generic.CreateView):
    model = Blog
    template_name = 'blog_form_create.html'
    form_class = PostCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(AdminRequiredMixin, generic.UpdateView):
    model = Blog
    template_name = 'blog_update_form.html'
    form_class = PostUpdateForm
    success_url = reverse_lazy('home')

    def get_queryset(self):
        qs = super().get_queryset()
        return Blog.objects.filter(pk=self.kwargs['pk'])
    
class PostDeleteView(AdminRequiredMixin, generic.DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author = self.request.user)

class AllPostsView(generic.ListView):
    model = Blog
    template_name = 'allposts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Blog.objects.all().order_by('-created_at')[:30]
        return posts
    
class PostDetailView(generic.DetailView):
    model = Blog
    template_name = 'postdetail.html'
    context_object_name = 'post'

class CommentCreationView(UserRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'commentcreate.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk':self.kwargs['pk']})
    
class CommentEditView(UserRequiredMixin, generic.UpdateView):
    model = Comment
    template_name = "commentedit.html"
    form_class = CommentEditForm
    
    def get_success_url(self):
        postid = self.object.post.id
        return reverse_lazy('post-detail', kwargs={'pk':postid})

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author = self.request.user)

class CommentDeleteView(UserRequiredMixin, generic.DeleteView):
    model = Comment
    template_name = "commentdelete.html"
    
    def get_success_url(self):
        postid = self.object.post.id
        return reverse_lazy('post-detail', kwargs = {'pk':postid})
    
    def form_valid(self, form):
        messages.success(self.request,"Comment was deleted successfully.")
        return super().form_valid(form)
    

    
