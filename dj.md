# Django Complete Course

![Bidur Sapkota](https://www.bidursapkota.com.np/images/gravatar.webp "Bidur Sapkota - Developer")&nbsp;[Bidur Sapkota](https://www.bidursapkota.com.np/)

![Django Complete Guide by Bidur Sapkota](/images/unit-3/13-django-post-1200.webp "Django Complete Guide – Blog by Bidur Sapkota")

## Table of Content

- [MVC Architecture](#mvc-architecture)
- [Role of Backend](#role-of-backend)
- [Django](#django)
- [Django Setup](#django-setup)
- [URLs & Views](#urls--views)
- [Templates & Static Files](#templates--static-files)

---

## MVC Architecture

### What is MVC?

MVC (Model-View-Controller) is a software architectural pattern that separates an application into three interconnected components. This separation helps organize code, making it easier to develop, test, and maintain applications.

MVC was originally developed for desktop applications but has become the foundation for most modern web frameworks. It promotes the principle of **"separation of concerns"** — each component has a specific job and should not interfere with the responsibilities of others.

#### Model (The Data Layer)

The Model represents the data and the business logic of the application. It is responsible for:

- **Data Storage**: Managing how data is stored, retrieved, and updated
- **Business Rules**: Enforcing the rules and logic of the application
- **Data Validation**: Ensuring data integrity before saving
- **Database Communication**: Interacting with databases to persist data

The Model is completely independent of the user interface. It doesn't know or care how data will be displayed — it only focuses on data management.

**Responsibilities of Model:**

- Define data structures (tables, fields, relationships)
- Validate data before saving
- Perform database queries
- Implement business logic (calculations, rules)
- Notify controllers/views when data changes

---

#### View (The Presentation Layer)

The View is responsible for displaying data to the user. It is the visual representation of the Model's data and handles:

- **Data Display**: Presenting information in a user-friendly format
- **User Interface**: Rendering HTML, CSS, and visual elements
- **Templates**: Using template engines to generate dynamic content
- **No Business Logic**: Views should only display, never process data

The View receives data from the Controller and renders it. It should be passive and not directly access the Model.

**Responsibilities of View:**

- Render HTML templates
- Display data from the Model
- Format data for presentation
- Handle visual layout and styling
- Generate responses (HTML, JSON, XML)

---

#### Controller (The Logic Layer)

The Controller acts as an intermediary between the Model and View. It:

- **Handles User Input**: Receives requests from users
- **Processes Requests**: Interprets what the user wants to do
- **Coordinates Flow**: Decides which Model to use and which View to render
- **Updates Model**: Instructs the Model to update data
- **Selects View**: Chooses the appropriate View for the response

The Controller is the "traffic cop" of the application, directing the flow of data between components.

**Responsibilities of Controller:**

- Receive HTTP requests
- Parse and validate user input
- Call appropriate Model methods
- Pass data to Views
- Return HTTP responses

![MVC Diagram](/images/unit-3/mvc.webp)

#### Detailed Request-Response Cycle

1. **User Action**: User clicks a link or submits a form
2. **Request Sent**: Browser sends HTTP request to server
3. **Routing**: Server routes request to appropriate Controller
4. **Controller Processing**: Controller receives request, validates input
5. **Model Interaction**: Controller calls Model methods to get/modify data
6. **Data Processing**: Model performs database operations, applies business rules
7. **Data Return**: Model returns data to Controller
8. **View Selection**: Controller selects appropriate View
9. **View Rendering**: View receives data and generates HTML
10. **Response Sent**: HTML sent back to user's browser
11. **Display**: Browser renders the page for user

#### Benefits of MVC Architecture

| Benefit                    | Description                                                              |
| -------------------------- | ------------------------------------------------------------------------ |
| **Separation of Concerns** | Each component has a single responsibility, making code cleaner          |
| **Maintainability**        | Changes in one component don't affect others                             |
| **Testability**            | Each component can be tested independently                               |
| **Parallel Development**   | Frontend and backend developers can work simultaneously                  |
| **Reusability**            | Models and Views can be reused across different parts of the application |
| **Scalability**            | Easier to scale individual components                                    |
| **Code Organization**      | Clear structure makes codebase easier to navigate                        |

#### MVC in Different Frameworks

| Framework     | Language   | MVC Implementation           |
| ------------- | ---------- | ---------------------------- |
| Django        | Python     | MTV (Model-Template-View)    |
| Ruby on Rails | Ruby       | Traditional MVC              |
| ASP.NET MVC   | C#         | Traditional MVC              |
| Spring MVC    | Java       | Traditional MVC              |
| Laravel       | PHP        | Traditional MVC              |
| Express.js    | JavaScript | Flexible (can implement MVC) |

#### Simple MVC Example

```python
# eg
```

---

---

---

## Role of Backend

#### What is Backend?

The backend (also called server-side) is the part of a web application that users don't see. It runs on the server and handles:

- Processing user requests
- Managing databases
- Running business logic
- Authenticating users
- Sending responses to the frontend

While the frontend is what users interact with (buttons, forms, colors), the backend is what makes everything actually work behind the scenes.

#### Frontend vs Backend

| Frontend                                            | Backend                                                      |
| --------------------------------------------------- | ------------------------------------------------------------ |
| Runs in the user’s browser.                         | Runs on the web server.                                      |
| Uses languages such as HTML, CSS, and JavaScript.   | Uses languages such as Python, Java, PHP, Ruby, and Node.js. |
| Is visible to the user and allows interaction.      | Is hidden from the user.                                     |
| Focuses on building the user interface.             | Handles data processing and application logic.               |
| Includes elements like buttons, forms, and layouts. | Includes databases, APIs, and authentication systems.        |

---

#### Core Responsibilities of Backend

#### 1. Server Logic

The server is a computer that:

- **Listens** for incoming requests from clients
- **Processes** those requests
- **Sends** appropriate responses back

**How servers work:**

1. Server runs continuously, listening on a port (e.g., port 80 or 443)
2. When a request arrives, server creates a new thread/process to handle it
3. Request is processed and response is generated
4. Response is sent back to the client
5. Connection may be kept open or closed

![HTTP](/images/unit-3/http.webp)

#### 2. Routing

Routing is the process of determining what code should run based on the URL requested. It maps URLs to specific functions or handlers.

**Why routing matters:**

- `/home` → Show homepage
- `/products` → Show product list
- `/products/123` → Show product with ID 123
- `/login` → Show login form
- `/api/users` → Return user data as JSON

**Types of routes:**

- **Static routes**: Exact URL match (`/about`, `/contact`)
- **Dynamic routes**: URLs with variables (`/users/<id>`, `/products/<category>`)
- **Wildcard routes**: Catch-all patterns (`/blog/*`)

**Route parameters:**

- **Path parameters**: `/users/123` (123 is the user ID)
- **Query parameters**: `/search?q=python&page=2`

#### 3. Business Logic

Business logic is the code that implements the rules and operations specific to your application. It's the "brain" of your application.

**Examples of business logic:**

- Calculating total price with discounts
- Checking if user has permission to perform an action
- Validating that email addresses are unique
- Processing payment transactions
- Generating reports from data

**Business logic should:**

- Be separate from presentation (Views)
- Be testable in isolation
- Be reusable across different interfaces
- Handle edge cases and errors

**Example business rules:**

```text
- Users must be 18+ to register
- Orders over $100 get free shipping
- Passwords must be at least 8 characters
- Users can only edit their own posts
- Maximum 5 items per cart
```

#### 4. Security Layers

Security is critical for backend applications. Multiple layers protect the application:

**a) Authentication (Who are you?)**

- Verifying user identity
- Login systems (username/password)
- Multi-factor authentication
- OAuth/Social login

**b) Authorization (What can you do?)**

- Checking user permissions
- Role-based access control (Admin, User, Guest)
- Resource ownership verification

**c) Input Validation**

- Sanitizing user input
- Preventing SQL injection
- Preventing XSS (Cross-Site Scripting)
- Validating data types and formats

**d) Data Protection**

- Encrypting sensitive data
- Hashing passwords (never store plain text!)
- HTTPS for data in transit
- Secure session management

**e) CSRF Protection**

- Preventing cross-site request forgery
- Using CSRF tokens in forms

**f) Rate Limiting**

- Preventing brute force attacks
- Limiting API requests per user

---

---

---

## Django

Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.

**Django's Philosophy:**

- **"Batteries included"**: Comes with everything you need out of the box
- **DRY (Don't Repeat Yourself)**: Encourages code reuse
- **Rapid Development**: Build applications quickly
- **Security First**: Protects against common vulnerabilities

#### Why Choose Django?

| Feature                             | Benefit                                      |
| ----------------------------------- | -------------------------------------------- |
| **Built-in Admin Panel**            | Automatic admin interface for managing data  |
| **ORM (Object-Relational Mapping)** | Work with databases using Python, not SQL    |
| **Security**                        | Protection against SQL injection, XSS, CSRF  |
| **Scalability**                     | Powers large sites like Instagram, Pinterest |
| **Large Community**                 | Extensive documentation and packages         |
| **Authentication System**           | Built-in user management                     |

### MTV Pattern (Django's Version of MVC)

Django uses **MTV (Model-Template-View)** pattern, which is similar to MVC but with different naming:

| MVC        | Django MTV   | Role                                |
| ---------- | ------------ | ----------------------------------- |
| Model      | **Model**    | Data structure and database         |
| View       | **Template** | HTML presentation                   |
| Controller | **View**     | Business logic and request handling |

- In Django, a "View" is a Python function/class that handles requests (like a Controller)
- A "Template" is the HTML file that displays data (like a View in MVC)

![alt text](/images/unit-3/mtv.webp)

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
```

When you create a Django project, the following structure is generated:

```text
myproject/                 # Root directory (any name)
│
├── manage.py             # Command-line utility for Django
│
├── myproject/            # Project package (same name as root)
│   ├── __init__.py       # Makes this a Python package
│   ├── settings.py       # Project configuration
│   ├── urls.py           # Main URL routing
│   ├── asgi.py           # Asynchronous Server Gateway Interface (ASGI) configuration
│   └── wsgi.py           # Web Server Gateway Interface (WSGI) configuration
│
```

#### Key Files

#### 1. manage.py

The command-line tool for interacting with Django:

```bash
python manage.py runserver     # Start development server
python manage.py makemigrations # Create migration files
python manage.py migrate       # Apply migrations to database
python manage.py createsuperuser # Create admin user
```

#### 2. settings.py

Contains all project configuration:

- Database settings
- Installed apps
- Middleware
- Templates configuration
- Static files settings
- Security settings

#### 3. urls.py

Maps URLs to views:

```python
# eg
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
]
```

#### 4. models.py

Defines database structure:

```python
# eg
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

#### 5. views.py

Handles request processing:

```python
# eg
from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})
```

<!-- more -->

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
  "python.languageServer": "Pylance"
}
```

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

A Django project can contain multiple apps. An app is a web application that does something specific.

**Project vs App:**

- **Project**: The entire website (configuration, settings)
- **App**: A specific feature/module (blog, users, products)

**Example structure with multiple apps:**

```
myproject/
├── manage.py
├── myproject/          # Project settings
├── blog/               # Blog app
├── users/              # User management app
├── products/           # E-commerce app
└── api/                # REST API app
```

**Creating an App:**

```bash
python manage.py startapp myapp
```

**App Structure:**

```text
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
    'blog',    # Another custom app
    'users',   # Another custom app
]
```

**Complete Project and App Structure**

```text
myproject/                 # Root directory (any name)
│
├── manage.py             # Command-line utility for Django
│
├── myproject/            # Project package (same name as root)
│   ├── __init__.py       # Makes this a Python package
│   ├── settings.py       # Project configuration
│   ├── urls.py           # Main URL routing
│   ├── asgi.py           # ASGI configuration (async)
│   └── wsgi.py           # WSGI configuration (deployment)
│
└── myapp/                # Your application (created separately)
    ├── __init__.py       # Makes this a Python package
    ├── admin.py          # Admin panel configuration
    ├── apps.py           # App configuration
    ├── models.py         # Database models
    ├── views.py          # View functions/classes
    ├── urls.py           # App-specific URL routing
    ├── tests.py          # Unit tests
    └── migrations/       # Database migration files
        └── __init__.py
