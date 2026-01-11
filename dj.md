# Django Complete Course

---

## Getting Started

### What is Django?

- Django is a high-level Python web framework
- Follows the MTV (Model-Template-View) architecture pattern
- Built-in features: admin panel, ORM, authentication, security
- "Batteries included" philosophy - comes with everything you need

**Why Django?**

1. Rapid development
2. Secure by default
3. Scalable architecture
4. Large community and excellent documentation

---

### The Course Prerequisites

- Basic Python knowledge (variables, functions, classes, loops)
- Understanding of HTML/CSS basics
- Familiarity with command line/terminal
- A computer with internet access
- Basic understanding of databases
- Experience with any text editor/IDE

---

---

---

## Django Setup

### Installing Python & Django

**Install Python**

```bash
# Download Python from python.org
# Verify installation
python --version
# or
python3 --version
```

**Create Virtual Environment**

```bash
# Create project folder
mkdir django_course
cd django_course

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

**Install Django**

```bash
pip install django
# Verify installation
django-admin --version
```

---

### Creating a Django Project

```bash
# Create new Django project
django-admin startproject myproject

# Project structure created:
# myproject/
#   ├── manage.py
#   └── myproject/
#       ├── __init__.py
#       ├── settings.py
#       ├── urls.py
#       ├── asgi.py
#       └── wsgi.py
```

---

### Installing an IDE

**Recommended: Visual Studio Code**

1. Download from code.visualstudio.com
2. Install Python extension
3. Install Pylance extension
4. Install autopep8 extension
5. Install Django extension
6. Configure Python interpreter to use virtual environment

```json
// .vscode/settings.json
{
  "python.pythonPath": "/usr/local/bin/python3",
  "window.zoomLevel": 6,
  "python.languageServer": "Pylance"
}
```

---

### Analyzing the Created Project

| File          | Purpose                                            |
| ------------- | -------------------------------------------------- |
| `manage.py`   | Command-line utility for project management        |
| `settings.py` | Project configuration (database, apps, middleware) |
| `urls.py`     | URL routing configuration                          |
| `wsgi.py`     | Web Server Gateway Interface for deployment        |
| `asgi.py`     | Asynchronous Server Gateway Interface              |

---

### Starting a Development Server

```bash
# Navigate to project folder
cd myproject

# Start development server
python manage.py runserver

# Server runs at http://127.0.0.1:8000/
# Press Ctrl+C to stop
```

**Custom Port:**

```bash
python manage.py runserver 8080
```

---

### Django Apps

Apps are modular components of a Django project.

**Creating an App:**

```bash
python manage.py startapp myapp
```

**App Structure:**

```
myapp/
├── __init__.py
├── admin.py      # Admin panel configuration
├── apps.py       # App configuration
├── models.py     # Database models
├── tests.py      # Unit tests
├── views.py      # View functions/classes
└── migrations/   # Database migrations
```

**Registering App in settings.py:**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... other apps
    'myapp',  # Add your app here
]
```

---

## URLs & Views

### Creating a New Project

```bash
# Create fresh project for this module
django-admin startproject urlsviews_project
cd urlsviews_project
python manage.py startapp challenges
```

---

### What are URLs & Views?

**URLs:** Map web addresses to Python functions
**Views:** Python functions that handle requests and return responses

**Flow:**

```text
User Request → URL Pattern → View Function → Response
```

---

### Creating a First View & URL

**Create View (challenges/views.py)**

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Challenges App!")
```

**Create App URLs (challenges/urls.py)**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

**Include in Project URLs (urlsviews_project/urls.py)**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('challenges/', include('challenges.urls')),
]
```

---

### Adding More Views & URLs

```python
# challenges/views.py
def january(request):
    return HttpResponse("January Challenge: Exercise daily!")

def february(request):
    return HttpResponse("February Challenge: Read a book!")

# challenges/urls.py
urlpatterns = [
    path('', views.index, name='index'),
    path('january/', views.january, name='january'),
    path('february/', views.february, name='february'),
]
```

---

### Dynamic Path Segments & Captured Values

```python
# challenges/urls.py
urlpatterns = [
    path('<month>/', views.monthly_challenge, name='monthly-challenge'),
]

# challenges/views.py
def monthly_challenge(request, month):
    return HttpResponse(f"Challenge for {month}")
```

