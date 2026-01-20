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

---

---

## Templates & Static Files

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