```

**Simple Complete Django Setup Steps**

```python
# 1. Install Django
# pip install django

# 2. Create project
# django-admin startproject mysite

# 3. Create app
# cd mysite
# python manage.py startapp blog

# 4. Register app in settings.py
# Add 'blog' to INSTALLED_APPS

# 5. Run server
# python manage.py runserver
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

#### What is Routing?

Routing is the mechanism that maps URLs to specific code (views/controllers). When a user visits a URL, the routing system determines which function should handle the request.

#### What are URLs & Views?

**URL Dispatcher**

Django uses a URL dispatcher defined in `urls.py` files. It matches incoming URLs against patterns and calls the corresponding view.

**How URL matching works:**

1. Request comes in with a URL (e.g., `/articles/5/`)
2. Django checks patterns in order from top to bottom
3. First matching pattern wins
4. Associated view function is called
5. View returns a response

**URLs:** Maps web addresses (URLs) to views
**Views:** Python function or class that receives a web request and returns a web response. Views contain the logic that processes requests.

---

#### Basic URL Configuration

**Project-level urls.py:**

```python
# eg
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Include app URLs
    path('api/', include('api.urls')),
]
```

**App-level urls.py (blog/urls.py):**

```python
# eg
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
]
```

#### Functional View

```python
# eg
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!")
```