---

### Path Converters

**Available Converters:**

- `str` - Matches any non-empty string (default)
- `int` - Matches positive integers
- `slug` - Matches slug strings (letters, numbers, hyphens, underscores)
- `uuid` - Matches UUID strings
- `path` - Matches any string including slashes

```python
# Examples
path('<str:month>/', views.monthly_challenge),
path('<int:month>/', views.monthly_challenge_by_number),
path('<slug:title>/', views.post_detail),
```

---

### Adding More Dynamic View Logic

```python
from django.http import HttpResponse, HttpResponseNotFound

# challenges/views.py
monthly_challenges = {
    'january': 'Exercise daily for 30 minutes',
    'february': 'Read one book',
    'march': 'Learn something new each day',
    'april': 'Drink at least 2 liters of water daily',
    'may': 'Wake up early every day',
    'june': 'Practice a new skill for 20 minutes daily',
    'july': 'Avoid junk food for the entire month',
    'august': 'Write a daily journal entry',
    'september': 'Learn and revise one topic each day',
    'october': 'Limit social media usage to 30 minutes per day',
    'november': 'Express gratitude by writing one thankful note daily',
    'december': 'Reflect on the year and plan goals for next year',
}

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseNotFound("This month is not supported!")
```

---

### Redirects

```python
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Method 1: HttpResponseRedirect
def old_url(request):
    return HttpResponseRedirect('/challenges/january/')

# Method 2: redirect shortcut (preferred)
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponse("Invalid month", status=404)
    return redirect(f'/challenges/{months[month-1]}/')
```

---

### The Reverse Function & Named URLs

```python
from django.urls import reverse

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    # Using reverse with named URL
    redirect_url = reverse('monthly-challenge', args=[redirect_month])
    return redirect(redirect_url)
```

---

### Returning HTML

```python
def index(request):
    html_content = """
    <html>
        <head><title>Challenges</title></head>
        <body>
            <h1>Monthly Challenges</h1>
            <ul>
                <li><a href="/challenges/january/">January</a></li>
                <li><a href="/challenges/february/">February</a></li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(html_content)
```

```py
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
```

**Dynamic generation of html with list of links**

```py
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
```

---

## Module 4: Templates & Static Files

### 4.2 Adding & Registering Templates

**Create templates folder**

```
challenges/
└── templates/
    └── challenges/
        └── index.html
```

**Register app in settings.py**

```python
INSTALLED_APPS = [
    # ...
    'challenges',
]
```

---

### 4.3 Rendering Templates

```python
# challenges/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'challenges/index.html')
```

---

### 4.4 Template Language & Variable Interpolation

```html
<!-- challenges/templates/challenges/index.html -->
<h1>{{ title }}</h1>
<p>{{ description }}</p>
```

```python
# views.py
def index(request):
    context = {
        'title': 'Monthly Challenges',
        'description': 'Choose your challenge!'
    }
    return render(request, 'challenges/index.html', context)
```

---

### 4.5 Filters

**Common Filters:**

```html
{{ name|title }}
<!-- Capitalizes each word -->
{{ text|truncatewords:30 }}
<!-- Limits to 30 words -->
{{ date|date:"D d M Y" }}
<!-- Date formatting -->
{{ text|default:"N/A" }}
<!-- Default value -->
{{ text|length }}
<!-- String/list length -->
{{ html|safe }}
<!-- Mark as safe HTML -->
```

---

### 4.6 Tags & the "for" Tag

```html
<ul>
  {% for month in months %}
  <li>{{ month }}</li>
  {% empty %}
  <li>No months available</li>
  {% endfor %}
</ul>

<!-- Loop counter -->
{% for item in items %} {{ forloop.counter }} - {{ item }} {% endfor %}
```

---

### 4.7 The URL Tag for Dynamic URLs

```html
<!-- Instead of hardcoding URLs -->
<a href="{% url 'monthly-challenge' month='january' %}">January</a>

<!-- With variable -->
<a href="{% url 'monthly-challenge' month=month_name %}">{{ month_name }}</a>
```

---

### 4.8 The "if" Tag for Conditional Content

```html
{% if user.is_authenticated %}
<p>Welcome, {{ user.username }}!</p>
{% elif user.is_guest %}
<p>Welcome, Guest!</p>
{% else %}
<p>Please log in.</p>
{% endif %}

<!-- Comparison operators -->
{% if score > 90 %}
<p>Excellent!</p>
{% endif %}
```

