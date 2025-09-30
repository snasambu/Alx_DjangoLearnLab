# Change directory to project
Set-Location "C:\Users\USER\Alx_DjangoLearnLab\django_blog"

# Create templates folder if not exists
$templatesFolder = ".\blog\templates\blog"
if (-not (Test-Path $templatesFolder)) { New-Item -ItemType Directory -Path $templatesFolder -Force }

# ---------------------------
# Write models.py
# ---------------------------
@'
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
'@ | Out-File -FilePath ".\blog\models.py" -Encoding UTF8

# ---------------------------
# Write forms.py
# ---------------------------
@'
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","content"]
'@ | Out-File -FilePath ".\blog\forms.py" -Encoding UTF8

# ---------------------------
# Write views.py
# ---------------------------
@'
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title","content"]
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title","content"]
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = "/posts/"

    def test_func(self):
        return self.request.user == self.get_object().author
'@ | Out-File -FilePath ".\blog\views.py" -Encoding UTF8

# ---------------------------
# Write urls.py
# ---------------------------
@'
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete")
]
'@ | Out-File -FilePath ".\blog\urls.py" -Encoding UTF8

# ---------------------------
# Write Templates
# ---------------------------
@'
{% extends "blog/base.html" %}
{% block title %}All Posts{% endblock %}
{% block content %}
<h2>All Posts</h2>
{% for post in posts %}
<div>
<h3><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h3>
<p>{{ post.content|slice:":200" }}...</p>
</div>
{% endfor %}
{% endblock %}
'@ | Out-File -FilePath "$templatesFolder\post_list.html" -Encoding UTF8

@'
{% extends "blog/base.html" %}
{% block title %}Post Detail{% endblock %}
{% block content %}
<h2>{{ object.title }}</h2>
<p>{{ object.content }}</p>
<p>Author: {{ object.author }}</p>
{% if user == object.author %}
<a href="{% url "post-update" object.pk %}">Edit</a> | 
<a href="{% url "post-delete" object.pk %}">Delete</a>
{% endif %}
{% endblock %}
'@ | Out-File -FilePath "$templatesFolder\post_detail.html" -Encoding UTF8

@'
{% extends "blog/base.html" %}
{% block title %}Post Form{% endblock %}
{% block content %}
<h2>Create/Edit Post</h2>
<form method="post">
{% csrf_token %}
{{ form.as_p }}
<button type="submit">Save</button>
</form>
{% endblock %}
'@ | Out-File -FilePath "$templatesFolder\post_form.html" -Encoding UTF8

@'
{% extends "blog/base.html" %}
{% block title %}Delete Post{% endblock %}
{% block content %}
<h2>Delete Post</h2>
<p>Are you sure you want to delete "{{ object.title }}"?</p>
<form method="post">
{% csrf_token %}
<button type="submit">Yes, delete</button>
</form>
{% endblock %}
'@ | Out-File -FilePath "$templatesFolder\post_confirm_delete.html" -Encoding UTF8

# ---------------------------
# Django Migrations
# ---------------------------
python manage.py makemigrations
python manage.py migrate

# ---------------------------
# Git Commit & Push
# ---------------------------
git add .
git commit -m "Add blog CRUD features"
git push --set-upstream origin main