**The request object contains:**

- `request.method` - HTTP method (GET, POST, etc.)
- `request.GET` - Query parameters dictionary
- `request.POST` - POST data dictionary
- `request.body` - Raw request body
- `request.headers` - HTTP headers
- `request.user` - Currently logged-in user
- `request.session` - Session data

---

### Handling Different HTTP Methods

```python
# eg
from django.http import HttpResponse

def article_view(request):
    if request.method == 'GET':
        return HttpResponse("Showing articles")

    elif request.method == 'POST':
        return HttpResponse("Creating article")

    elif request.method == 'DELETE':
        return HttpResponse("Deleting article")
```

### URL Configuration

Connect URLs to views in **urls.py**:

```python
# eg
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.article_list, name='articles'),
    path('articles/<int:id>/', views.article_detail, name='article_detail'),
]
```

### Accessing URL Parameters

```python
# eg
def article_detail(request, id):
    # id is automatically passed from the URL
    return HttpResponse(f"Article ID: {id}")
```

---

### Query Parameters

Access GET parameters from the URL:

```python
# eg
# URL: /search/?q=python&page=2

def search(request):
    query = request.GET.get('q', '')       # 'python'
    page = request.GET.get('page', '1')    # '2'
    return HttpResponse(f"Searching: {query}, Page: {page}")
```

---

### Path Converters

```python
# eg
from django.urls import path

urlpatterns = [
    # Integer parameter
    path('article/<int:id>/', views.article_detail),

    # String parameter
    path('category/<str:name>/', views.category_view),

    # Slug parameter (letters, numbers, hyphens, underscores)
    path('post/<slug:slug>/', views.post_detail),

    # Multiple parameters
    path('archive/<int:year>/<int:month>/', views.archive),
]
```

**In views:**

```python
# eg
def article_detail(request, id):
    # id is automatically converted to integer
    return HttpResponse(f"Article {id}")

def archive(request, year, month):
    return HttpResponse(f"Archive: {year}/{month}")
```

---

### Named URLs

Give URLs names for easy referencing:

```python
# eg
path('articles/', views.article_list, name='article_list'),
path('articles/<int:id>/', views.article_detail, name='article_detail'),
```

**Using named URLs in templates:**

```html
<a href="{% url 'article_list' %}">All Articles</a>
<a href="{% url 'article_detail' id=5 %}">Article 5</a>
```

**Using named URLs in views:**

```python
# eg
from django.urls import reverse
from django.shortcuts import redirect

def my_view(request):
    url = reverse('article_detail', args=[5])  # '/articles/5/'
    return redirect('article_list')  # Redirect by name
```

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

Give URLs names for easy referencing:

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

---

---

## Templates & Static Files

Templating is the process of generating dynamic HTML by combining a template (HTML structure) with data. Templates separate presentation from logic.

---

### Django Template Language (DTL)

Django's template language allows you to:

- Insert dynamic data with `{{ variable }}`
- Use logic with `{% tag %}`
- Apply filters with `{{ variable|filter }}`

---

A Django template is a text file (usually HTML) that contains static content mixed with Django Template Language (DTL) to dynamically display data sent from a view.

### Template Variables

Output data using double curly braces:

```html
<!-- eg -->
<h1>{{ title }}</h1>
<p>Welcome, {{ user.username }}!</p>
<p>You have {{ message_count }} messages.</p>
```

**Accessing nested data:**

```html
<!-- eg -->
{{ user.profile.avatar }} {{ article.author.name }} {{ items.0 }}
<!-- First item in list -->
```

---

### Template Tags

Control logic using `{% tag %}`:

**If/Else:**

```html
<!-- eg -->
{% if user.is_authenticated %}
<p>Welcome back, {{ user.username }}!</p>
{% else %}
<p>Please <a href="/login/">log in</a>.</p>
{% endif %}
```

**For Loop:**

```html
<!-- eg -->
<ul>
  {% for article in articles %}
  <li>{{ article.title }}</li>
  {% empty %}
  <li>No articles found.</li>
  {% endfor %}
</ul>
```

**Loop variables:**

```html
<!-- eg -->
{% for item in items %} {{ forloop.counter }}
<!-- 1, 2, 3, ... -->
{{ forloop.counter0 }}
<!-- 0, 1, 2, ... -->
{{ forloop.first }}
<!-- True if first iteration -->
{{ forloop.last }}
<!-- True if last iteration -->
{% endfor %}
```

---

### Template Filters

Transform data using `|filter`:

```html
<!-- eg -->
{{ name|upper }}
<!-- JOHN -->
{{ name|lower }}
<!-- john -->
{{ name|title }}
<!-- John Doe -->
{{ text|truncatewords:20 }}
<!-- First 20 words... -->
{{ date|date:"Y-m-d" }}
<!-- 2026-01-17 -->
{{ price|floatformat:2 }}
<!-- 19.99 -->
{{ list|length }}
<!-- 5 -->
{{ value|default:"N/A" }}
<!-- Shows "N/A" if empty -->
{{ html_content|safe }}
<!-- Renders HTML (careful!) -->
```

---

### Template Inheritance

Create a base template and extend it:

**base.html:**

```html
<!-- eg -->
<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %}My Site{% endblock %}</title>
  </head>
  <body>
    <nav>
      <a href="/">Home</a>
      <a href="/about/">About</a>
    </nav>

    <main>{% block content %}{% endblock %}</main>

    <footer>&copy; 2026 My Site</footer>
  </body>
</html>
```

**home.html:**

```html
<!-- eg -->
{% extends "base.html" %} {% block title %}Home - My Site{% endblock %} {% block
content %}
<h1>Welcome to My Site</h1>
<p>This is the homepage.</p>
{% endblock %}
```

---

### Including Templates

Reuse template fragments:

**navbar.html:**

```html
<!-- eg -->
<nav>
  <a href="/">Home</a>
  <a href="/about/">About</a>
</nav>
```

**page.html:**

```html
<!-- eg -->
{% include "navbar.html" %}

<h1>Page Content</h1>
```

**Passing variables to includes:**

```html
<!-- eg -->
{% include "card.html" with title="My Card" content="Card content" %}
```

---

```html
<!-- eg -->
<h1>Hello {{ user_name }}</h1>
```

```py
# eg
from django.shortcuts import render

def hello_view(request):
    context = {
        'user_name': 'Bidur'
    }
    return render(request, 'hello.html', context)
```

### JSON Responses

- For APIs, return JSON instead of HTML.
- By default, `JsonResponse` expects a dictionary.

```python
# eg
from django.http import JsonResponse

def api_articles(request):
    data = {
        'articles': [
            {'id': 1, 'title': 'First'},
            {'id': 2, 'title': 'Second'},
        ],
        'count': 2
    }
    return JsonResponse(data)
```

**Response:**

```json
// eg
{
  "articles": [
    { "id": 1, "title": "First" },
    { "id": 2, "title": "Second" }
  ],
  "count": 2
}
```

### Setting Custom Status Codes

```python
# eg
from django.http import HttpResponse, JsonResponse

def custom_status(request):
    return HttpResponse("Created!", status=201)

def json_error(request):
    return JsonResponse({'error': 'Bad request'}, status=400)
```

---

### Complete View Example

```python
# eg
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

def article_api(request, id=None):
    """Handle article CRUD operations"""

    if request.method == 'GET':
        if id:
            # Return single article
            return JsonResponse({'id': id, 'title': 'Sample'})
        else:
            # Return all articles
            return JsonResponse({'articles': []})

    elif request.method == 'POST':
        # Create new article
        return JsonResponse({'message': 'Created'}, status=201)

    elif request.method == 'DELETE':
        if id:
            # Delete article
            return JsonResponse({'message': 'Deleted'})
        return JsonResponse({'error': 'ID required'}, status=400)

    # Method not allowed
    return HttpResponse(status=405)
```

### Template Directory Structure

```
myproject/
├── templates/              # Project-wide templates
│   ├── base.html
│   └── navbar.html
│
├── blog/
│   └── templates/
│       └── blog/           # App-specific templates
│           ├── post_list.html
│           └── post_detail.html
│
└── users/
    └── templates/
        └── users/
            ├── login.html
            └── profile.html
```

**Summary**

| Concept           | Description                                     |
| ----------------- | ----------------------------------------------- |
| **HTTP Request**  | Message from client to server                   |
| **HTTP Response** | Message from server to client                   |
| **HTTP Methods**  | GET, POST, PUT, PATCH, DELETE                   |
| **Status Codes**  | 2xx success, 4xx client error, 5xx server error |
| **View**          | Python function/class handling requests         |
| **render()**      | Returns HTML from template                      |
| **JsonResponse**  | Returns JSON data                               |
| **redirect()**    | Sends user to different URL                     |

### Adding & Registering Templates

**Create templates folder**

```text
challenges/
└── templates/
    └── challenges/
        └── challenge.html
```

**Register app in settings.py**

```python
INSTALLED_APPS = [
    # ...
    'challenges',
]
```

---

### Challenge Template

**Add content in `challenges/templates/challenges/challenge.html`**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>This Month's Challenge</h1>
    <h2>Challenge text</h2>
  </body>
</html>
```

### Rendering Templates

**Using render_to_string**

```py
# challenges/views.py
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
```

**Using render**

```python
# challenges/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return render(request, "challenges/challenge.html")
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
```

---

### Template Language & Variable Interpolation

```html
<!-- challenges/templates/challenges/challenge.html -->
<h1>This Month's Challenge</h1>
<h2>{{ text }}</h2>
```

```python
# challenges/views.py
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
```

**Adding month name too**

```html
<head>
  <title>{{ month_name }} Challenge</title>
</head>
<body>
  <h1>{{ month_name }} Challenge</h1>
  <h2>{{ text }}</h2>
</body>
```

```py
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
```

---

### Filters

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

```html
<head>
  <title>{{ month_name|title }} Challenge</title>
</head>
<body>
  <h1>{{ month_name|title }} Challenge</h1>
  <h2>{{ text }}</h2>
</body>
```

---

### Tags & the "for" Tag

**First, update index view with template**

**Create `challenges/templates/challenges/index.html` template**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>All Challenges</title>
  </head>
  <body>
    <ul>
      <li><a href="/challenges/january">January</a></li>
      <li><a href="/challenges/february">February</a></li>
      <li><a href="/challenges/march">March</a></li>
      <li><a href="/challenges/april">April</a></li>
      <li><a href="/challenges/may">May</a></li>
      <li><a href="/challenges/june">June</a></li>
      <li><a href="/challenges/july">July</a></li>
      <li><a href="/challenges/august">August</a></li>
      <li><a href="/challenges/september">September</a></li>
      <li><a href="/challenges/october">October</a></li>
      <li><a href="/challenges/november">November</a></li>
      <li><a href="/challenges/december">December</a></li>
    </ul>
  </body>
</html>
```