---

### 4.9 Template Inheritance

**base.html (Parent Template):**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %}My Site{% endblock %}</title>
    {% block css %}{% endblock %}
  </head>
  <body>
    <nav><!-- Navigation --></nav>

    <main>{% block content %}{% endblock %}</main>

    <footer>© 2024</footer>
  </body>
</html>
```

**Child Template:**

```html
{% extends "base.html" %} {% block title %}Home Page{% endblock %} {% block
content %}
<h1>Welcome to our site!</h1>
{% endblock %}
```

---

### 4.10 Including Partial Template Snippets

```html
<!-- _header.html (partial) -->
<header>
  <h1>{{ site_name }}</h1>
</header>

<!-- main template -->
{% include "_header.html" with site_name="My Blog" %}
```

---

### 4.11 404 Templates

**Create templates/404.html:**

```html
{% extends "base.html" %} {% block title %}Page Not Found{% endblock %} {% block
content %}
<h1>404 - Page Not Found</h1>
<p>The page you're looking for doesn't exist.</p>
<a href="{% url 'home' %}">Go Home</a>
{% endblock %}
```

**Note:** Set `DEBUG = False` in settings.py to see custom 404 pages.

---

### 4.12 Adding Static Files

**Step 1: Create static folder**

```
challenges/
└── static/
    └── challenges/
        ├── css/
        │   └── styles.css
        └── images/
            └── logo.png
```

**Step 2: Load in template**

```html
{% load static %}

<link rel="stylesheet" href="{% static 'challenges/css/styles.css' %}" />
<img src="{% static 'challenges/images/logo.png' %}" alt="Logo" />
```

---

### 4.13 Adding Global Static Files

**settings.py:**

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Global static files
]

STATIC_URL = '/static/'
```

## Module 5: Project Blog - Basics

### 5.1 Module Introduction

**Objective:** Build a blog application's frontend structure.

---

### 5.2 Setting Up the Starting Project

```bash
django-admin startproject my_blog
cd my_blog
python manage.py startapp blog
```

**Register in settings.py:**

```python
INSTALLED_APPS = [
    # ...
    'blog',
]
```

---

### 5.3 Planning the Project

**Pages Needed:**

1. **Home Page** - Featured posts
2. **All Posts** - List of all blog posts
3. **Single Post** - Individual post detail
4. **About** - About page

**Data Structure:**

- Title, Author, Date, Image, Excerpt, Content, Slug

---

### 5.4 Adding URLs & Views

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts/', views.posts, name='posts-page'),
    path('posts/<slug:slug>/', views.post_detail, name='post-detail-page'),
]

# blog/views.py
def starting_page(request):
    return render(request, 'blog/index.html')

def posts(request):
    return render(request, 'blog/all-posts.html')

def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')
```

---

### 5.5 Adding First Templates

**Template Structure:**

```
blog/
└── templates/
    └── blog/
        ├── base.html
        ├── index.html
        ├── all-posts.html
        └── post-detail.html
```

---

### 5.6 Template Content & Static Files

**base.html:**

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}My Blog{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'blog/css/base.css' %}" />
    {% block css %}{% endblock %}
  </head>
  <body>
    <header>
      <nav>
        <a href="{% url 'starting-page' %}">Home</a>
        <a href="{% url 'posts-page' %}">All Posts</a>
      </nav>
    </header>
    <main>{% block content %}{% endblock %}</main>
  </body>
</html>
```

---

### 5.7 Adding Dummy Data to Views

```python
# blog/views.py
all_posts = [
    {
        'slug': 'first-post',
        'title': 'My First Post',
        'author': 'John Doe',
        'date': date(2024, 1, 15),
        'image': 'post1.jpg',
        'excerpt': 'This is my first blog post...',
        'content': 'Full content here...'
    },
    # More posts...
]

def starting_page(request):
    latest_posts = sorted(all_posts, key=lambda x: x['date'], reverse=True)[:3]
    return render(request, 'blog/index.html', {'posts': latest_posts})

def posts(request):
    return render(request, 'blog/all-posts.html', {'posts': all_posts})

def post_detail(request, slug):
    post = next((p for p in all_posts if p['slug'] == slug), None)
    if not post:
        raise Http404()
    return render(request, 'blog/post-detail.html', {'post': post})
```

---

### 5.8 Adding a 404 Page

```python
# views.py
from django.http import Http404

def post_detail(request, slug):
    post = get_post_by_slug(slug)
    if not post:
        raise Http404("Post not found")
    return render(request, 'blog/post-detail.html', {'post': post})
```

---

## Module 6: Data & Models

### 6.1 Module Introduction

**Objective:** Master Django's ORM and database operations.

---

### 6.2 Understanding Database Options

**Supported Databases:**

- SQLite (default, file-based)
- PostgreSQL (recommended for production)
- MySQL
- Oracle

---

### 6.3 Django Models

**Models Define:**

- Database table structure
- Field types and constraints
- Relationships between tables

---

### 6.4 Creating a Django Model

```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=300)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
```

**Common Field Types:**
| Field | Description |
|-------|-------------|
| CharField | Short text with max_length |
| TextField | Long text |
| IntegerField | Integer numbers |
| FloatField | Decimal numbers |
| BooleanField | True/False |
| DateField | Date |
| DateTimeField | Date and time |
| EmailField | Email validation |
| SlugField | URL-friendly text |
| ImageField | Image upload |
| FileField | File upload |
| ForeignKey | Many-to-one relationship |

---

### 6.5 Migrations

```bash
# Create migration files
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# View migration SQL
python manage.py sqlmigrate blog 0001
```

---

### 6.6 Inserting Data

```python
# Django shell
python manage.py shell

>>> from blog.models import Post
>>> post = Post(title="Hello", excerpt="...", content="...", slug="hello")
>>> post.save()

# Or using create()
>>> Post.objects.create(title="Hello", excerpt="...", content="...", slug="hello")
```

---

### 6.7 Getting All Entries

```python
>>> Post.objects.all()  # QuerySet of all posts
>>> list(Post.objects.all())  # Evaluate QuerySet
```

---

### 6.8 Updating Data

```python
>>> post = Post.objects.get(id=1)
>>> post.title = "Updated Title"
>>> post.save()

# Bulk update
>>> Post.objects.filter(author='John').update(author='Jane')
```

---

### 6.9 Deleting Data

```python
>>> post = Post.objects.get(id=1)
>>> post.delete()

# Bulk delete
>>> Post.objects.filter(date__lt=date(2020, 1, 1)).delete()
```

---

### 6.10 Querying & Filtering Data

```python
# Get single object
>>> Post.objects.get(slug='hello')

# Filter (returns QuerySet)
>>> Post.objects.filter(author='John')
>>> Post.objects.filter(title__contains='Django')
>>> Post.objects.filter(date__year=2024)

# Exclude
>>> Post.objects.exclude(author='John')

# Chaining
>>> Post.objects.filter(author='John').exclude(date__year=2020)
```

**Field Lookups:**

- `__exact`, `__iexact` - Exact match
- `__contains`, `__icontains` - Contains
- `__startswith`, `__endswith` - String matching
- `__gt`, `__gte`, `__lt`, `__lte` - Comparisons
- `__in` - In list
- `__isnull` - Is null check

---

### 6.11 "or" Conditions

```python
from django.db.models import Q

# OR condition
Post.objects.filter(Q(author='John') | Q(author='Jane'))

# Complex queries
Post.objects.filter(
    Q(author='John') & (Q(title__contains='Django') | Q(title__contains='Python'))
)
```

---

### 6.12 Aggregation & Ordering

```python
from django.db.models import Count, Avg, Sum, Max, Min

# Ordering
Post.objects.order_by('date')  # Ascending
Post.objects.order_by('-date')  # Descending

# Aggregation
Post.objects.aggregate(Avg('rating'))
Post.objects.aggregate(total=Count('id'))
```

---

## Module 7: Admin

### 7.1 Module Introduction

**Objective:** Configure Django's admin panel.

---

### 7.2 Logging Into Admin

```bash
# Create superuser
python manage.py createsuperuser

# Access at http://127.0.0.1:8000/admin/
```

---

### 7.3 Adding Models to Admin

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

---