```py
# challenges/views.py
def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })
```

```html
<!-- challenges/templates/challenges/index.html -->
<ul>
  {% for month in months %}
  <li>
    <a href="/challenges/{{month}}">
      {{ forloop.counter }} - {{ month|title }}
    </a>
  </li>
  {% endfor %}
</ul>
```

---

### The URL Tag for Dynamic URLs

```html
<!-- challenges/templates/challenges/index.html -->
<ul>
  {% for month in months %}
  <li>
    <a href="{% url 'monthly-challenge' month %}">
      {{ forloop.counter }} - {{ month|title }}
    </a>
  </li>
  {% endfor %}
</ul>
```

---

### The "if" Tag for Conditional Content

**Update monthly challenge dictionary**

```py
# challenges/views.py
monthly_challenges = {
    'january': 'Exercise daily for 30 minutes',
    # ...
    'december': None
}
```

```html
<!-- challenges/templates/challenges/challenge.html -->
<h1>{{ month_name|title }} Challenge</h1>
{% if text is not None %}
<h2>{{ text }}</h2>
{% else %}
<p>There is no challenge for this month yet!</p>
{% endif %}
```

---

### Template Inheritance

**Update settings.py to add global templates folder location**

```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
        ],
        'APP_DIRS': True,
        # ...
    }
]
```

**Create `templates/base.html` (Parent Template):**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block page_title %}My Challenges{% endblock %}</title>
  </head>
  <body>
    {% block content %}{% endblock %}
  </body>
</html>
```

**Child Template:**

```html
<!-- challenges\templates\challenges\index.html -->
<!-- pre tag is not required, just for proper blog format -->
<pre>
{% extends "base.html" %}

{% block page_title %}
  All Challenges
{% endblock %}

{% block content %}
  <ul>
    {% for month in months %}
      <li><a href="{% url 'monthly-challenge' month %}">{{ month|title }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
</pre>
```

```html
<!-- challenges\templates\challenges\challenge.html -->
<pre>
{% extends "base.html" %}

{% block page_title %}
  {{ month_name|title }} Challenge
{% endblock %}
  
{% block content %}
  <h1>{{ month_name|title }} Challenge</h1>
  {% if text is not None %}
    <h2>{{ text }}</h2>
  {% else %}
    <p>There is no challenge for this month yet!</p>
  {% endif %}
{% endblock %}
</pre>
```

---

### Including Partial Template Snippets

**Create `challenges\templates\challenges\includes\header.html`**

```html
<header>
  <nav>
    <a href="{% url "index" %}">All Challenges</a>
  </nav>
</header>
```

**Add include header to both index and challenge template**

```html
<pre>
{% block content %}
  {% include "challenges/includes/header.html" %}
  <!-- ... -->
{% endblock %}
</pre>
```

---

### 404 Templates

**Create `templates/404.html`:**

```html
<pre>
{% extends "base.html" %}

{% block page_title %}
  Something went wrong - we could not find that page!
{%endblock%}

{% block content %}
  <h1>We could not find that page!</h1>
  <p>Sorry, but we could not find a matching page!</p>
{% endblock %}
</pre>
```

```py
from django.http import Http404

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
```

**Note:** Set `DEBUG = False` and `ALLOWED_HOSTS = ['*']` in settings.py to see custom 404 pages.

---

### Adding Static Files

**Create static folder**

```text
challenges/
└── static/
    └── challenges/
        ├── css/
        │   └── challenges.css
        └── images/
            └── logo.png
```

**Load in template**

```css
/* challenges\static\challenges\css\challenges.css */
ul {
  list-style: none;
}
```

```html
<!-- templates\base.html -->
<head>
  {% block css_files %}{% endblock %}
</head>
```

```html
<!-- challenges\templates\challenges\index.html -->
<pre>
{% load static %}

{% block css_files %}
  <link rel="stylesheet" href="{% static 'challenges/css/challenges.css' %}">
{% endblock %}
</pre>
```

---

### Adding Global Static Files

**settings.py:**

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Global static files
]
```

**Create `static\styles.css`**

```css
@import url("https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@400;700&display=swap");

html {
  font-family: "Roboto Condensed", sans-serif;
}

body {
  margin: 0;
  background-color: #1a1a1a;
}
```

```html
<!-- templates\base.html -->
<pre>
{% load static %}

<head>
    <link rel="stylesheet" href="{% static "styles.css" %}">
    {% block css_files %}{% endblock %}
</head>
</pre>
```

### More CSS

**Create `challenges\static\challenges\includes\header.css`**

```css
header {
  width: 100%;
  height: 5rem;
  background-color: #353535;
}

header nav {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

header nav a {
  color: white;
  font-size: 2rem;
  font-weight: bold;
  text-decoration: none;
}

header nav a:hover,
header nav a:active {
  color: #cf54a6;
}
```

**Create `challenges\static\challenges\css\challenge.css`**

```css
h1,
h2 {
  text-align: center;
  color: white;
}

h1 {
  font-size: 1.5rem;
  margin: 2rem 0 1rem 0;
  font-weight: normal;
  color: #cf54a6;
}

h2 {
  font-size: 3rem;
  font-weight: bold;
}

.fallback {
  text-align: center;
  color: white;
}
```

**Update `challenges\static\challenges\css\challenges.css`**

```css
ul {
  list-style: none;
  margin: 2rem auto;
  width: 90%;
  max-width: 20rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 1rem;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  height: 30rem;
  background-color: #eeeeee;
}

li {
  margin: 1rem 0;
  text-align: center;
  font-size: 1.5rem;
  border-bottom: 1px solid #ccc;
  padding-bottom: 1rem;
}

li:last-of-type,
li:nth-of-type(6) {
  border-bottom: none;
}

li a {
  text-decoration: none;
  color: #383838;
}

li a:hover,
li a:active {
  color: #7e0154;
}
```

**Update `challenges\templates\challenges\challenge.html`**

```html
<pre>
{% extends "base.html" %}
{% load static %}

{% block css_files %}
  <link rel="stylesheet" href="{% static "challenges/challenge.css" %}">
  <link rel="stylesheet" href="{% static "challenges/includes/header.css" %}">
{% endblock %}
</pre>
```

**Update `challenges\templates\challenges\index.html`**

```html
<pre>
{% extends "base.html" %}
{% load static %}

{% block css_files %}
  <link rel="stylesheet" href="{% static "challenges/challenges.css" %}">
  <link rel="stylesheet" href="{% static "challenges/includes/header.css" %}">
{% endblock %}
</pre>
```

---

---

---

## Data and Models

### What is ORM?

ORM (Object-Relational Mapping) is a technique that lets you work with databases using your programming language's objects instead of writing SQL queries.

**Benefits of ORM:**

- Write Python (or other language) instead of SQL
- Database-agnostic code
- Automatic SQL injection protection
- Easier to maintain and read
- Object-oriented database access

**How ORM Works:**

![Class to Table Mapping](/images/unit-3/class-to-table-mapping.webp)

**Supported Databases:**

- SQLite (default, file-based)
- PostgreSQL (recommended for production)
- MySQL
- Oracle

**Create fresh project**

```bash
# Create fresh project for this module
django-admin startproject book_store
cd book_store
python manage.py startapp book_outlet
```

**Register in settings.py:**

```python
INSTALLED_APPS = [
    # ...
    'book_outlet',
]
```

### Django ORM

Django includes a powerful built-in ORM. You define models as Python classes, and Django handles the database operations.

**Defining Models**

Models are defined in `models.py`:

```py
from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=50)
  rating = models.IntegerField()
```

**Equivalent to sql below after we migrate**

```sql
CREATE TABLE books (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  rating INTEGER NOT NULL
)
```

**Create file `db.sqlite3` if not present already.**

---

### Common Field Types

| Field Type        | Description                      | Example                               |
| ----------------- | -------------------------------- | ------------------------------------- |
| `CharField`       | Short text (requires max_length) | `name = CharField(max_length=100)`    |
| `TextField`       | Long text                        | `bio = TextField()`                   |
| `IntegerField`    | Integer numbers                  | `age = IntegerField()`                |
| `FloatField`      | Decimal numbers                  | `price = FloatField()`                |
| `BooleanField`    | True/False                       | `active = BooleanField(default=True)` |
| `DateField`       | Date only                        | `birth_date = DateField()`            |
| `DateTimeField`   | Date and time                    | `created_at = DateTimeField()`        |
| `EmailField`      | Email validation                 | `email = EmailField()`                |
| `URLField`        | URL validation                   | `website = URLField()`                |
| `ForeignKey`      | Many-to-one relationship         | `author = ForeignKey(Author)`         |
| `ManyToManyField` | Many-to-many relationship        | `tags = ManyToManyField(Tag)`         |

---

### Field Options

| Option         | Description                          |
| -------------- | ------------------------------------ |
| `max_length`   | Maximum length for CharField         |
| `default`      | Default value for the field          |
| `null=True`    | Allow NULL in database               |
| `blank=True`   | Allow empty in forms                 |
| `unique=True`  | Enforce unique values                |
| `choices`      | Limit to specific choices            |
| `auto_now_add` | Set to current time on creation      |
| `auto_now`     | Update to current time on every save |

---

### Migrations

After defining/changing models, you need to create and apply migrations:

```bash
# Create migration files based on model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

**What migrations do:**

1. Detect changes in your models
2. Generate SQL to update the database
3. Keep track of database schema versions
4. Allow reverting changes

**Open Django Shell**

```bash
python3 manage.py shell
```

**Create Book**

```py
from book_outlet.models import Book
harry_potter = Book(title="Harry Potter 1 – The Philosopher's Stone", rating=5)
harry_potter.save()
```

**Equivalent to:**

```sql
INSERT INTO books ( title, rating )
VALUES ('Lord of the Rings', 5)
```

```py
lord_of_the_rings = Book(title="Lord of the Rings", rating=4)
lord_of_the_rings.save()
```

**Read Book**

```py
Book.objects.all()
# <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>
```

**Equivalent to:**

```sql
SELECT * FROM books;
```

---

**Add more attributes and str method**

```py
from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.rating})"
```

**Migrate**

```bash
python manage.py makemigrations
python manage.py migrate

# Open Django Shell
python3 manage.py shell
```

**Read and Update**

```py
from book_outlet.models import Book

Book.objects.all()[1]
# <Book: Lord of the Rings (4)>

Book.objects.all()[1].author
Book.objects.all()[1].is_bestselling
# False

Book.objects.all()[1].rating
# 4

harry_potter = Book.objects.all()[0]
harry_potter.title
# "Harry Potter 1 – The Philosopher's Stone"

lotr = Book.objects.all()[1]
lotr.title
# 'Lord of the Rings'

harry_potter.author = "J.K. Rowling"
harry_potter.is_bestselling = True
harry_potter.save()

Book.objects.all()[0].author
# 'J.K. Rowling'

lotr.author = "J.R.R. Tolkien"
lotr.is_bestselling = True
lotr.save()

Book.objects.all()[1].author
# 'J.R.R. Tolkien'

Book.objects.all()[1].is_bestselling
# True
```

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("book_outlet.urls"))
]
```

**Delete**

```py
harry_potter = Book.objects.all()[0]
harry_potter.delete()
# (1, {'book_outlet.Book': 1})
Book.objects.all()
# <QuerySet [<Book: Lord of the Rings (4)>]>
```

**create method**