### 7.4 Configuring Model Fields

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    list_filter = ('date', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-date',)

admin.site.register(Post, PostAdmin)
```

---

### 7.5 More Config Options

```python
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    list_filter = ('date', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'
    list_editable = ('author',)
    list_per_page = 20
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'author')
        }),
        ('Content', {
            'fields': ('excerpt', 'content', 'image')
        }),
    )
```

---

## Module 8: Relationships

### 8.1 Module Introduction

**Objective:** Understand database relationships in Django.

---

### 8.2 Understanding Relationship Types

**Three Types:**

1. **One-to-Many (ForeignKey)** - Author → Many Posts
2. **One-to-One (OneToOneField)** - User → Profile
3. **Many-to-Many (ManyToManyField)** - Posts ↔ Tags

---

### 8.3 One-to-Many Relationship

```python
# models.py
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    # ...
```

**on_delete Options:**

- `CASCADE` - Delete related objects
- `PROTECT` - Prevent deletion
- `SET_NULL` - Set to NULL (requires null=True)
- `SET_DEFAULT` - Set to default value

**Usage:**

```python
>>> author = Author.objects.get(id=1)
>>> author.posts.all()  # All posts by author

>>> post = Post.objects.get(id=1)
>>> post.author  # Get author of post
```

---

### 8.4 One-to-One Relationship

```python
class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
```

---

### 8.5 Many-to-Many Relationship

```python
class Tag(models.Model):
    caption = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=150)
    tags = models.ManyToManyField(Tag, related_name='posts')
```

**Usage:**

```python
>>> post = Post.objects.get(id=1)
>>> post.tags.all()
>>> post.tags.add(tag1, tag2)
>>> post.tags.remove(tag1)
>>> post.tags.clear()

>>> tag = Tag.objects.get(id=1)
>>> tag.posts.all()  # All posts with this tag
```

---

### 8.6 Cross Model Queries

```python
# Get posts by author name
Post.objects.filter(author__first_name='John')

# Get posts with specific tag
Post.objects.filter(tags__caption='Django')
```

---

## Module 9: Forms

### 9.1 Module Introduction

**Objective:** Handle user input through forms.

---

### 9.2 Get & Post Requests

```python
def contact(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'contact.html')
```

---

### 9.3 CSRF Protection

```html
<form method="POST">
  {% csrf_token %}
  <input type="text" name="username" />
  <button type="submit">Submit</button>
</form>
```

---

### 9.4 Using Django Form Class

```python
# forms.py
from django import forms

class ReviewForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    rating = forms.IntegerField(min_value=1, max_value=5)
    review = forms.CharField(widget=forms.Textarea)

# views.py
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Process data
            username = form.cleaned_data['username']
            # ...
            return redirect('success')
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})
```

---

### 9.5 Rendering Forms in Templates

```html
<!-- Method 1: Auto-render all fields -->
<form method="POST">
  {% csrf_token %} {{ form }}
  <button type="submit">Submit</button>
</form>

<!-- Method 2: Render individually -->
<form method="POST">
  {% csrf_token %} {{ form.username.label_tag }} {{ form.username }} {{
  form.username.errors }}
  <!-- ... -->
</form>

<!-- Method 3: As list/table -->
{{ form.as_p }} {{ form.as_ul }} {{ form.as_table }}
```

---

### 9.6 ModelForms

```python
# forms.py
from django.forms import ModelForm
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['username', 'email', 'rating', 'review']
        # or fields = '__all__'
        # exclude = ['created_date']

        widgets = {
            'review': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'username': 'Your Name',
        }

# views.py
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()  # Automatically saves to database
            return redirect('success')
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})
```

---

## Module 10: Class-Based Views

### 10.1 Module Introduction

**Objective:** Use class-based views for cleaner code.

---

### 10.2 TemplateView

```python
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome'
        return context

# urls.py
path('', HomeView.as_view(), name='home'),
```

---

### 10.3 ListView

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 10
```

---

### 10.4 DetailView

```python
from django.views.generic import DetailView

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
```

---

### 10.5 FormView

```python
from django.views.generic.edit import FormView
from .forms import ContactForm

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/success/'

    def form_valid(self, form):
        # Process the form
        return super().form_valid(form)
```

---

### 10.6 CreateView

```python
from django.views.generic.edit import CreateView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'excerpt', 'content']
    template_name = 'posts/create.html'
    success_url = '/posts/'
```

## Module 11: File Upload