```py
Book.objects.create(title="Harry Potter 1", rating=5, author="J.K. Rowling", is_bestselling=True)
# <Book: Harry Potter 1 (5)>
Book.objects.all()
# <QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>]>
Book.objects.create(title="My Story", rating=2, author="Max", is_bestselling=False)
# <Book: My Story (2)>
Book.objects.create(title="Some random book", rating=1, author="Random Dude", is_bestselling=False)
# <Book: Some random book (1)>
Book.objects.all()
# <QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>, <Book: My Story (2)>, <Book: Some random book (1)>]>
```

**get method**

```py
Book.objects.get(title="My Story")
# <Book: My Story (2)>
Book.objects.get(rating=5)
# <Book: Harry Potter 1 (5)>
Book.objects.all()
# <QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>, <Book: My Story (2)>, <Book: Some random book (1)>]>
Book.objects.get(is_bestselling=True)
# Traceback (most recent call last):
#   ...
# django.core.exceptions.MultipleObjectsReturned: get() returned more than one Book -- it returned 2!
```

**filter method**

```py
Book.objects.filter(is_bestselling=True)
# <QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>]>
Book.objects.filter(is_bestselling=False)
# <QuerySet [<Book: My Story (2)>, <Book: Some random book (1)>]>
Book.objects.filter(is_bestselling=False, rating=2)
# <QuerySet [<Book: My Story (2)>]>
Book.objects.filter(rating<3)
# Traceback (most recent call last):
#   ...
# NameError: name 'rating' is not defined
Book.objects.filter(rating__lt=3)
# <QuerySet [<Book: My Story (2)>, <Book: Some random book (1)>]>
Book.objects.filter(rating__lt=3, title__contains="Story")
# <QuerySet [<Book: My Story (2)>]>
```

**case-insensitive lookups and "OR" queries using Q objects**

```py
Book.objects.filter(rating__lt=3, title__contains="story")
# <QuerySet []>, but works for sqlite
Book.objects.filter(rating__lt=3, title__icontains="story")
# <QuerySet [<Book: My Story (2)>]>
from django.db.models import Q
Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True)))
#   File "<console>", line 1
#     Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True)))
#                                                                 ^
# SyntaxError: unmatched ')'
Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True))
# <QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>, <Book: My Story (2)>, <Book: Some random book (1)>]>

Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True), Q(author="J.K. Rowling"))
# <QuerySet [<Book: Harry Potter 1 (5)>]>
Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True), author="J.K. Rowling")
# <QuerySet [<Book: Harry Potter 1 (5)>]>
Book.objects.filter(author="J.K. Rowling", Q(rating__lt=3) | Q(is_bestselling=True))
#   File "<console>", line 1
#     Book.objects.filter(author="J.K. Rowling", Q(rating__lt=3) | Q(is_bestselling=True))
#                                              ^
# SyntaxError: positional argument follows keyword argument
```

**Query Optimizations**

```py
bestsellers = Book.objects.filter(is_bestselling=True)
amazing_bestsellers = bestsellers.filter(rating__gt=4)
print(bestsellers)
# <QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>]>
print(amazing_bestsellers)
# <QuerySet [<Book: Harry Potter 1 (5)>]>
print(bestsellers)
# <QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>]>

print(Book.objects.filter(rating__gt=3))
# <QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>]>
print(Book.objects.filter(rating__gt=3))
# <QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>]>
good_books = Book.objects.filter(rating__gt=3)
print(good_books)
# <QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>]>
print(good_books)
# <QuerySet [<Book: Lord of the Rings (4)>, <Book: Harry Potter 1 (5)>]>
```

**Ordering and Aggregation**

```py
# Ordering
Book.objects.order_by('title')  # Ascending
Book.objects.order_by('-title')  # Descending
# Aggregation
Book.objects.aggregate(Avg('rating'))
Book.objects.aggregate(total=Count('id'))
```

---

### QuerySet Methods

| Method       | Description                                   |
| ------------ | --------------------------------------------- |
| `all()`      | Get all records                               |
| `get()`      | Get single record (raises error if not found) |
| `filter()`   | Get records matching conditions               |
| `exclude()`  | Get records NOT matching conditions           |
| `order_by()` | Sort records                                  |
| `first()`    | Get first record                              |
| `last()`     | Get last record                               |
| `count()`    | Count records                                 |
| `exists()`   | Check if records exist                        |
| `values()`   | Return dictionaries instead of objects        |
| `distinct()` | Remove duplicates                             |

---

### Lookup Expressions (Filters)

| Lookup       | Description               | Example                             |
| ------------ | ------------------------- | ----------------------------------- |
| `exact`      | Exact match               | `filter(name__exact='John')`        |
| `iexact`     | Case-insensitive exact    | `filter(name__iexact='john')`       |
| `contains`   | Contains substring        | `filter(title__contains='Python')`  |
| `icontains`  | Case-insensitive contains | `filter(title__icontains='python')` |
| `startswith` | Starts with               | `filter(name__startswith='J')`      |
| `endswith`   | Ends with                 | `filter(email__endswith='.com')`    |
| `gt`         | Greater than              | `filter(age__gt=18)`                |
| `gte`        | Greater than or equal     | `filter(age__gte=18)`               |
| `lt`         | Less than                 | `filter(price__lt=100)`             |
| `lte`        | Less than or equal        | `filter(price__lte=100)`            |
| `in`         | In a list                 | `filter(id__in=[1, 2, 3])`          |
| `isnull`     | Is NULL                   | `filter(bio__isnull=True)`          |

---

**Implementing Models in Django**

**Create book_outlet\templates\book_outlet\base.html**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}{% endblock title %}</title>
  </head>
  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

**Create book_outlet\templates\book_outlet\index.html**

```html
<pre>
{% extends "book_outlet/base.html" %}

{% block title %}
  All Books
{% endblock title %}

{% block content %}
  <ul>
    <li>Book 1...</li>
  </ul>
{% endblock content %}
</pre>
```

**Register url**

```py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index)
]
```

**Create view**

```py
from django.shortcuts import render

def index(request):
  return render(request, "book_outlet/index.html")
```

**Update view**

```py
from django.shortcuts import render

from .models import Book

def index(request):
  books = Book.objects.all()
  return render(request, "book_outlet/index.html", {
    "books": books
  })
```

**Update book_outlet\templates\book_outlet\index.html**