### 11.1 Module Introduction

**Objective:** Handle file and image uploads in Django.

---

### 11.2 Setting Up Media Files

**settings.py:**

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'uploads'
```

**urls.py (development only):**

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### 11.3 Adding FileField to Model

```python
# models.py
class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
```

---

### 11.4 Using ImageField

```bash
# Install Pillow for image handling
pip install Pillow
```

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
```

---

### 11.5 File Upload Form

```python
# forms.py
from django import forms

class DocumentForm(forms.Form):
    title = forms.CharField(max_length=200)
    file = forms.FileField()

# views.py
def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle file
            uploaded_file = request.FILES['file']
            # Save logic...
            return redirect('success')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})
```

**Template:**

```html
<form method="POST" enctype="multipart/form-data">
  {% csrf_token %} {{ form }}
  <button type="submit">Upload</button>
</form>
```

---

### 11.6 CreateView for File Upload

```python
from django.views.generic.edit import CreateView
from .models import Document

class DocumentCreateView(CreateView):
    model = Document
    fields = ['title', 'file']
    template_name = 'upload.html'
    success_url = '/documents/'
```

---

### 11.7 Displaying Uploaded Files

```html
{% if document.file %}
<a href="{{ document.file.url }}">Download File</a>
{% endif %} {% if post.image %}
<img src="{{ post.image.url }}" alt="{{ post.title }}" />
{% endif %}
```

---

## Module 12: Sessions

### 12.1 Module Introduction

**Objective:** Manage user sessions and temporary data storage.

---

### 12.2 What are Sessions?

**Sessions allow you to:**

- Store data per visitor
- Persist data across requests
- Track user activity without authentication

---

### 12.3 Enabling Sessions

**settings.py (enabled by default):**

```python
INSTALLED_APPS = [
    # ...
    'django.contrib.sessions',
]

MIDDLEWARE = [
    # ...
    'django.contrib.sessions.middleware.SessionMiddleware',
]

# Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Database-backed
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
```

---

### 12.4 Storing Data in Sessions

```python
def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart.append(product_id)
    request.session['cart'] = cart
    return redirect('cart')
```

---

### 12.5 Using Session Data

```python
def view_cart(request):
    cart = request.session.get('cart', [])
    # Get products from cart
    products = Product.objects.filter(id__in=cart)
    return render(request, 'cart.html', {'products': products})

def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('cart')
```

---

### 12.6 Safely Accessing Session Data

```python
# Safe access with default
cart = request.session.get('cart', [])
username = request.session.get('username', 'Guest')

# Check if key exists
if 'cart' in request.session:
    # ...

# Set with modification flag
request.session['cart'] = ['item1', 'item2']
request.session.modified = True  # Explicitly mark as modified
```

---

## Module 13: Project Blog - Forms, Files & Sessions

### 13.1 Module Introduction

**Objective:** Complete the blog project with forms, file uploads, and sessions.

---

### 13.2 Adding ImageField to Post Model

```python
# blog/models.py
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
```

---

### 13.3 Adding Comment Model

```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
```

---

### 13.4 Adding Comment Form

```python
# forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'user_email', 'text']
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'user_email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'text': forms.Textarea(attrs={'placeholder': 'Your Comment', 'rows': 4}),
        }
        labels = {
            'user_name': 'Name',
            'user_email': 'Email',
            'text': 'Comment',
        }
```

---

### 13.5 Handling Comment Submission

```python
# views.py
from .forms import CommentForm

class PostDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm()
        comments = post.comments.all()
        return render(request, 'blog/post-detail.html', {
            'post': post,
            'form': form,
            'comments': comments
        })

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail-page', slug=slug)

        comments = post.comments.all()
        return render(request, 'blog/post-detail.html', {
            'post': post,
            'form': form,
            'comments': comments
        })
```

---

### 13.6 Displaying Comments

```html
<!-- post-detail.html -->
<section class="comments">
  <h2>Comments ({{ comments|length }})</h2>

  {% for comment in comments %}
  <article class="comment">
    <header>
      <strong>{{ comment.user_name }}</strong>
      <time>{{ comment.created_at|date:"M d, Y" }}</time>
    </header>
    <p>{{ comment.text }}</p>
  </article>
  {% empty %}
  <p>No comments yet. Be the first to comment!</p>
  {% endfor %}
</section>

<section class="comment-form">
  <h2>Leave a Comment</h2>
  <form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button type="submit">Post Comment</button>
  </form>
</section>
```