```html
<pre>
{% extends "book_outlet/base.html" %}

{% block title %}
  All Books
{% endblock title %}

{% block content %}
  <ul>
    {% for book in books %}
      <li>{{ book.title }} (Rating: {{ book.rating }})</li>
    {% endfor %}
  </ul>
{% endblock content %}
</pre>
```

---

**Create book_outlet\templates\book_outlet\book_detail.html**

```html
<pre>
{% extends "book_outlet/base.html" %}

{% block title %}
  {{ title }}
{% endblock %}

{% block content %}
  <h1>{{ title }}</h1>
  <h2>{{ author }}</h2>
  <p>The book has a rating of {{ rating }} 
  {% if is_bestseller %}
    and is a bestseller.
  {% else %}
    but isn't a bestseller.
  {% endif %}
  </p>
{% endblock %}
</pre>
```

**Add Book detail url**

```py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<int:id>", views.book_detail, name="book-detail")
]
```

**Add Book detail view**

```py
from django.shortcuts import get_object_or_404, render
from django.http import Http404


def book_detail(request, id):
  # try:
  #   book = Book.objects.get(pk=id)
  # except:
  #   raise Http404()
  book = get_object_or_404(Book, pk=id)
  return render(request, "book_outlet/book_detail.html", {
    "title": book.title,
    "author": book.author,
    "rating": book.rating,
    "is_bestseller": book.is_bestselling
  })
```

**Update index page**

```html
<pre>
{% extends "book_outlet/base.html" %}

{% block title %}
  All Books
{% endblock %}

{% block content %}
  <ul>
    {% for book in books %}
      <li>
        <a href="{% url 'book-detail' book.id %}">
          {{ book.title }}
        </a>
        (Rating: {{ book.rating }})
      </li>
    {% endfor %}
  </ul>
{% endblock %}
</pre>
```

---

**Using slug instead of id**

**Update model**

```py
from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    # Harry Potter 1 => harry-potter-1
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
        # return reverse("book-detail", args=[self.id])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
```

**Just call save again to add slug**

```py
Book.objects.get(title="Harry Potter 1").save()
Book.objects.get(title="Harry Potter 1").slug
# 'harry-potter-1'
Book.objects.get(title="Lord of the Rings").save()
Book.objects.get(title="Lord of the Rings").slug
# 'lord-of-the-rings'
Book.objects.get(title="My Story").save()
Book.objects.get(title="Some random book").save()
```

**Update urls**

```py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.book_detail, name="book-detail")
]
```

**Update view**

```py
def book_detail(request, slug):
  book = get_object_or_404(Book, slug=slug)
  return render(request, "book_outlet/book_detail.html", {
    "title": book.title,
    "author": book.author,
    "rating": book.rating,
    "is_bestseller": book.is_bestselling
  })
```

**Update index page**

```html
<pre>
{% extends "book_outlet/base.html" %}

{% block title %}
  All Books
{% endblock %}

{% block content %}
  <ul>
    {% for book in books %}
      <li><a href="{{ book.get_absolute_url }}">{{ book.title }}</a> (Rating: {{ book.rating }})</li>
    {% endfor %}
  </ul>
{% endblock %}
</pre>
```

---

**Adding Summary**

**Update view**

```py
from django.db.models import Avg

def index(request):
  books = Book.objects.all().order_by("-rating")
  num_books = books.count()
  avg_rating = books.aggregate(Avg("rating")) # rating__avg, rating__min

  return render(request, "book_outlet/index.html", {
    "books": books,
    "total_number_of_books": num_books,
    "average_rating": avg_rating
  })
```

**Update index page**

```html
<pre>
{% extends "book_outlet/base.html" %}

{% block title %}
  All Books
{% endblock %}

{% block content %}
  <ul>
    {% for book in books %}
      <li><a href="{{ book.get_absolute_url }}">{{ book.title }}</a> (Rating: {{ book.rating }})</li>
    {% endfor %}
  </ul>

  <hr>

  <p>Total Number Of Books: {{ total_number_of_books }}</p>
  <p>Average Rating: {{ average_rating.rating__avg }}</p>
{% endblock %}
</pre>
```

---

---

---

## Form Data Handling and Sessions

#### What are HTML Forms?

HTML forms are the primary way users submit data to a web server. Forms allow users to:

- Enter text (usernames, passwords, comments)
- Select options (dropdowns, checkboxes, radio buttons)
- Upload files
- Submit data for processing

#### HTTP Methods for Forms

| Method   | Usage                               | Data Location                    |
| -------- | ----------------------------------- | -------------------------------- |
| **GET**  | Retrieving data, search forms       | URL query string (`?name=value`) |
| **POST** | Submitting data, creating resources | Request body (hidden from URL)   |

**When to use each:**

- **GET**: Search forms, filters, bookmarkable pages
- **POST**: Login forms, registration, file uploads, sensitive data

---

### Basic HTML Form

```html
<form method="POST" action="/submit/">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username" />

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" />

  <button type="submit">Submit</button>
</form>
```

**Key attributes:**

- `method`: HTTP method (GET or POST)
- `action`: URL where form data is sent
- `name`: Field name used to access data on server

---

### Processing Form Data in Django

#### Accessing POST Data

```python
from django.http import HttpResponse
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        # Access form data using field names
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Process the data (save to database, etc.)
        return HttpResponse(f"Welcome, {username}!")

    # Show empty form for GET request
    return render(request, 'register.html')
```

---

#### Accessing GET Data

```python
def search(request):
    # Access query parameters
    query = request.GET.get('q', '')  # Default to empty string
    page = request.GET.get('page', '1')

    # Perform search with query
    return HttpResponse(f"Searching for: {query}")
```

---

### Form Data Methods

| Method                                 | Description                               |
| -------------------------------------- | ----------------------------------------- |
| `request.POST.get('field')`            | Get single value, returns None if missing |
| `request.POST.get('field', 'default')` | Get value with default                    |
| `request.POST['field']`                | Get value, raises error if missing        |
| `request.POST.getlist('field')`        | Get multiple values (checkboxes)          |

---