---

### 13.7 Read Later Feature with Sessions

```python
# views.py
class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('read_later', [])
        posts = Post.objects.filter(id__in=stored_posts)
        return render(request, 'blog/read-later.html', {'posts': posts})

    def post(self, request):
        post_id = request.POST.get('post_id')
        stored_posts = request.session.get('read_later', [])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session['read_later'] = stored_posts
        return redirect(request.META.get('HTTP_REFERER', 'starting-page'))
```

**Template Button:**

```html
<form method="POST" action="{% url 'read-later' %}">
  {% csrf_token %}
  <input type="hidden" name="post_id" value="{{ post.id }}" />
  {% if post.id|stringformat:'i' in stored_posts %}
  <button type="submit">Remove from Read Later</button>
  {% else %}
  <button type="submit">Read Later</button>
  {% endif %}
</form>
```

---

## Module 14: Deployment

### 14.1 Module Introduction

**Objective:** Deploy Django application to production.

---

### 14.2 Deployment Considerations

**Key Areas:**

1. Database (PostgreSQL for production)
2. Static files (CDN or S3)
3. Media files (S3 or cloud storage)
4. Security settings
5. Environment variables

---

### 14.3 Production Settings

**settings.py:**

```python
import os
from pathlib import Path

# Security
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# HTTPS settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

### 14.4 Database Configuration

```python
# settings.py
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# Or manual PostgreSQL config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '5432',
    }
}
```

---

### 14.5 Collecting Static Files

```bash
# settings.py
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Collect all static files
python manage.py collectstatic
```

---

### 14.6 Locking Dependencies

```bash
# Generate requirements file
pip freeze > requirements.txt

# Or use pipenv
pipenv lock

# Or use poetry
poetry export -f requirements.txt > requirements.txt
```

**requirements.txt example:**

```
Django==4.2
gunicorn==21.2.0
psycopg2-binary==2.9.9
whitenoise==6.6.0
dj-database-url==2.1.0
boto3==1.34.0
django-storages==1.14.2
```

---

### 14.7 Using Environment Variables

```python
# settings.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
DATABASE_URL = os.environ.get('DATABASE_URL')
```

**.env file (don't commit!):**

```
SECRET_KEY=your-super-secret-key
DEBUG=False
DATABASE_URL=postgres://user:pass@host:5432/dbname
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
```

---

### 14.8 Serving Static Files with WhiteNoise

```bash
pip install whitenoise
```

```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add after SecurityMiddleware
    # ... other middleware
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

---

### 14.9 Serving Files via S3

```bash
pip install django-storages boto3
```

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'storages',
]

# AWS Settings
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

# Static files on S3
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Media files on S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

---

### 14.10 Deploying with Gunicorn

```bash
pip install gunicorn
```

**Procfile (for Heroku/Railway):**

```
web: gunicorn myproject.wsgi:application
```

**Run locally:**

```bash
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
```

---

### 14.11 Docker Deployment

**Dockerfile:**

```dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
```

**docker-compose.yml:**

```yaml
version: "3.8"

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - DATABASE_URL=postgres://user:pass@db:5432/dbname
    depends_on:
      - db

  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=dbname
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass

volumes:
  postgres_data:
```

---

### 14.12 Deployment Checklist

```bash
# Run Django's deployment check
python manage.py check --deploy
```

**Security Checklist:**

- [ ] DEBUG = False
- [ ] SECRET_KEY from environment variable
- [ ] ALLOWED_HOSTS configured
- [ ] HTTPS enabled
- [ ] Database credentials secured
- [ ] Static files collected
- [ ] Migrations run
- [ ] Admin URL changed (optional)

---

## Quick Reference

### Essential Commands

```bash
# Project Setup
django-admin startproject projectname
python manage.py startapp appname

# Database
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Development
python manage.py runserver
python manage.py shell

# Static Files
python manage.py collectstatic

# Testing
python manage.py test

# Deployment
python manage.py check --deploy
```

### Common Imports

```python
# Views
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

# Models
from django.db import models
from django.db.models import Q, Count, Avg, Sum

# Forms
from django import forms
from django.forms import ModelForm

# Auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
```
