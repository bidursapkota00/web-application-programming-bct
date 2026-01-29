# Django REST Framework

![Bidur Sapkota](https://www.bidursapkota.com.np/images/gravatar.webp "Bidur Sapkota - Developer")&nbsp;[Bidur Sapkota](https://www.bidursapkota.com.np/)

![Django Rest Framework by Bidur Sapkota](/images/unit-4/14-drf-post-1200.webp "Django Rest Framework – Blog by Bidur Sapkota")

## Table of Contents

1. [API Basics](#api-basics)

## API Basics

An **API (Application Programming Interface)** is a set of rules, protocols, and tools that allows different software applications to communicate with each other. Think of an API as a waiter in a restaurant: you (the client) tell the waiter (the API) what you want, and the waiter communicates your order to the kitchen (the server) and brings back your food (the response).

In technical terms, an API defines:

- **What operations are available** (e.g., get user data, create a post, delete a record)
- **How to request those operations** (e.g., what URL to call, what data to send)
- **What format the response will be in** (e.g., JSON, XML)

APIs act as intermediaries that enable software components to interact without needing to know the internal workings of each other. This abstraction is powerful because it allows developers to use complex services without understanding their complete implementation.

### Types of APIs

There are several types of APIs based on their accessibility and purpose:

#### 1. Open APIs (Public APIs)

Open APIs are publicly available and can be used by any developer. They often require registration and an API key for access control and rate limiting. Examples include:

- Twitter API for accessing tweets and user data
- Google Maps API for embedding maps and location services
- OpenWeatherMap API for weather information

#### 2. Internal APIs (Private APIs)

Internal APIs are used within an organization to connect different internal systems. They are not exposed to external developers and are designed to improve productivity and data sharing among internal teams. For example, a company might have an internal API that connects their HR system with their payroll system.

#### 3. Partner APIs

Partner APIs are shared with specific business partners under agreed terms. They require special authorization and are used for B2B (business-to-business) integrations. An example would be an e-commerce platform sharing an API with its payment processor.

#### 4. Composite APIs

Composite APIs combine multiple API calls into a single request. They are useful when a client needs data from several sources. Instead of making five separate API calls, a composite API can bundle them together, reducing network overhead and improving performance.

### Why APIs are Used

APIs serve numerous critical purposes in modern software development:

#### 1. Modularity and Separation of Concerns

APIs allow developers to build modular systems where each component has a specific responsibility. The frontend can focus on user interface and experience, while the backend handles data processing and business logic. This separation makes systems easier to develop, test, and maintain.

#### 2. Reusability

Once an API is built, it can be used by multiple clients. A single backend API can serve a web application, a mobile app, a desktop application, and even third-party integrations. This eliminates code duplication and ensures consistency across platforms.

#### 3. Scalability

APIs enable horizontal scaling. As demand grows, you can deploy multiple instances of your API server behind a load balancer. Each API endpoint can also be scaled independently based on its usage patterns.

#### 4. Integration

APIs make it possible to integrate with external services without building everything from scratch. Need payment processing? Use Stripe's API. Need email delivery? Use SendGrid's API. Need maps? Use Google Maps API. This dramatically accelerates development.

#### 5. Security and Access Control

APIs provide a controlled way to expose functionality. Instead of giving direct database access (which would be extremely dangerous), you expose specific endpoints with defined permissions. This allows fine-grained control over who can access what data and what operations they can perform.

#### 6. Platform Independence

APIs abstract away implementation details. A client written in JavaScript can communicate with a server written in Python, which might store data in a PostgreSQL database. The client doesn't need to know anything about Python or PostgreSQL—it just needs to know how to make HTTP requests.

### Browser-Server Communication

Understanding browser-server communication is fundamental to understanding how APIs work in web applications.

#### The Request-Response Cycle

When you type a URL in your browser or click a link, a series of events occurs:

1. **DNS Resolution**: The browser converts the domain name (e.g., www.example.com) to an IP address using the Domain Name System.

2. **TCP Connection**: The browser establishes a TCP (Transmission Control Protocol) connection with the server. For HTTPS, this includes a TLS handshake for encryption.

3. **HTTP Request**: The browser sends an HTTP request to the server. This request includes:
   - The HTTP method (GET, POST, PUT, DELETE, etc.)
   - The URL path
   - Headers (metadata about the request)
   - Body (optional, containing data for POST/PUT requests)

4. **Server Processing**: The server receives the request, processes it (which might involve querying a database, performing calculations, calling other services), and prepares a response.

5. **HTTP Response**: The server sends back an HTTP response containing:
   - A status code (200 for success, 404 for not found, 500 for server error, etc.)
   - Headers (metadata about the response)
   - Body (the actual content—HTML, JSON, XML, images, etc.)

6. **Rendering**: The browser receives the response and renders it. For HTML, it parses the document and displays it. For API responses (typically JSON), the JavaScript code processes the data.

#### Synchronous vs Asynchronous Communication

**Synchronous communication** blocks the execution until a response is received. In early web development, page loads were synchronous—clicking a link would freeze the browser until the new page loaded.

**Asynchronous communication** allows the page to remain interactive while waiting for responses. Modern web applications use AJAX (Asynchronous JavaScript and XML) and the Fetch API to make asynchronous requests. This enables dynamic updates without full page reloads.

#### The Role of APIs in Modern Architecture

In traditional web applications (Multi-Page Applications or MPAs), the server generates complete HTML pages. When you click a link, the entire page reloads.

In modern web applications (Single-Page Applications or SPAs), the initial page load fetches a JavaScript application. Subsequent interactions are handled by the JavaScript code, which makes API calls to fetch or send data. Only the necessary parts of the page are updated, creating a smoother user experience.

This architectural shift has made APIs central to web development. The backend becomes an "API server" that serves data (usually as JSON), and the frontend becomes a separate application that consumes this data.

### API in Practice: How It All Connects

Consider a social media application:

1. **User opens the app**: The browser loads the frontend (HTML, CSS, JavaScript).

2. **User logs in**: The frontend sends the username and password to the `/api/login` endpoint. The server validates credentials and returns an authentication token.

3. **Loading the feed**: The frontend calls `/api/posts?page=1`. The server queries the database for recent posts and returns them as JSON.

4. **Creating a post**: The user writes a post and clicks "Share." The frontend sends the post content to `/api/posts` using a POST request. The server saves the post and returns the created post data.

5. **Liking a post**: The user clicks the like button. The frontend sends a POST request to `/api/posts/123/like`. The server updates the like count and returns the new count.

Each of these interactions happens through API calls, with the frontend and backend communicating via HTTP requests and JSON responses.

### Complete Code Example: Simple API Client (Browser)

The following is a complete HTML file that demonstrates how a browser communicates with an API. It uses a free public API to fetch and display data.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>API Communication Demo</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        max-width: 800px;
        margin: 50px auto;
        padding: 20px;
      }
      .user-card {
        border: 1px solid #ddd;
        padding: 15px;
        margin: 10px 0;
        border-radius: 8px;
      }
      button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
        border-radius: 5px;
      }
      button:hover {
        background-color: #0056b3;
      }
      #loading {
        color: #666;
        font-style: italic;
      }
    </style>
  </head>
  <body>
    <h1>Browser-Server API Communication</h1>
    <p>Click the button to fetch user data from a public API.</p>

    <button id="fetchBtn">Fetch Users from API</button>
    <p id="loading" style="display: none;">Loading data from server...</p>

    <div id="users"></div>

    <script>
      // Get references to DOM elements
      const fetchBtn = document.getElementById("fetchBtn");
      const usersDiv = document.getElementById("users");
      const loadingText = document.getElementById("loading");

      // Add click event listener to the button
      fetchBtn.addEventListener("click", function () {
        // Show loading indicator
        loadingText.style.display = "block";
        usersDiv.innerHTML = "";

        // Make an API request using the Fetch API
        // This is an asynchronous HTTP GET request
        fetch("https://jsonplaceholder.typicode.com/users")
          .then(function (response) {
            // Check if the response was successful
            if (!response.ok) {
              throw new Error(
                "Network response was not ok: " + response.status,
              );
            }
            // Parse the JSON from the response body
            return response.json();
          })
          .then(function (users) {
            // Hide loading indicator
            loadingText.style.display = "none";

            // Display each user
            users.forEach(function (user) {
              const card = document.createElement("div");
              card.className = "user-card";
              card.innerHTML =
                "<h3>" +
                user.name +
                "</h3>" +
                "<p><strong>Email:</strong> " +
                user.email +
                "</p>" +
                "<p><strong>Company:</strong> " +
                user.company.name +
                "</p>" +
                "<p><strong>City:</strong> " +
                user.address.city +
                "</p>";
              usersDiv.appendChild(card);
            });
          })
          .catch(function (error) {
            // Handle any errors that occurred during the fetch
            loadingText.style.display = "none";
            usersDiv.innerHTML =
              '<p style="color: red;">Error: ' + error.message + "</p>";
          });
      });
    </script>
  </body>
</html>
```

**How to run this example:**

1. Save the code above as `api_demo.html`
2. Open the file in any web browser
3. Click the "Fetch Users from API" button
4. The browser will make an HTTP GET request to the JSONPlaceholder API and display the returned user data

This example demonstrates the complete request-response cycle: the browser sends a request, waits asynchronously for the response, parses the JSON data, and updates the page dynamically.

---

## 4.2 REST Principles and Design, RESTful APIs

### What is REST?

**REST (Representational State Transfer)** is an architectural style for designing networked applications. It was introduced by Roy Fielding in his doctoral dissertation in 2000. REST is not a protocol or a standard—it's a set of architectural constraints that, when applied to web services, create systems that are scalable, flexible, and easy to understand.

A **RESTful API** is an API that adheres to REST principles. It uses HTTP as its communication protocol and follows specific conventions for how resources are identified, accessed, and manipulated.

REST has become the dominant architectural style for web APIs because it leverages the existing infrastructure of the web (HTTP, URLs, caching mechanisms) and provides a intuitive way to model operations on data.

### The Six Constraints of REST

Roy Fielding defined six architectural constraints that characterize REST:

#### 1. Client-Server Architecture

The client and server must be separate and independent. The client handles the user interface and user experience. The server handles data storage, business logic, and security. This separation allows each to evolve independently—you can completely rewrite the frontend without touching the backend, and vice versa.

**Benefits:**

- Portability of the user interface across multiple platforms
- Scalability by simplifying server components
- Independent evolution of client and server

#### 2. Statelessness

Each request from the client must contain all the information needed to process that request. The server does not store any client state between requests. If authentication is required, the client must include authentication credentials (like a token) with every request.

**Why statelessness matters:**

- **Scalability**: Any server can handle any request because there's no session state to maintain
- **Reliability**: If a server fails, requests can be routed to another server without losing state
- **Simplicity**: The server doesn't need complex session management logic

**Example of statelessness:**

```
Request 1: GET /api/users/123
Headers: Authorization: Bearer abc123token

Request 2: GET /api/users/123/posts
Headers: Authorization: Bearer abc123token
```

Each request includes the authentication token. The server doesn't remember that Request 1 was authenticated—the client must prove its identity every time.

#### 3. Cacheability

Responses must explicitly or implicitly define themselves as cacheable or non-cacheable. If cacheable, clients can reuse response data for equivalent requests, reducing server load and improving performance.

HTTP provides caching mechanisms through headers like:

- `Cache-Control`: Specifies caching directives
- `Expires`: Specifies when the response becomes stale
- `ETag`: A version identifier for the resource

**Example cache headers:**

```
HTTP/1.1 200 OK
Cache-Control: max-age=3600
ETag: "abc123"
```

This tells the client it can cache the response for 3600 seconds (1 hour).

#### 4. Uniform Interface

This is the fundamental constraint that distinguishes REST from other architectural styles. A uniform interface simplifies and decouples the architecture, allowing each part to evolve independently.

The uniform interface has four sub-constraints:

**a) Identification of Resources**: Resources are identified by URIs (Uniform Resource Identifiers). A resource could be a user, a product, an order, or any other entity. Each resource has a unique URI.

**b) Manipulation of Resources Through Representations**: When a client holds a representation of a resource (like a JSON object), it has enough information to modify or delete that resource.

**c) Self-Descriptive Messages**: Each message (request or response) contains enough information to describe how to process it. This includes the content type, caching headers, and status codes.

**d) Hypermedia as the Engine of Application State (HATEOAS)**: Responses should include links to related resources and available actions. The client can navigate the API by following these links.

#### 5. Layered System

The architecture can be composed of hierarchical layers, with each layer only knowing about the layer immediately adjacent to it. A client cannot tell whether it's connected directly to the end server or an intermediary. This allows for:

- **Load balancers**: Distributing requests across multiple servers
- **Proxies**: Caching responses or filtering content
- **Gateways**: Translating between protocols or handling authentication

#### 6. Code on Demand (Optional)

Servers can extend client functionality by sending executable code (like JavaScript). This is the only optional constraint in REST. While it adds flexibility, it also complicates security and is not commonly used in typical REST APIs.

### HTTP Verbs (Methods)

REST APIs use standard HTTP methods to define actions on resources. Each method has specific semantics:

#### GET - Retrieve Resources

GET requests retrieve data without modifying it. They are **safe** (don't change server state) and **idempotent** (calling multiple times has the same effect as calling once).

**Use cases:**

- Fetching a list of users: `GET /api/users`
- Fetching a specific user: `GET /api/users/123`
- Searching with filters: `GET /api/users?role=admin&active=true`

**Characteristics:**

- Should never modify data
- Can be cached
- Can be bookmarked
- Parameters go in the URL

#### POST - Create Resources

POST requests create new resources. They are neither safe nor idempotent—each POST typically creates a new resource.

**Use cases:**

- Creating a new user: `POST /api/users`
- Submitting a form: `POST /api/contact`
- Uploading a file: `POST /api/uploads`

**Characteristics:**

- Creates new resources
- Request body contains the resource data
- Returns the created resource (usually with its new ID)
- Typically returns 201 (Created) status code

#### PUT - Update/Replace Resources

PUT requests replace an existing resource entirely. They are idempotent—making the same PUT request multiple times has the same effect as making it once.

**Use cases:**

- Updating a user: `PUT /api/users/123`
- Replacing a configuration: `PUT /api/settings/notifications`

**Characteristics:**

- Replaces the entire resource
- Client must send the complete resource
- If the resource doesn't exist, it may create it
- Idempotent

#### PATCH - Partial Update

PATCH requests partially modify a resource. Unlike PUT, you only send the fields that need to change.

**Use cases:**

- Updating only the email: `PATCH /api/users/123` with body `{"email": "new@email.com"}`
- Changing the status: `PATCH /api/orders/456` with body `{"status": "shipped"}`

**Characteristics:**

- Partial update
- Only changed fields in the request body
- More efficient for small updates

#### DELETE - Remove Resources

DELETE requests remove a resource. They are idempotent—deleting a resource that doesn't exist should return the same response as successfully deleting it.

**Use cases:**

- Deleting a user: `DELETE /api/users/123`
- Removing an item from cart: `DELETE /api/cart/items/789`

**Characteristics:**

- Removes the resource
- Should be idempotent
- Typically returns 204 (No Content) or 200 with a confirmation message

### Endpoints and URL Design

Good URL design is crucial for creating intuitive and maintainable APIs. Here are the key principles:

#### 1. Use Nouns, Not Verbs

URLs should represent resources (nouns), and HTTP methods should represent actions (verbs).

**Good:**

- `GET /users` - Get all users
- `POST /users` - Create a user
- `DELETE /users/123` - Delete user 123

**Bad:**

- `GET /getUsers`
- `POST /createUser`
- `GET /deleteUser/123`

#### 2. Use Plural Nouns

Use plural nouns for consistency, even when referring to a single resource.

**Good:**

- `/users`
- `/users/123`
- `/posts`
- `/posts/456`

**Avoid mixing:**

- `/user` for single, `/users` for collection

#### 3. Hierarchical Relationships

Use URL hierarchy to represent relationships between resources.

- `GET /users/123/posts` - All posts by user 123
- `GET /users/123/posts/456` - Post 456 by user 123
- `GET /posts/456/comments` - All comments on post 456

#### 4. Use Query Parameters for Filtering

Use query strings for filtering, sorting, and pagination:

- `GET /users?role=admin` - Filter by role
- `GET /users?sort=name&order=asc` - Sort results
- `GET /users?page=2&limit=20` - Pagination
- `GET /products?minPrice=10&maxPrice=100` - Range filter

#### 5. Use Consistent Naming Conventions

Choose a naming convention and stick to it:

- **Lowercase**: `/users`, `/blog-posts`
- **Hyphens for multi-word**: `/user-profiles`, `/order-items`
- **Avoid underscores**: `/user_profiles` (less readable in URLs)

### Resource Modeling

Resource modeling is the process of identifying and designing the resources in your API. Good resource modeling leads to intuitive, usable APIs.

#### Identifying Resources

Resources are the fundamental units of your API. They typically map to:

- Database entities (users, products, orders)
- Business concepts (shopping cart, checkout, payment)
- Actions that behave like resources (authentication, search results)

#### Resource Relationships

Resources often have relationships with each other:

**One-to-Many:**

- User has many Posts
- `/users/123/posts`

**Many-to-Many:**

- Users belong to many Groups, Groups have many Users
- `/users/123/groups` or `/groups/456/members`

**Nested vs. Flat:**

**Nested approach:**

```
GET /authors/123/books/456/chapters/789
```

**Flat approach:**

```
GET /chapters/789
```

The nested approach shows the hierarchy but can become unwieldy. A common practice is to limit nesting to one or two levels, using query parameters for deeper filtering.

### HTTP Status Codes

Status codes communicate the result of an API request. They are grouped into categories:

#### 2xx - Success

- **200 OK**: Request succeeded. Used for GET, PUT, PATCH when returning data.
- **201 Created**: Resource created successfully. Used for POST.
- **204 No Content**: Request succeeded but no content to return. Used for DELETE.

#### 3xx - Redirection

- **301 Moved Permanently**: Resource has moved to a new URL permanently.
- **304 Not Modified**: Cached version is still valid (for conditional requests).

#### 4xx - Client Errors

- **400 Bad Request**: Malformed request (invalid JSON, missing required fields).
- **401 Unauthorized**: Authentication required or invalid credentials.
- **403 Forbidden**: Authenticated but not authorized for this resource.
- **404 Not Found**: Resource doesn't exist.
- **405 Method Not Allowed**: HTTP method not supported for this endpoint.
- **422 Unprocessable Entity**: Request is well-formed but contains semantic errors.
- **429 Too Many Requests**: Rate limit exceeded.

#### 5xx - Server Errors

- **500 Internal Server Error**: Generic server error.
- **502 Bad Gateway**: Server received an invalid response from upstream server.
- **503 Service Unavailable**: Server is temporarily unavailable.

### API Structure Best Practices

#### Versioning

APIs evolve over time. Versioning allows you to make changes without breaking existing clients.

**URL versioning:**

```
/api/v1/users
/api/v2/users
```

**Header versioning:**

```
GET /api/users
Headers: Api-Version: 2
```

**Query parameter versioning:**

```
/api/users?version=2
```

URL versioning is the most common and explicit approach.

#### Consistent Response Format

Maintain a consistent response structure across all endpoints:

```json
{
  "success": true,
  "data": {
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com"
  },
  "message": null
}
```

For errors:

```json
{
  "success": false,
  "data": null,
  "message": "User not found",
  "errors": [
    {
      "field": "id",
      "message": "No user exists with id 999"
    }
  ]
}
```

#### Pagination

For large collections, always implement pagination:

```json
{
    "data": [...],
    "pagination": {
        "currentPage": 2,
        "totalPages": 10,
        "totalItems": 195,
        "itemsPerPage": 20
    }
}
```

#### Authentication

Common authentication approaches:

- **API Keys**: Simple but less secure. Include in headers.
- **Bearer Tokens (JWT)**: More secure. Include in Authorization header.
- **OAuth 2.0**: For third-party access and delegated permissions.

### Complete Code Example: RESTful API with Django REST Framework

The following example demonstrates how to create a complete RESTful API using Django REST Framework (DRF). This example includes all the files needed to run a working Books API with all HTTP verbs.

#### Step 1: Project Setup

First, create a new Django project and install required packages:

```bash
# Create a project directory and navigate into it
mkdir books_api
cd books_api

# Create a virtual environment and activate it
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/Mac

# Install Django and Django REST Framework
pip install django djangorestframework

# Create Django project
django-admin startproject config .

# Create an app for books
python manage.py startapp books
```

#### Step 2: Configure Settings (config/settings.py)

Add `rest_framework` and `books` to the installed apps:

```python
# config/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'rest_framework',
    # Local apps
    'books',
]

# Optional: Configure REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

#### Step 3: Create the Model (books/models.py)

Define the Book model that represents our resource:

```python
# books/models.py

from django.db import models


class Book(models.Model):
    """
    Book model representing a book resource.
    Each book has a title, author, and optional publication year.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.title} by {self.author}"
```

#### Step 4: Create the Serializer (books/serializers.py)

Serializers convert model instances to JSON and validate incoming data:

```python
# books/serializers.py

from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Handles conversion between Book instances and JSON.
    Also performs validation on incoming data.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'year', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_year(self, value):
        """Custom validation for the year field."""
        if value is not None and (value < 1000 or value > 2100):
            raise serializers.ValidationError("Year must be between 1000 and 2100.")
        return value

    def validate_title(self, value):
        """Ensure title is not empty after stripping whitespace."""
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value.strip()
```

#### Step 5: Create the Views (books/views.py)

DRF provides ViewSets that automatically handle all CRUD operations:

```python
# books/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Book model.

    This single class provides all CRUD operations:
    - GET /api/books/ - List all books
    - POST /api/books/ - Create a new book
    - GET /api/books/{id}/ - Retrieve a specific book
    - PUT /api/books/{id}/ - Update a book (full replacement)
    - PATCH /api/books/{id}/ - Partial update of a book
    - DELETE /api/books/{id}/ - Delete a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        """
        GET /api/books/
        Returns a list of all books.
        Supports filtering by author using query parameter.
        """
        queryset = self.get_queryset()

        # Filter by author if provided
        author = request.query_params.get('author', None)
        if author:
            queryset = queryset.filter(author__icontains=author)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'count': queryset.count(),
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        """
        GET /api/books/{id}/
        Returns a single book by ID.
        """
        try:
            book = self.get_object()
            serializer = self.get_serializer(book)
            return Response({
                'success': True,
                'data': serializer.data
            })
        except Book.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Book not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """
        POST /api/books/
        Creates a new book.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Book created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        PUT /api/books/{id}/
        Updates a book (full replacement).
        """
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Book updated successfully',
                'data': serializer.data
            })
        return Response({
            'success': False,
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """
        PATCH /api/books/{id}/
        Partially updates a book.
        """
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Book partially updated',
                'data': serializer.data
            })
        return Response({
            'success': False,
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        DELETE /api/books/{id}/
        Deletes a book.
        """
        book = self.get_object()
        book.delete()
        return Response({
            'success': True,
            'message': 'Book deleted successfully'
        }, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_root(request):
    """
    API root endpoint providing documentation of available endpoints.
    """
    return Response({
        'message': 'Welcome to the Books API',
        'endpoints': {
            'GET /api/books/': 'List all books',
            'POST /api/books/': 'Create a new book',
            'GET /api/books/{id}/': 'Get a specific book',
            'PUT /api/books/{id}/': 'Update a book (full)',
            'PATCH /api/books/{id}/': 'Update a book (partial)',
            'DELETE /api/books/{id}/': 'Delete a book',
        }
    })
```

#### Step 6: Configure URLs (books/urls.py)

Create the URL routing for the API:

```python
# books/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, api_root

# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]
```

#### Step 7: Configure Project URLs (config/urls.py)

Include the books app URLs in the main project:

```python
# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
]
```

#### Step 8: Run Migrations and Start Server

```bash
# Create database tables
python manage.py makemigrations
python manage.py migrate

# Create sample data (optional - run in Django shell)
python manage.py shell
```

In the Django shell, create some sample books:

```python
from books.models import Book

Book.objects.create(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925)
Book.objects.create(title="To Kill a Mockingbird", author="Harper Lee", year=1960)
Book.objects.create(title="1984", author="George Orwell", year=1949)

exit()
```

Start the development server:

```bash
python manage.py runserver
```

The server will start at `http://localhost:8000`

#### Testing the API

You can test the API using Thunder Client (VS Code extension), the DRF browsable API, or any API testing tool.

**Using Thunder Client (VS Code Extension):**

Thunder Client is a lightweight REST API client built into VS Code. Follow these steps to test the API:

**Step 1: Install Thunder Client**

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Thunder Client"
4. Click Install

**Step 2: Open Thunder Client**

1. Click the Thunder Client icon in the VS Code sidebar (lightning bolt icon)
2. Click "New Request" button

**Step 3: GET All Books (List)**

1. Set the method dropdown to `GET`
2. Enter the URL: `http://localhost:8000/api/books/`
3. Click "Send"
4. You will see the JSON response with all books in the Response section

**Step 4: GET a Specific Book**

1. Click "New Request"
2. Set method to `GET`
3. Enter URL: `http://localhost:8000/api/books/1/`
4. Click "Send"
5. You will see the details of book with ID 1

**Step 5: Filter Books by Author**

1. Click "New Request"
2. Set method to `GET`
3. Enter URL: `http://localhost:8000/api/books/`
4. Click on the "Query" tab below the URL
5. Add a parameter: Key = `author`, Value = `orwell`
6. Click "Send"
7. You will see only books by authors matching "orwell"

**Step 6: POST - Create a New Book**

1. Click "New Request"
2. Set method to `POST`
3. Enter URL: `http://localhost:8000/api/books/`
4. Click on the "Body" tab
5. Select "JSON" from the dropdown
6. Enter the following JSON:

```json
{
  "title": "The Catcher in the Rye",
  "author": "J.D. Salinger",
  "year": 1951
}
```

7. Click "Send"
8. You will see a 201 Created response with the new book data

**Step 7: PUT - Update a Book (Full Replacement)**

1. Click "New Request"
2. Set method to `PUT`
3. Enter URL: `http://localhost:8000/api/books/1/`
4. Click on the "Body" tab
5. Select "JSON"
6. Enter the following JSON (all required fields):

```json
{
  "title": "The Great Gatsby - Revised Edition",
  "author": "F. Scott Fitzgerald",
  "year": 1926
}
```

7. Click "Send"
8. Book with ID 1 will be completely replaced with new data

**Step 8: PATCH - Partial Update**

1. Click "New Request"
2. Set method to `PATCH`
3. Enter URL: `http://localhost:8000/api/books/1/`
4. Click on the "Body" tab
5. Select "JSON"
6. Enter only the field you want to update:

```json
{
  "year": 2025
}
```

7. Click "Send"
8. Only the year field will be updated, other fields remain unchanged

**Step 9: DELETE - Remove a Book**

1. Click "New Request"
2. Set method to `DELETE`
3. Enter URL: `http://localhost:8000/api/books/2/`
4. Click "Send"
5. Book with ID 2 will be deleted
6. You will see a success message in the response

**Thunder Client Tips:**

- Save your requests to a Collection for reuse
- Use Environment variables for the base URL (e.g., `{{base_url}}/api/books/`)
- View response headers, status codes, and response time in the Response panel
- Use the "Tests" tab to add automated assertions

**Using the DRF Browsable API:**

Open `http://localhost:8000/api/books/` in your browser. DRF provides a user-friendly interface where you can:

- View the list of books
- Click on individual books to see details
- Use the built-in forms to create, update, or delete books
- See the raw JSON responses

This example demonstrates a complete RESTful API using Django REST Framework with proper HTTP verbs, meaningful endpoints, appropriate status codes, data validation through serializers, and consistent response formatting.

---

## 4.3 JSON versus XML Data Exchange

### Introduction to Data Exchange Formats

When APIs communicate, they need a common language to exchange data. This data must be structured in a way that both the sender and receiver can understand. The two most common formats for data exchange in web APIs are **JSON (JavaScript Object Notation)** and **XML (eXtensible Markup Language)**.

Choosing the right data format affects the performance, readability, and ease of development of your API. While both formats can represent the same data, they have different characteristics that make each better suited for specific use cases.

### What is JSON?

**JSON (JavaScript Object Notation)** is a lightweight, text-based data interchange format. Despite its name suggesting a connection to JavaScript, JSON is language-independent and can be used with virtually any programming language.

JSON was derived from JavaScript object literal syntax but has become a standard format used across all platforms. Its simplicity and readability have made it the dominant format for web APIs.

#### JSON Syntax Rules

JSON follows strict syntax rules:

1. **Data is in name/value pairs**: Each piece of data consists of a field name (in double quotes) followed by a colon and a value.

2. **Data is separated by commas**: Multiple name/value pairs are separated by commas.

3. **Curly braces hold objects**: An object is enclosed in curly braces `{}` and contains zero or more name/value pairs.

4. **Square brackets hold arrays**: An array is enclosed in square brackets `[]` and contains zero or more values.

5. **Values can be**: strings (in double quotes), numbers, booleans (`true` or `false`), `null`, objects, or arrays.

6. **Strings must use double quotes**: Single quotes are not allowed in JSON.

#### JSON Data Types

JSON supports the following data types:

| Data Type | Example             | Description                          |
| --------- | ------------------- | ------------------------------------ |
| String    | `"Hello World"`     | Text enclosed in double quotes       |
| Number    | `42`, `3.14`, `-17` | Integer or floating-point, no quotes |
| Boolean   | `true`, `false`     | Logical true or false values         |
| Null      | `null`              | Represents empty or unknown value    |
| Object    | `{"key": "value"}`  | Collection of key-value pairs        |
| Array     | `[1, 2, 3]`         | Ordered list of values               |

#### JSON Example

```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": {
    "firstName": "F. Scott",
    "lastName": "Fitzgerald",
    "nationality": "American"
  },
  "year": 1925,
  "genres": ["Fiction", "Classic", "Literary"],
  "available": true,
  "rating": 4.5,
  "publisher": null
}
```

This example demonstrates:

- Simple values (id, title, year, available, rating)
- Nested object (author)
- Array (genres)
- Null value (publisher)

### What is XML?

**XML (eXtensible Markup Language)** is a markup language designed to store and transport data. Unlike HTML, which is designed to display data, XML is designed to carry data with a focus on what the data is.

XML was developed by the W3C (World Wide Web Consortium) and was the dominant data exchange format before JSON gained popularity. It is still widely used in enterprise systems, document formats, and configuration files.

#### XML Syntax Rules

XML follows these syntax rules:

1. **XML must have a root element**: Every XML document must have exactly one root element that contains all other elements.

2. **Tags are case-sensitive**: `<Book>` and `<book>` are different elements.

3. **Elements must have closing tags**: Every opening tag must have a corresponding closing tag (`<title></title>`) or be self-closing (`<empty/>`).

4. **Elements must be properly nested**: Child elements must be closed before parent elements.

5. **Attribute values must be quoted**: Attributes are specified in the opening tag with values in quotes.

6. **Special characters must be escaped**: Characters like `<`, `>`, `&` must use entity references (`&lt;`, `&gt;`, `&amp;`).

#### XML Structure Components

| Component   | Syntax                   | Description                            |
| ----------- | ------------------------ | -------------------------------------- |
| Declaration | `<?xml version="1.0"?>`  | Optional header specifying XML version |
| Element     | `<name>content</name>`   | The basic building block of XML        |
| Attribute   | `<element attr="value">` | Metadata attached to an element        |
| Comment     | `<!-- comment -->`       | Notes that are not processed           |
| CDATA       | `<![CDATA[content]]>`    | Content that should not be parsed      |

#### XML Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<book id="1">
    <title>The Great Gatsby</title>
    <author>
        <firstName>F. Scott</firstName>
        <lastName>Fitzgerald</lastName>
        <nationality>American</nationality>
    </author>
    <year>1925</year>
    <genres>
        <genre>Fiction</genre>
        <genre>Classic</genre>
        <genre>Literary</genre>
    </genres>
    <available>true</available>
    <rating>4.5</rating>
    <publisher/>
</book>
```

This example shows:

- XML declaration
- Root element with attribute (book id="1")
- Nested elements (author)
- Multiple child elements for arrays (genre)
- Self-closing empty element (publisher)

### JSON vs XML: Detailed Comparison

#### 1. Syntax and Readability

**JSON:**

- Uses minimal punctuation (braces, brackets, colons, commas)
- More compact and less verbose
- Native to JavaScript, easy to read for web developers
- No closing tags or attributes

**XML:**

- Uses opening and closing tags for every element
- More verbose, requires more characters for the same data
- Tag names provide context but add bulk
- Supports attributes for metadata

**Example comparison for the same data:**

JSON (89 characters):

```json
{ "name": "John", "age": 30, "city": "New York" }
```

XML (119 characters):

```xml
<person><name>John</name><age>30</age><city>New York</city></person>
```

JSON is approximately 25% smaller for the same data.

#### 2. Data Types

**JSON:**

- Has built-in data types: string, number, boolean, null, array, object
- Numbers and booleans are native types (no quotes)
- Easy to distinguish between data types

**XML:**

- Everything is text by default
- No native data types; all values are strings
- Data types must be inferred or defined in a schema
- Requires parsing to determine if "30" is a number or string

#### 3. Arrays and Collections

**JSON:**

- Arrays are first-class citizens with `[]` syntax
- Easy to represent ordered collections
- Clear and concise: `"colors": ["red", "green", "blue"]`

**XML:**

- No native array support
- Collections are represented by repeating elements
- Requires wrapper elements or conventions
- More verbose: `<colors><color>red</color><color>green</color></colors>`

#### 4. Comments

**JSON:**

- Does not support comments
- Comments must be stripped before parsing
- Some parsers support non-standard comment syntax

**XML:**

- Supports comments with `<!-- comment -->` syntax
- Useful for documentation within the data

#### 5. Namespace Support

**JSON:**

- No built-in namespace support
- Naming conflicts must be handled by convention

**XML:**

- Full namespace support for avoiding naming conflicts
- Useful for combining data from multiple sources
- Example: `<book xmlns="http://example.com/books">`

#### 6. Schema Validation

**JSON:**

- JSON Schema available but not universally adopted
- Simpler validation rules
- Less mature tooling compared to XML

**XML:**

- Mature schema languages: DTD, XSD, RelaxNG
- Comprehensive validation capabilities
- Strong typing and complex constraints supported

#### 7. Parsing and Performance

**JSON:**

- Native parsing in JavaScript with `JSON.parse()`
- Fast parsing in most languages
- Lower memory overhead
- Simpler parser implementation

**XML:**

- Requires dedicated parser (DOM, SAX, StAX)
- DOM parsing loads entire document into memory
- SAX parsing is event-driven and memory-efficient
- XPath and XSLT for querying and transformation

### Comparison Summary Table

| Feature                | JSON                  | XML                 |
| ---------------------- | --------------------- | ------------------- |
| Readability            | High (for developers) | Medium              |
| Verbosity              | Low                   | High                |
| File Size              | Smaller               | Larger              |
| Data Types             | Built-in              | Text only           |
| Arrays                 | Native support        | No native support   |
| Comments               | Not supported         | Supported           |
| Namespaces             | Not supported         | Supported           |
| Schema                 | JSON Schema           | DTD, XSD, RelaxNG   |
| Parsing Speed          | Faster                | Slower              |
| JavaScript Integration | Native                | Requires conversion |
| Metadata (attributes)  | Not supported         | Supported           |
| Document markup        | Not suitable          | Well suited         |
| Configuration files    | Good                  | Good                |
| Web APIs               | Dominant              | Legacy systems      |

### When to Use JSON

- **Web APIs and REST services**: JSON is the standard for modern web APIs
- **JavaScript/Node.js applications**: Native support makes it the obvious choice
- **Mobile applications**: Smaller payload sizes reduce bandwidth
- **Configuration files**: Many modern tools use JSON for configuration
- **Data storage in NoSQL databases**: MongoDB, CouchDB store JSON documents
- **Real-time applications**: Lower parsing overhead benefits performance

### When to Use XML

- **Enterprise applications**: Many legacy systems use XML
- **Document-centric data**: Books, articles, contracts with mixed content
- **Complex data validation**: When strict schema validation is required
- **SOAP web services**: SOAP is XML-based and still used in enterprises
- **Configuration files**: Many Java applications use XML configuration
- **Data interchange with namespaces**: When combining data from multiple sources
- **Office documents**: DOCX, XLSX are XML-based formats

### Parsing JSON in Python

Python provides the built-in `json` module for working with JSON data.

```python
"""
JSON Parsing Demo in Python
This script demonstrates how to parse JSON data and convert Python objects to JSON.
"""

import json

# Sample JSON string (as received from an API)
json_string = '''
{
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "genres": ["Fiction", "Classic"],
    "available": true
}
'''

# Parse JSON string to Python dictionary
book = json.loads(json_string)

# Access data from the parsed JSON
print("Title:", book["title"])
print("Author:", book["author"])
print("Year:", book["year"])
print("Genres:", ", ".join(book["genres"]))
print("Available:", book["available"])

# Modify the data
book["rating"] = 4.5
book["genres"].append("Literary")

# Convert Python dictionary back to JSON string
json_output = json.dumps(book, indent=4)
print("\nModified JSON:")
print(json_output)
```

**Output:**

```
Title: The Great Gatsby
Author: F. Scott Fitzgerald
Year: 1925
Genres: Fiction, Classic
Available: True

Modified JSON:
{
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "genres": [
        "Fiction",
        "Classic",
        "Literary"
    ],
    "available": true,
    "rating": 4.5
}
```

### Parsing XML in Python

Python provides the `xml.etree.ElementTree` module for working with XML data.

```python
"""
XML Parsing Demo in Python
This script demonstrates how to parse XML data and extract values.
"""

import xml.etree.ElementTree as ET

# Sample XML string
xml_string = '''<?xml version="1.0" encoding="UTF-8"?>
<book id="1">
    <title>The Great Gatsby</title>
    <author>F. Scott Fitzgerald</author>
    <year>1925</year>
    <genres>
        <genre>Fiction</genre>
        <genre>Classic</genre>
    </genres>
    <available>true</available>
</book>
'''

# Parse XML string
root = ET.fromstring(xml_string)

# Access data from the parsed XML
print("Book ID:", root.attrib["id"])
print("Title:", root.find("title").text)
print("Author:", root.find("author").text)
print("Year:", root.find("year").text)

# Access nested elements (genres)
genres = root.find("genres")
genre_list = [genre.text for genre in genres.findall("genre")]
print("Genres:", ", ".join(genre_list))

# Access boolean (stored as string in XML)
available_text = root.find("available").text
available = available_text.lower() == "true"
print("Available:", available)

# Modify the XML
rating = ET.SubElement(root, "rating")
rating.text = "4.5"

# Add a new genre
new_genre = ET.SubElement(genres, "genre")
new_genre.text = "Literary"

# Convert back to string
modified_xml = ET.tostring(root, encoding="unicode")
print("\nModified XML:")
print(modified_xml)
```

### JSON in Django REST Framework

Django REST Framework uses JSON as the default format for API responses. When you make requests and receive responses, DRF automatically handles the conversion between Python objects and JSON.

DRF also supports content negotiation, allowing clients to request different formats by setting the `Accept` header or using format suffixes in URLs.

---

## 4.4 Data Validation and Serialization

### What is Serialization?

**Serialization** is the process of converting complex data types (like Python objects, database models, or querysets) into a format that can be easily transmitted over a network or stored. In the context of web APIs, serialization typically means converting data to JSON or XML.

**Deserialization** is the reverse process—converting data received in a format like JSON back into complex data types that can be used by the application.

In Django REST Framework, serializers handle both serialization and deserialization. They are one of the most powerful features of DRF, providing:

1. **Conversion**: Transform complex types to native Python datatypes that can then be rendered into JSON
2. **Validation**: Validate incoming data before it is saved to the database
3. **Parsing**: Parse incoming JSON data into Python objects

### Why is Serialization Important?

Serialization is crucial for web APIs because:

1. **Data Transfer**: HTTP is a text-based protocol. Complex objects like Python classes or database records cannot be sent directly over HTTP. They must be converted to a text format like JSON.

2. **Language Independence**: JSON can be understood by any programming language. A Python backend can serve data to JavaScript, Java, Swift, or any other client.

3. **Security**: Serialization allows you to control exactly what data is exposed. You can exclude sensitive fields like passwords or internal IDs.

4. **Data Transformation**: Serialization can transform data during the process, such as formatting dates, computing derived fields, or restructuring nested data.

5. **Consistency**: Serializers ensure that the API response format is consistent across all endpoints.

### What is Data Validation?

**Data validation** is the process of ensuring that incoming data meets specific requirements before it is processed or stored. Validation protects your application from:

1. **Invalid Data**: Ensuring data types are correct (e.g., age is a number, not a string)
2. **Missing Required Fields**: Ensuring all mandatory fields are present
3. **Business Rule Violations**: Ensuring data makes sense (e.g., end date is after start date)
4. **Security Threats**: Preventing malicious input like SQL injection or XSS attacks
5. **Data Corruption**: Maintaining data integrity in the database

### Validation Levels

Validation can occur at multiple levels:

| Level              | Description                              | Example                          |
| ------------------ | ---------------------------------------- | -------------------------------- |
| **Client-side**    | Validation in the browser before sending | HTML5 form validation            |
| **Request-level**  | Validating the HTTP request format       | Checking Content-Type header     |
| **Field-level**    | Validating individual fields             | Email format, string length      |
| **Object-level**   | Validating relationships between fields  | Password confirmation match      |
| **Database-level** | Constraints enforced by the database     | Unique constraints, foreign keys |

Django REST Framework provides powerful tools for field-level and object-level validation through serializers.

### Django REST Framework Serializers

DRF provides several types of serializers:

#### 1. Serializer

The base `Serializer` class gives you full control over the serialization process. You manually define each field and how it should be serialized.

#### 2. ModelSerializer

`ModelSerializer` automatically generates fields based on a Django model. It provides default implementations for `create()` and `update()` methods, reducing boilerplate code significantly.

#### 3. HyperlinkedModelSerializer

Similar to `ModelSerializer` but uses hyperlinks for relationships instead of primary keys.

### Serializer Field Types

DRF provides many field types that correspond to different data types:

| Field Type      | Python Type | Description                   |
| --------------- | ----------- | ----------------------------- |
| `CharField`     | `str`       | Text field                    |
| `IntegerField`  | `int`       | Integer numbers               |
| `FloatField`    | `float`     | Floating-point numbers        |
| `DecimalField`  | `Decimal`   | Fixed-precision decimal       |
| `BooleanField`  | `bool`      | True/False values             |
| `DateField`     | `date`      | Date values                   |
| `DateTimeField` | `datetime`  | Date and time values          |
| `EmailField`    | `str`       | Validated email addresses     |
| `URLField`      | `str`       | Validated URLs                |
| `ChoiceField`   | `str`       | One of predefined choices     |
| `ListField`     | `list`      | List of values                |
| `DictField`     | `dict`      | Dictionary of key-value pairs |

### Field Validation Options

Each field can have validation options:

| Option        | Description                   | Example            |
| ------------- | ----------------------------- | ------------------ |
| `required`    | Field must be present         | `required=True`    |
| `allow_null`  | Allow None values             | `allow_null=True`  |
| `allow_blank` | Allow empty strings           | `allow_blank=True` |
| `default`     | Default value if not provided | `default=0`        |
| `max_length`  | Maximum string length         | `max_length=100`   |
| `min_length`  | Minimum string length         | `min_length=3`     |
| `max_value`   | Maximum numeric value         | `max_value=100`    |
| `min_value`   | Minimum numeric value         | `min_value=0`      |
| `read_only`   | Field only for output         | `read_only=True`   |
| `write_only`  | Field only for input          | `write_only=True`  |

### Types of Validation in DRF

#### 1. Built-in Field Validation

Each field type has built-in validation. For example, `EmailField` validates email format, `URLField` validates URL format, and `IntegerField` ensures the value is an integer.

#### 2. Field-Level Validation

You can add custom validation for individual fields by defining `validate_<fieldname>` methods in your serializer.

#### 3. Object-Level Validation

For validation that depends on multiple fields, you override the `validate()` method. This is useful for validating relationships between fields.

#### 4. Custom Validators

You can create reusable validator functions or classes that can be applied to multiple fields or serializers.

### Complete Code Example: Data Validation and Serialization with DRF

This example demonstrates comprehensive validation and serialization using Django REST Framework. We will create a Book API with various validation rules.

#### Step 1: Create the Model (books/models.py)

```python
# books/models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    """
    Book model with various fields for demonstrating validation.
    """
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('history', 'History'),
        ('biography', 'Biography'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    publication_year = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(2100)]
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pages = models.PositiveIntegerField()
    in_stock = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.author}"
```

#### Step 2: Create Custom Validators (books/validators.py)

```python
# books/validators.py

from rest_framework import serializers
import re


def validate_isbn(value):
    """
    Custom validator to check ISBN format.
    ISBN must be exactly 10 or 13 digits.
    """
    # Remove any hyphens or spaces
    cleaned = re.sub(r'[-\s]', '', value)

    if len(cleaned) not in [10, 13]:
        raise serializers.ValidationError(
            "ISBN must be exactly 10 or 13 digits."
        )

    if not cleaned.isdigit():
        raise serializers.ValidationError(
            "ISBN must contain only digits."
        )

    return cleaned


def validate_no_special_characters(value):
    """
    Validator to ensure a string contains no special characters.
    Only letters, numbers, and spaces are allowed.
    """
    if not re.match(r'^[a-zA-Z0-9\s]+$', value):
        raise serializers.ValidationError(
            "This field can only contain letters, numbers, and spaces."
        )
    return value


class PriceRangeValidator:
    """
    Class-based validator to check if price is within a range.
    Can be configured with min and max values.
    """
    def __init__(self, min_price=0, max_price=10000):
        self.min_price = min_price
        self.max_price = max_price

    def __call__(self, value):
        if value < self.min_price:
            raise serializers.ValidationError(
                f"Price cannot be less than {self.min_price}."
            )
        if value > self.max_price:
            raise serializers.ValidationError(
                f"Price cannot exceed {self.max_price}."
            )
        return value
```

#### Step 3: Create the Serializer with Validation (books/serializers.py)

```python
# books/serializers.py

from rest_framework import serializers
from .models import Book
from .validators import validate_isbn, validate_no_special_characters, PriceRangeValidator
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model with comprehensive validation.
    Demonstrates various validation techniques in DRF.
    """

    # Explicit field definitions with validators
    isbn = serializers.CharField(
        max_length=13,
        validators=[validate_isbn],
        help_text="ISBN-10 or ISBN-13 format"
    )

    price = serializers.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[PriceRangeValidator(min_price=0.01, max_price=9999.99)]
    )

    # Read-only computed field
    price_display = serializers.SerializerMethodField()

    # Write-only field example
    confirm_data = serializers.BooleanField(
        write_only=True,
        required=False,
        default=True
    )

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'isbn', 'genre',
            'publication_year', 'price', 'price_display',
            'pages', 'in_stock', 'description',
            'confirm_data', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_price_display(self, obj):
        """
        SerializerMethodField to format price with currency.
        This is a computed field that only appears in output.
        """
        return f"${obj.price:.2f}"

    # Field-level validation methods
    def validate_title(self, value):
        """
        Validate the title field.
        - Must not be empty after stripping whitespace
        - Must be at least 2 characters long
        - Must not be all uppercase
        """
        value = value.strip()

        if not value:
            raise serializers.ValidationError("Title cannot be empty.")

        if len(value) < 2:
            raise serializers.ValidationError(
                "Title must be at least 2 characters long."
            )

        if value.isupper():
            raise serializers.ValidationError(
                "Title cannot be all uppercase. Please use proper capitalization."
            )

        return value

    def validate_author(self, value):
        """
        Validate the author field.
        - Must contain only letters and spaces
        - Must have at least first and last name
        """
        value = value.strip()

        if not value.replace(' ', '').isalpha():
            raise serializers.ValidationError(
                "Author name can only contain letters and spaces."
            )

        parts = value.split()
        if len(parts) < 2:
            raise serializers.ValidationError(
                "Please provide both first and last name."
            )

        return value

    def validate_publication_year(self, value):
        """
        Validate publication year.
        - Must be a valid year
        - Cannot be in the future
        """
        current_year = datetime.now().year

        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year is {current_year}."
            )

        if value < 1450:  # Gutenberg's printing press
            raise serializers.ValidationError(
                "Publication year seems too old. Books weren't printed before 1450."
            )

        return value

    def validate_pages(self, value):
        """
        Validate page count.
        - Must be a reasonable number
        """
        if value < 1:
            raise serializers.ValidationError(
                "A book must have at least 1 page."
            )

        if value > 10000:
            raise serializers.ValidationError(
                "Page count seems unrealistic. Maximum allowed is 10,000."
            )

        return value

    # Object-level validation
    def validate(self, data):
        """
        Object-level validation for cross-field validation.
        This method receives all field values and can validate
        relationships between fields.
        """
        # Check if price is reasonable for page count
        if 'price' in data and 'pages' in data:
            price_per_page = float(data['price']) / data['pages']
            if price_per_page > 1:
                raise serializers.ValidationError({
                    'price': 'Price per page is unusually high. Please verify the price.'
                })

        # Check if description is provided for non-fiction
        if data.get('genre') == 'non-fiction':
            if not data.get('description'):
                raise serializers.ValidationError({
                    'description': 'Non-fiction books should have a description.'
                })

        # Check if user confirmed data accuracy (for demonstration)
        if not data.get('confirm_data', True):
            raise serializers.ValidationError(
                "You must confirm that the data is accurate."
            )

        return data

    def create(self, validated_data):
        """
        Custom create method.
        Remove write-only fields before creating the model instance.
        """
        # Remove write-only field that's not part of the model
        validated_data.pop('confirm_data', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Custom update method.
        Remove write-only fields before updating.
        """
        validated_data.pop('confirm_data', None)
        return super().update(instance, validated_data)


class BookListSerializer(serializers.ModelSerializer):
    """
    Simplified serializer for list views.
    Shows fewer fields for better performance and cleaner list output.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'price', 'in_stock']
```

#### Step 4: Create the Views (books/views.py)

```python
# books/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Book
from .serializers import BookSerializer, BookListSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Book model demonstrating validation responses.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        """
        Use different serializers for different actions.
        List action uses a simplified serializer.
        """
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer

    def create(self, request):
        """
        Create a new book with detailed validation error responses.
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Book created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        # Return detailed validation errors
        return Response({
            'success': False,
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Update a book with validation.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Book updated successfully',
                'data': serializer.data
            })

        return Response({
            'success': False,
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def validate_only(self, request):
        """
        Custom action to validate data without saving.
        Useful for checking if data is valid before submission.
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            return Response({
                'success': True,
                'message': 'Data is valid',
                'validated_data': serializer.validated_data
            })

        return Response({
            'success': False,
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
```

#### Testing Validation with Thunder Client

**Test 1: Create a valid book**

1. Method: `POST`
2. URL: `http://localhost:8000/api/books/`
3. Body (JSON):

```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "9780743273565",
  "genre": "fiction",
  "publication_year": 1925,
  "price": "15.99",
  "pages": 180,
  "in_stock": true,
  "description": "A classic American novel."
}
```

**Test 2: Test validation errors (invalid data)**

1. Method: `POST`
2. URL: `http://localhost:8000/api/books/`
3. Body (JSON):

```json
{
  "title": "AB",
  "author": "John",
  "isbn": "123",
  "genre": "fiction",
  "publication_year": 2030,
  "price": "10000.00",
  "pages": 0,
  "in_stock": true
}
```

Expected validation errors:

- title: Must be at least 2 characters
- author: Must have first and last name
- isbn: Must be 10 or 13 digits
- publication_year: Cannot be in the future
- price: Exceeds maximum allowed
- pages: Must have at least 1 page

**Test 3: Test validate-only endpoint**

1. Method: `POST`
2. URL: `http://localhost:8000/api/books/validate_only/`
3. Body: Same as Test 1

This will validate the data without creating a record, useful for form validation before submission.

### Serialization and Deserialization Flow

Understanding the complete flow helps in debugging and designing APIs:

**Incoming Request (Deserialization):**

```
Client JSON → Request Body → Serializer → Field Validation →
Object Validation → Validated Data → Model Instance → Database
```

**Outgoing Response (Serialization):**

```
Database → Model Instance → Serializer → Python Dict →
JSON Renderer → Response Body → Client
```

### Best Practices for Validation

1. **Validate early**: Catch errors as soon as possible in the request lifecycle
2. **Be specific**: Provide clear, actionable error messages
3. **Validate completely**: Check all fields, not just the first error
4. **Use appropriate level**: Field-level for individual fields, object-level for cross-field validation
5. **Reuse validators**: Create reusable validator functions for common patterns
6. **Document validation rules**: Make it clear what the API expects
7. **Test edge cases**: Test boundary conditions and invalid inputs
8. **Sanitize input**: Clean data to prevent security vulnerabilities

---

## 4.5 Microservices

### What are Microservices?

**Microservices** (or Microservices Architecture) is an architectural approach where an application is built as a collection of small, independent services. Each service runs in its own process, can be deployed independently, and communicates with other services through well-defined APIs.

This is in contrast to the traditional **monolithic architecture**, where an entire application is built as a single, unified codebase. In a monolith, all features—user management, payments, notifications, reporting—are tightly integrated into one large application.

### Monolithic vs Microservices Architecture

#### Monolithic Architecture

In a monolithic application:

- All functionality exists in a single codebase
- The entire application is deployed as one unit
- All components share the same database
- Changes to any part require redeploying the entire application
- Scaling means replicating the entire application

**Example of a Monolithic E-commerce Application:**

```
┌─────────────────────────────────────────────────┐
│              E-Commerce Application              │
├─────────────────────────────────────────────────┤
│  User Module  │  Product Module  │ Order Module │
├───────────────┴──────────────────┴──────────────┤
│              Payment Module                      │
├─────────────────────────────────────────────────┤
│              Notification Module                 │
├─────────────────────────────────────────────────┤
│              Shared Database                     │
└─────────────────────────────────────────────────┘
```

#### Microservices Architecture

In a microservices application:

- Each service is a small, focused application
- Services can be deployed independently
- Each service can have its own database
- Services communicate via APIs (REST, gRPC, message queues)
- Individual services can be scaled independently

**Example of a Microservices E-commerce Application:**

```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│    User     │  │   Product   │  │    Order    │
│   Service   │  │   Service   │  │   Service   │
│  (Django)   │  │   (Flask)   │  │  (FastAPI)  │
│   [DB1]     │  │    [DB2]    │  │    [DB3]    │
└──────┬──────┘  └──────┬──────┘  └──────┬──────┘
       │                │                │
       └────────────────┼────────────────┘
                        │
                ┌───────┴───────┐
                │  API Gateway  │
                └───────┬───────┘
                        │
                   [Clients]
```

### Key Characteristics of Microservices

#### 1. Single Responsibility

Each microservice should do one thing and do it well. It focuses on a specific business capability. For example:

- User Service: Handles user registration, authentication, profile management
- Product Service: Manages product catalog, inventory, pricing
- Order Service: Processes orders, manages order status
- Payment Service: Handles payment processing, refunds
- Notification Service: Sends emails, SMS, push notifications

#### 2. Independence

Microservices are independent in several ways:

**Development Independence**: Different teams can work on different services without stepping on each other's toes.

**Technology Independence**: Each service can use the best technology for its specific needs. The User Service might use Django, while the Payment Service uses Node.js.

**Deployment Independence**: Services can be deployed separately. Updating the Product Service doesn't require redeploying the Order Service.

**Scaling Independence**: Services experiencing high load can be scaled independently. If the Product Service gets 10x more traffic, you scale only that service.

#### 3. Decentralized Data Management

Each microservice typically owns and manages its own data:

- Services have their own databases
- No direct database access across services
- Data is accessed only through service APIs
- This ensures loose coupling between services

#### 4. Resilience and Fault Isolation

If one service fails, it shouldn't bring down the entire system:

- Services are designed to handle failures gracefully
- Circuit breakers prevent cascading failures
- Fallback mechanisms provide degraded functionality
- The system remains partially operational even during failures

### Loose Coupling

**Loose coupling** means that services have minimal dependencies on each other. Changes to one service should not require changes to other services.

#### Why Loose Coupling Matters

1. **Independent Development**: Teams can work without waiting for other teams
2. **Independent Deployment**: Deploy one service without affecting others
3. **Fault Isolation**: Failures in one service don't cascade
4. **Technology Flexibility**: Change implementation without affecting consumers
5. **Easier Testing**: Test services in isolation

#### Achieving Loose Coupling

**1. API Contracts**: Define clear interfaces between services. As long as the API contract is maintained, internal implementation can change freely.

**2. Avoid Shared Databases**: Each service owns its data. Other services access data only through APIs.

**3. Asynchronous Communication**: Use message queues for non-time-critical operations. The sender doesn't wait for the receiver.

**4. Event-Driven Architecture**: Services publish events when something happens. Other services subscribe to events they care about.

**5. Versioned APIs**: When APIs change, support multiple versions to avoid breaking existing consumers.

#### Example of Tight vs Loose Coupling

**Tight Coupling (Bad):**

```python
# Order Service directly queries User database
def create_order(user_id, product_id):
    # BAD: Direct database access to another service's data
    user = UserTable.objects.get(id=user_id)
    if user.credit_limit > order_total:
        # Process order
```

**Loose Coupling (Good):**

```python
# Order Service calls User Service API
def create_order(user_id, product_id):
    # GOOD: Access data through API
    response = requests.get(f'http://user-service/api/users/{user_id}/')
    user_data = response.json()
    if user_data['credit_limit'] > order_total:
        # Process order
```

### Service Communication

Microservices need to communicate with each other. There are two main patterns:

#### Synchronous Communication

In synchronous communication, the caller waits for a response before proceeding.

**REST APIs**: The most common approach. Services expose REST endpoints and call each other using HTTP requests.

```python
# Product Service calling Inventory Service
import requests

def check_availability(product_id, quantity):
    response = requests.get(
        f'http://inventory-service/api/stock/{product_id}/',
        params={'quantity': quantity}
    )
    return response.json()['available']
```

**gRPC**: A high-performance RPC framework using Protocol Buffers. Faster than REST but more complex to implement.

**Pros of Synchronous:**

- Simple to understand and implement
- Immediate feedback
- Easy to debug

**Cons of Synchronous:**

- Tight temporal coupling (caller must wait)
- If the called service is slow or down, the caller is blocked
- Can create cascading failures

#### Asynchronous Communication

In asynchronous communication, the caller sends a message and continues without waiting for a response.

**Message Queues**: Services communicate through a message broker (RabbitMQ, Redis, Amazon SQS).

```python
# Order Service publishing an event
import pika

def order_created(order_data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='order_events')
    channel.basic_publish(
        exchange='',
        routing_key='order_events',
        body=json.dumps({'event': 'order_created', 'data': order_data})
    )
    connection.close()
```

```python
# Notification Service consuming the event
def callback(ch, method, properties, body):
    event = json.loads(body)
    if event['event'] == 'order_created':
        send_order_confirmation_email(event['data'])

channel.basic_consume(queue='order_events', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
```

**Event-Driven Architecture**: Services emit events when something significant happens. Other services react to these events.

**Pros of Asynchronous:**

- Loose temporal coupling
- Better resilience (messages are queued if service is down)
- Better scalability
- Natural fit for event-driven systems

**Cons of Asynchronous:**

- More complex to implement and debug
- Eventual consistency (data may not be immediately consistent)
- Requires message broker infrastructure

### API Gateway

An **API Gateway** is a server that acts as a single entry point for all client requests. Instead of clients calling individual microservices directly, they call the API Gateway, which routes requests to the appropriate services.

#### Why Use an API Gateway?

**1. Single Entry Point**: Clients only need to know about one URL (the gateway), not dozens of service URLs.

**2. Request Routing**: The gateway routes requests to the appropriate backend services based on the URL path, headers, or other criteria.

**3. Authentication and Authorization**: Centralized security. The gateway handles authentication (verifying identity) and authorization (checking permissions) before requests reach backend services.

**4. Rate Limiting**: Protect services from abuse by limiting the number of requests from each client.

**5. Request/Response Transformation**: Transform requests and responses. For example, aggregate data from multiple services into a single response.

**6. Load Balancing**: Distribute requests across multiple instances of a service.

**7. Caching**: Cache frequently requested data to reduce load on backend services.

**8. SSL Termination**: Handle HTTPS at the gateway level, allowing internal communication to use plain HTTP.

**9. Monitoring and Logging**: Centralized logging and monitoring of all API traffic.

#### API Gateway Architecture

```
                    ┌──────────────────────┐
                    │       Clients        │
                    │  (Web, Mobile, IoT)  │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │     API Gateway      │
                    │  ┌────────────────┐  │
                    │  │ Authentication │  │
                    │  │ Rate Limiting  │  │
                    │  │ Load Balancing │  │
                    │  │ Routing        │  │
                    │  └────────────────┘  │
                    └──────────┬───────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
┌───────▼───────┐    ┌────────▼────────┐    ┌───────▼───────┐
│ User Service  │    │ Product Service │    │ Order Service │
└───────────────┘    └─────────────────┘    └───────────────┘
```

#### Popular API Gateway Solutions

| Gateway             | Type          | Description                           |
| ------------------- | ------------- | ------------------------------------- |
| **Kong**            | Open Source   | Popular, extensible, based on NGINX   |
| **AWS API Gateway** | Cloud Service | Fully managed, integrates with AWS    |
| **NGINX**           | Open Source   | Can be configured as API gateway      |
| **Traefik**         | Open Source   | Container-native, automatic discovery |
| **Zuul**            | Open Source   | Netflix's gateway, Java-based         |
| **Express Gateway** | Open Source   | Built on Express.js                   |

### Advantages of Microservices

1. **Scalability**: Scale individual services based on demand
2. **Technology Flexibility**: Use the best tool for each job
3. **Faster Development**: Smaller codebases are easier to understand and modify
4. **Independent Deployment**: Deploy services without affecting others
5. **Fault Isolation**: Failures are contained within individual services
6. **Team Autonomy**: Teams own their services end-to-end
7. **Easier Maintenance**: Smaller, focused codebases are easier to maintain

### Disadvantages of Microservices

1. **Complexity**: Distributed systems are inherently more complex
2. **Network Latency**: Service-to-service calls add latency
3. **Data Consistency**: Maintaining consistency across services is challenging
4. **Debugging Difficulty**: Tracing issues across multiple services is harder
5. **Operational Overhead**: More services mean more things to deploy and monitor
6. **Testing Challenges**: Integration testing across services is complex
7. **Initial Cost**: Higher upfront investment in infrastructure and tooling

### When to Use Microservices

**Use Microservices When:**

- Your application is large and complex
- You have multiple development teams
- Different parts of the application have different scaling needs
- You need technology diversity
- You need to deploy parts of the application independently

**Stick with Monolith When:**

- Your application is small or simple
- You have a small team
- You're building a prototype or MVP
- You don't have the operational expertise for distributed systems
- Performance is critical (fewer network calls)

### Microservices Communication Example

Here's a simplified example showing how microservices might communicate in a Django REST Framework context:

#### User Service (Django)

```python
# user_service/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        """
        GET /api/users/{id}/
        This endpoint is called by other services to get user data.
        """
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response({
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'credit_limit': user.credit_limit
        })
```

#### Order Service (Django)

```python
# order_service/views.py
import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


# Configuration for other services
USER_SERVICE_URL = 'http://user-service:8001'
PRODUCT_SERVICE_URL = 'http://product-service:8002'


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request):
        """
        POST /api/orders/
        Creates an order by calling other microservices.
        """
        user_id = request.data.get('user_id')
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        # Call User Service to verify user and get credit limit
        try:
            user_response = requests.get(
                f'{USER_SERVICE_URL}/api/users/{user_id}/',
                timeout=5
            )
            user_response.raise_for_status()
            user_data = user_response.json()
        except requests.RequestException as e:
            return Response({
                'success': False,
                'message': 'User service unavailable'
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # Call Product Service to get product details and check stock
        try:
            product_response = requests.get(
                f'{PRODUCT_SERVICE_URL}/api/products/{product_id}/',
                params={'check_stock': quantity},
                timeout=5
            )
            product_response.raise_for_status()
            product_data = product_response.json()
        except requests.RequestException as e:
            return Response({
                'success': False,
                'message': 'Product service unavailable'
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # Business logic
        total_price = product_data['price'] * quantity

        if total_price > user_data['credit_limit']:
            return Response({
                'success': False,
                'message': 'Insufficient credit limit'
            }, status=status.HTTP_400_BAD_REQUEST)

        if not product_data.get('in_stock'):
            return Response({
                'success': False,
                'message': 'Product out of stock'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Create the order
        order = Order.objects.create(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity,
            total_price=total_price
        )

        return Response({
            'success': True,
            'message': 'Order created successfully',
            'data': {
                'order_id': order.id,
                'user': user_data['name'],
                'product': product_data['name'],
                'quantity': quantity,
                'total_price': total_price
            }
        }, status=status.HTTP_201_CREATED)
```

This example demonstrates:

- Service-to-service communication via REST APIs
- Error handling for service unavailability
- Aggregating data from multiple services
- Loose coupling (Order Service only knows User Service's API, not its database)

---

## 4.6 Building and Testing a Simple REST API

### Overview

This section provides a complete, step-by-step guide to building and testing a REST API using Django REST Framework. We will create a Task Management API that demonstrates all CRUD operations, proper API design, and thorough testing.

### Project Setup

#### Step 1: Create Project Directory and Virtual Environment

```bash
# Create project directory
mkdir task_api
cd task_api

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/Mac

# Install dependencies
pip install django djangorestframework
```

#### Step 2: Create Django Project and App

```bash
# Create Django project
django-admin startproject config .

# Create tasks app
python manage.py startapp tasks
```

#### Step 3: Configure Settings (config/settings.py)

```python
# config/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party
    'rest_framework',
    # Local
    'tasks',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

### Building the API

#### Step 4: Create the Model (tasks/models.py)

```python
# tasks/models.py

from django.db import models


class Task(models.Model):
    """
    Task model for the Task Management API.
    """
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='pending'
    )
    due_date = models.DateField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
```

#### Step 5: Create the Serializer (tasks/serializers.py)

```python
# tasks/serializers.py

from rest_framework import serializers
from django.utils import timezone
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model with validation.
    """
    # Read-only field showing time since creation
    age = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'priority', 'status',
            'due_date', 'completed_at', 'created_at', 'updated_at', 'age'
        ]
        read_only_fields = ['id', 'completed_at', 'created_at', 'updated_at']

    def get_age(self, obj):
        """Calculate how long ago the task was created."""
        delta = timezone.now() - obj.created_at
        days = delta.days
        if days == 0:
            hours = delta.seconds // 3600
            if hours == 0:
                minutes = delta.seconds // 60
                return f"{minutes} minute(s) ago"
            return f"{hours} hour(s) ago"
        return f"{days} day(s) ago"

    def validate_title(self, value):
        """Validate title is not empty."""
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value.strip()

    def validate_due_date(self, value):
        """Validate due_date is not in the past."""
        if value and value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    def validate(self, data):
        """Object-level validation."""
        # If status is completed, set completed_at
        if data.get('status') == 'completed':
            data['completed_at'] = timezone.now()
        return data


class TaskListSerializer(serializers.ModelSerializer):
    """
    Simplified serializer for list view.
    """
    class Meta:
        model = Task
        fields = ['id', 'title', 'priority', 'status', 'due_date']
```

#### Step 6: Create the Views (tasks/views.py)

```python
# tasks/views.py

from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer, TaskListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Task CRUD operations.

    Endpoints:
    - GET /api/tasks/ - List all tasks
    - POST /api/tasks/ - Create a new task
    - GET /api/tasks/{id}/ - Retrieve a task
    - PUT /api/tasks/{id}/ - Update a task
    - PATCH /api/tasks/{id}/ - Partial update
    - DELETE /api/tasks/{id}/ - Delete a task
    - POST /api/tasks/{id}/complete/ - Mark task as complete
    - GET /api/tasks/statistics/ - Get task statistics
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'priority', 'status']

    def get_serializer_class(self):
        """Use different serializer for list action."""
        if self.action == 'list':
            return TaskListSerializer
        return TaskSerializer

    def get_queryset(self):
        """
        Optionally filter by status and priority.
        """
        queryset = Task.objects.all()

        # Filter by status
        status_param = self.request.query_params.get('status')
        if status_param:
            queryset = queryset.filter(status=status_param)

        # Filter by priority
        priority = self.request.query_params.get('priority')
        if priority:
            queryset = queryset.filter(priority=priority)

        return queryset

    def list(self, request):
        """
        GET /api/tasks/
        List all tasks with optional filtering.
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'count': queryset.count(),
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        """
        GET /api/tasks/{id}/
        Retrieve a specific task.
        """
        task = self.get_object()
        serializer = self.get_serializer(task)
        return Response({
            'success': True,
            'data': serializer.data
        })

    def create(self, request):
        """
        POST /api/tasks/
        Create a new task.
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Task created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'success': False,
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        PUT /api/tasks/{id}/
        Update a task (full update).
        """
        task = self.get_object()
        serializer = self.get_serializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Task updated successfully',
                'data': serializer.data
            })

        return Response({
            'success': False,
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """
        PATCH /api/tasks/{id}/
        Partial update of a task.
        """
        task = self.get_object()
        serializer = self.get_serializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Task updated successfully',
                'data': serializer.data
            })

        return Response({
            'success': False,
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        DELETE /api/tasks/{id}/
        Delete a task.
        """
        task = self.get_object()
        task_title = task.title
        task.delete()

        return Response({
            'success': True,
            'message': f'Task "{task_title}" deleted successfully'
        })

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        """
        POST /api/tasks/{id}/complete/
        Mark a task as completed.
        """
        task = self.get_object()

        if task.status == 'completed':
            return Response({
                'success': False,
                'message': 'Task is already completed'
            }, status=status.HTTP_400_BAD_REQUEST)

        task.status = 'completed'
        task.completed_at = timezone.now()
        task.save()

        serializer = self.get_serializer(task)
        return Response({
            'success': True,
            'message': 'Task marked as completed',
            'data': serializer.data
        })

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """
        GET /api/tasks/statistics/
        Get task statistics.
        """
        total = Task.objects.count()
        pending = Task.objects.filter(status='pending').count()
        in_progress = Task.objects.filter(status='in_progress').count()
        completed = Task.objects.filter(status='completed').count()
        cancelled = Task.objects.filter(status='cancelled').count()

        high_priority = Task.objects.filter(priority='high').count()
        overdue = Task.objects.filter(
            due_date__lt=timezone.now().date(),
            status__in=['pending', 'in_progress']
        ).count()

        return Response({
            'success': True,
            'data': {
                'total': total,
                'by_status': {
                    'pending': pending,
                    'in_progress': in_progress,
                    'completed': completed,
                    'cancelled': cancelled
                },
                'high_priority': high_priority,
                'overdue': overdue,
                'completion_rate': f"{(completed/total*100):.1f}%" if total > 0 else "0%"
            }
        })
```

#### Step 7: Configure URLs (tasks/urls.py)

```python
# tasks/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
```

#### Step 8: Configure Project URLs (config/urls.py)

```python
# config/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request):
    """API documentation endpoint."""
    return Response({
        'message': 'Task Management API',
        'version': '1.0',
        'endpoints': {
            'tasks': {
                'list': 'GET /api/tasks/',
                'create': 'POST /api/tasks/',
                'retrieve': 'GET /api/tasks/{id}/',
                'update': 'PUT /api/tasks/{id}/',
                'partial_update': 'PATCH /api/tasks/{id}/',
                'delete': 'DELETE /api/tasks/{id}/',
                'complete': 'POST /api/tasks/{id}/complete/',
                'statistics': 'GET /api/tasks/statistics/',
            },
            'filters': {
                'by_status': '?status=pending|in_progress|completed|cancelled',
                'by_priority': '?priority=low|medium|high',
                'search': '?search=keyword',
                'ordering': '?ordering=created_at|-created_at|due_date|priority',
            }
        }
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('', api_root, name='api-root'),
]
```

#### Step 9: Run Migrations and Create Sample Data

```bash
# Create database tables
python manage.py makemigrations
python manage.py migrate

# Start the server
python manage.py runserver
```

Create sample data (run `python manage.py shell`):

```python
from tasks.models import Task
from datetime import date, timedelta

# Create sample tasks
Task.objects.create(
    title="Complete project documentation",
    description="Write comprehensive documentation for the API project",
    priority="high",
    status="in_progress",
    due_date=date.today() + timedelta(days=3)
)

Task.objects.create(
    title="Review pull requests",
    description="Review and merge pending pull requests",
    priority="medium",
    status="pending",
    due_date=date.today() + timedelta(days=1)
)

Task.objects.create(
    title="Setup CI/CD pipeline",
    description="Configure GitHub Actions for automated testing",
    priority="high",
    status="pending",
    due_date=date.today() + timedelta(days=7)
)

Task.objects.create(
    title="Write unit tests",
    description="Add unit tests for all API endpoints",
    priority="medium",
    status="pending"
)

Task.objects.create(
    title="Database optimization",
    description="Optimize database queries for better performance",
    priority="low",
    status="pending"
)

exit()
```

### Testing the API with Thunder Client

Now let's test all the API endpoints using Thunder Client:

#### Test 1: View API Documentation

1. Method: `GET`
2. URL: `http://localhost:8000/`
3. Expected: API documentation with all available endpoints

#### Test 2: List All Tasks

1. Method: `GET`
2. URL: `http://localhost:8000/api/tasks/`
3. Expected: List of all tasks with pagination

#### Test 3: Filter Tasks by Status

1. Method: `GET`
2. URL: `http://localhost:8000/api/tasks/`
3. Query tab: Add `status` = `pending`
4. Expected: Only pending tasks returned

#### Test 4: Filter Tasks by Priority

1. Method: `GET`
2. URL: `http://localhost:8000/api/tasks/`
3. Query tab: Add `priority` = `high`
4. Expected: Only high priority tasks returned

#### Test 5: Search Tasks

1. Method: `GET`
2. URL: `http://localhost:8000/api/tasks/`
3. Query tab: Add `search` = `documentation`
4. Expected: Tasks containing "documentation" in title or description

#### Test 6: Create a New Task

1. Method: `POST`
2. URL: `http://localhost:8000/api/tasks/`
3. Body tab → JSON:

```json
{
  "title": "Learn Django REST Framework",
  "description": "Complete the DRF tutorial and build a sample API",
  "priority": "high",
  "status": "pending",
  "due_date": "2026-02-15"
}
```

4. Expected: 201 Created with task data

#### Test 7: Retrieve a Specific Task

1. Method: `GET`
2. URL: `http://localhost:8000/api/tasks/1/`
3. Expected: Complete task details including computed `age` field

#### Test 8: Update a Task (PUT - Full Update)

1. Method: `PUT`
2. URL: `http://localhost:8000/api/tasks/1/`
3. Body tab → JSON:

```json
{
  "title": "Complete project documentation - Updated",
  "description": "Write comprehensive documentation for the API project including examples",
  "priority": "high",
  "status": "in_progress",
  "due_date": "2026-02-10"
}
```

4. Expected: 200 OK with updated task data

#### Test 9: Partial Update (PATCH)

1. Method: `PATCH`
2. URL: `http://localhost:8000/api/tasks/1/`
3. Body tab → JSON:

```json
{
  "status": "completed"
}
```

4. Expected: Task status updated, `completed_at` automatically set

#### Test 10: Mark Task as Complete (Custom Action)

1. Method: `POST`
2. URL: `http://localhost:8000/api/tasks/2/complete/`
3. No body needed
4. Expected: Task marked as completed

#### Test 11: Get Task Statistics

1. Method: `GET`
2. URL: `http://localhost:8000/api/tasks/statistics/`
3. Expected: Statistics showing counts by status, priority, and completion rate

#### Test 12: Delete a Task

1. Method: `DELETE`
2. URL: `http://localhost:8000/api/tasks/5/`
3. Expected: Success message confirming deletion

#### Test 13: Test Validation Errors

1. Method: `POST`
2. URL: `http://localhost:8000/api/tasks/`
3. Body tab → JSON:

```json
{
  "title": "",
  "priority": "invalid",
  "due_date": "2020-01-01"
}
```

4. Expected: 400 Bad Request with validation errors:
   - title: Cannot be empty
   - priority: Invalid choice
   - due_date: Cannot be in the past

#### Test 14: Order Tasks

1. Method: `GET`
2. URL: `http://localhost:8000/api/tasks/`
3. Query tab: Add `ordering` = `-priority` (descending by priority)
4. Expected: Tasks ordered by priority (high first)

### Using the DRF Browsable API

Open `http://localhost:8000/api/tasks/` in your browser. Django REST Framework's browsable API provides:

1. **Visual Interface**: A user-friendly web interface to interact with the API
2. **Built-in Forms**: Forms at the bottom of each page to create or update resources
3. **Raw Data View**: Toggle between formatted and raw JSON
4. **Authentication Support**: Login forms if authentication is configured
5. **OPTIONS Button**: View allowed HTTP methods and other metadata

### API Testing Best Practices

1. **Test All HTTP Methods**: Ensure GET, POST, PUT, PATCH, DELETE all work correctly

2. **Test Success Cases**: Verify valid inputs produce correct outputs

3. **Test Error Cases**: Verify invalid inputs return appropriate error messages

4. **Test Edge Cases**: Empty strings, null values, boundary values

5. **Test Authentication/Authorization**: Ensure protected endpoints are secured

6. **Test Pagination**: Verify pagination works with large datasets

7. **Test Filtering and Search**: Verify query parameters work correctly

8. **Test Status Codes**: Verify correct HTTP status codes are returned:
   - 200 OK for successful GET, PUT, PATCH
   - 201 Created for successful POST
   - 204 No Content or 200 for successful DELETE
   - 400 Bad Request for validation errors
   - 404 Not Found for missing resources
   - 500 Internal Server Error for server errors

9. **Document Your Tests**: Keep a collection of test requests for regression testing

10. **Automate Testing**: Use Django's test framework for automated API tests

### Summary

This chapter covered the essential concepts of Web Services and APIs:

- **4.1 API Basics**: Understanding what APIs are, their types, and how browser-server communication works
- **4.2 REST Principles**: The six constraints of REST, HTTP verbs, endpoint design, and status codes
- **4.3 JSON vs XML**: Comparing data exchange formats, their syntax, and when to use each
- **4.4 Data Validation and Serialization**: Using Django REST Framework serializers for data transformation and validation
- **4.5 Microservices**: Understanding microservices architecture, loose coupling, service communication, and API gateways
- **4.6 Building and Testing APIs**: Complete walkthrough of building and testing a REST API with Django REST Framework

These concepts form the foundation for building modern, scalable web applications that communicate through well-designed APIs.

---

## Full-Stack Project: Grocery Bud (React + Django REST Framework)

This section demonstrates a complete full-stack application with a React frontend and Django REST Framework backend. The Grocery Bud app allows users to manage a grocery shopping list with features to add, edit, delete, and mark items as completed.

### Project Overview

**Features:**

- Add new grocery items
- Mark items as completed/uncompleted
- Edit grocery item names
- Delete grocery items
- Persistent storage via REST API (not local storage)

**Architecture:**

```
┌───────────────────┐         ┌───────────────────┐
│  React Frontend   │  HTTP   │   Django Backend  │
│  (localhost:5173) │ ──────► │  (localhost:8000) │
│                   │  JSON   │                   │
│  - Vite + React   │ ◄────── │  - DRF API        │
│  - fetch API      │         │  - SQLite DB      │
└───────────────────┘         └───────────────────┘
```

---

## Part 1: Django REST Framework Backend

### Step 1: Create Backend Project

```bash
# Create project directory
mkdir grocery-api
cd grocery-api

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install django djangorestframework django-cors-headers

# Create Django project and app
django-admin startproject config .
python manage.py startapp groceries
```

### Step 2: Configure Settings (config/settings.py)

```python
# config/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party
    'rest_framework',
    'corsheaders',
    # Local
    'groceries',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Add this at the top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS settings - Allow React dev server
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

### Step 3: Create the Model (groceries/models.py)

```python
# groceries/models.py

from django.db import models


class GroceryItem(models.Model):
    """
    Model representing a grocery item in the shopping list.
    """
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
```

### Step 4: Create the Serializer (groceries/serializers.py)

```python
# groceries/serializers.py

from rest_framework import serializers
from .models import GroceryItem


class GroceryItemSerializer(serializers.ModelSerializer):
    """
    Serializer for GroceryItem model.
    """
    class Meta:
        model = GroceryItem
        fields = ['id', 'name', 'completed', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_name(self, value):
        """Ensure name is not empty."""
        if not value.strip():
            raise serializers.ValidationError("Item name cannot be empty.")
        return value.strip()
```

### Step 5: Create the Views (groceries/views.py)

```python
# groceries/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import GroceryItem
from .serializers import GroceryItemSerializer


class GroceryItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet for GroceryItem CRUD operations.

    Endpoints:
    - GET    /api/groceries/      - List all items
    - POST   /api/groceries/      - Create a new item
    - GET    /api/groceries/{id}/ - Retrieve an item
    - PUT    /api/groceries/{id}/ - Full update
    - PATCH  /api/groceries/{id}/ - Partial update (toggle completed, edit name)
    - DELETE /api/groceries/{id}/ - Delete an item
    """
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer

    def list(self, request):
        """GET /api/groceries/ - List all grocery items."""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST /api/groceries/ - Create a new grocery item."""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """PATCH /api/groceries/{id}/ - Update completed status or name."""
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """DELETE /api/groceries/{id}/ - Delete a grocery item."""
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### Step 6: Configure URLs (groceries/urls.py)

```python
# groceries/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroceryItemViewSet

router = DefaultRouter()
router.register(r'groceries', GroceryItemViewSet, basename='grocery')

urlpatterns = [
    path('', include(router.urls)),
]
```

### Step 7: Configure Project URLs (config/urls.py)

```python
# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('groceries.urls')),
]
```

### Step 8: Run Migrations and Start Server

```bash
# Create database tables
python manage.py makemigrations
python manage.py migrate

# Create some sample data (optional)
python manage.py shell
```

In the shell:

```python
from groceries.models import GroceryItem

GroceryItem.objects.create(name="milk", completed=True)
GroceryItem.objects.create(name="bread", completed=True)
GroceryItem.objects.create(name="eggs", completed=False)
GroceryItem.objects.create(name="butter", completed=False)

exit()
```

Start the server:

```bash
python manage.py runserver
```

The API is now running at `http://localhost:8000/api/groceries/`

### Testing the API with Thunder Client

**GET all items:**

- Method: `GET`
- URL: `http://localhost:8000/api/groceries/`

**Create an item:**

- Method: `POST`
- URL: `http://localhost:8000/api/groceries/`
- Body: `{"name": "cheese"}`

**Toggle completed:**

- Method: `PATCH`
- URL: `http://localhost:8000/api/groceries/1/`
- Body: `{"completed": true}`

**Update name:**

- Method: `PATCH`
- URL: `http://localhost:8000/api/groceries/1/`
- Body: `{"name": "whole milk"}`

**Delete item:**

- Method: `DELETE`
- URL: `http://localhost:8000/api/groceries/1/`

---

## Part 2: React Frontend with Fetch API

Now let's create the React frontend that communicates with the Django backend using the Fetch API.

### Step 1: Create Vite Project

```bash
cd Desktop
npm create vite@latest grocery-bud -- --template react
cd grocery-bud
npm install
npm install react-icons react-toastify
code .
```

### Step 2: Project Structure

```text
grocery-bud/
├── src/
│   ├── components/
│   │   ├── Form.jsx
│   │   ├── Form.css
│   │   ├── Items.jsx
│   │   ├── Items.css
│   │   ├── SingleItem.jsx
│   │   └── SingleItem.css
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
```

### Step 3: Setup Global Styles

**Create `src/index.css`**

```css
*,
::after,
::before {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: #eee;
  font-family: Helvetica, sans-serif;
  font-weight: 400;
  line-height: 1.2;
  color: #222;
}
```

### Step 4: Create SingleItem Component

**Create `src/components/SingleItem.jsx`**

```javascript
import { FiEdit, FiTrash2 } from "react-icons/fi";
import "./SingleItem.css";

const SingleItem = ({ item, editCompleted, removeItem, setEditId }) => {
  return (
    <div className="single-item">
      <input
        type="checkbox"
        checked={item.completed}
        onChange={() => editCompleted(item.id)}
      />
      <p
        style={{
          textTransform: "capitalize",
          textDecoration: item.completed ? "line-through" : "none",
        }}
      >
        {item.name}
      </p>

      <button
        className="btn icon-btn"
        type="button"
        onClick={() => setEditId(item.id)}
      >
        <FiEdit size={18} />
      </button>

      <button
        className="btn icon-btn remove-btn"
        type="button"
        onClick={() => removeItem(item.id)}
      >
        <FiTrash2 size={18} />
      </button>
    </div>
  );
};

export default SingleItem;
```

**Create `src/components/SingleItem.css`**

```css
.single-item {
  display: grid;
  grid-template-columns: auto 1fr auto auto;
  column-gap: 1rem;
  align-items: center;
}

.single-item .btn {
  cursor: pointer;
  color: #fff;
  background: #06b6d4;
  border: transparent;
  border-radius: 0.25rem;
  padding: 0.375rem 0.75rem;
  font-size: 0.75rem;
}

.single-item .btn:hover {
  background: #0e7490;
}

.single-item .remove-btn {
  background: #222;
}

.single-item .remove-btn:hover {
  background: #900e0e;
}
```

### Step 5: Create Items Component

**Create `src/components/Items.jsx`**

```javascript
import SingleItem from "./SingleItem";
import "./Items.css";

const Items = ({ items, editCompleted, removeItem, setEditId }) => {
  return (
    <div className="items">
      {items.map((item) => {
        return (
          <SingleItem
            key={item.id}
            item={item}
            editCompleted={editCompleted}
            removeItem={removeItem}
            setEditId={setEditId}
          />
        );
      })}
    </div>
  );
};

export default Items;
```

**Create `src/components/Items.css`**

```css
.items {
  margin-top: 2rem;
  display: grid;
  row-gap: 1rem;
}
```

### Step 6: Create Form Component

**Create `src/components/Form.jsx`**

```javascript
import { useState, useEffect } from "react";
import { toast } from "react-toastify";
import "./Form.css";

const Form = ({
  addItem,
  editItemId,
  updateItemName,
  itemToEdit,
  inputRef,
}) => {
  const [newItemName, setNewItemName] = useState("");

  useEffect(() => {
    if (itemToEdit) {
      setNewItemName(itemToEdit.name);
    } else {
      setNewItemName("");
    }
  }, [itemToEdit]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!newItemName) {
      toast.error("Please provide a value");
      return;
    }
    if (editItemId) {
      updateItemName(newItemName);
    } else {
      addItem(newItemName);
    }
    setNewItemName("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>grocery bud</h2>
      <div className="form-control">
        <input
          type="text"
          className="form-input"
          value={newItemName}
          ref={inputRef}
          placeholder="e.g. eggs"
          onChange={(event) => setNewItemName(event.target.value)}
        />
        <button type="submit" className="btn">
          {editItemId ? "edit item" : "add item"}
        </button>
      </div>
    </form>
  );
};

export default Form;
```

**Create `src/components/Form.css`**

```css
form h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  text-transform: capitalize;
  font-weight: normal;
}

.form-control {
  display: grid;
  grid-template-columns: 1fr 100px;
}

.form-input {
  width: 100%;
  padding: 0.375rem 0.75rem;
  border-radius: 0;
  border-top-left-radius: 0.25rem;
  border-bottom-left-radius: 0.25rem;
  border: 1px solid #ddd;
}

.form-input::placeholder {
  color: #aaa;
}

.form-control .btn {
  cursor: pointer;
  color: #fff;
  background: #06b6d4;
  border: transparent;
  border-radius: 0;
  border-top-right-radius: 0.25rem;
  border-bottom-right-radius: 0.25rem;
  padding: 0.375rem 0.75rem;
  text-transform: capitalize;
}

.form-control .btn:hover {
  background: #0e7490;
}
```

### Step 7: Create Main App Component with Fetch API

**Update `src/App.jsx`**

```javascript
import { useEffect, useRef, useState } from "react";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import Form from "./components/Form";
import Items from "./components/Items";
import "./App.css";

// API Base URL - Django backend
const API_URL = "http://localhost:8000/api/groceries/";

const App = () => {
  const [items, setItems] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [editId, setEditId] = useState(null);
  const inputRef = useRef(null);

  // Focus input when editing
  useEffect(() => {
    if (editId && inputRef.current) {
      inputRef.current.focus();
    }
  }, [editId]);

  // Fetch all items on component mount
  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await fetch(API_URL);
        if (!response.ok) {
          throw new Error("Failed to fetch items");
        }
        const data = await response.json();
        setItems(data);
      } catch (error) {
        toast.error("Error loading items");
        console.error("Fetch error:", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchItems();
  }, []);

  // Add new item
  const addItem = async (itemName) => {
    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name: itemName }),
      });

      if (!response.ok) {
        throw new Error("Failed to add item");
      }

      const newItem = await response.json();
      setItems([newItem, ...items]);
      toast.success("Item added to the list");
    } catch (error) {
      toast.error("Error adding item");
      console.error("Add error:", error);
    }
  };

  // Toggle completed status
  const editCompleted = async (itemId) => {
    const item = items.find((i) => i.id === itemId);
    if (!item) return;

    try {
      const response = await fetch(`${API_URL}${itemId}/`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ completed: !item.completed }),
      });

      if (!response.ok) {
        throw new Error("Failed to update item");
      }

      const updatedItem = await response.json();
      const newItems = items.map((i) => (i.id === itemId ? updatedItem : i));
      setItems(newItems);
    } catch (error) {
      toast.error("Error updating item");
      console.error("Update error:", error);
    }
  };

  // Remove item
  const removeItem = async (itemId) => {
    try {
      const response = await fetch(`${API_URL}${itemId}/`, {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error("Failed to delete item");
      }

      const newItems = items.filter((item) => item.id !== itemId);
      setItems(newItems);
      toast.success("Item deleted");
    } catch (error) {
      toast.error("Error deleting item");
      console.error("Delete error:", error);
    }
  };

  // Update item name
  const updateItemName = async (newName) => {
    try {
      const response = await fetch(`${API_URL}${editId}/`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name: newName }),
      });

      if (!response.ok) {
        throw new Error("Failed to update item");
      }

      const updatedItem = await response.json();
      const newItems = items.map((item) =>
        item.id === editId ? updatedItem : item,
      );
      setItems(newItems);
      setEditId(null);
      toast.success("Item updated");
    } catch (error) {
      toast.error("Error updating item");
      console.error("Update error:", error);
    }
  };

  if (isLoading) {
    return (
      <section className="section-center">
        <p style={{ textAlign: "center" }}>Loading...</p>
      </section>
    );
  }

  return (
    <section className="section-center">
      <ToastContainer position="top-center" />
      <Form
        addItem={addItem}
        updateItemName={updateItemName}
        editItemId={editId}
        itemToEdit={items.find((item) => item.id === editId)}
        inputRef={inputRef}
      />
      <Items
        items={items}
        editCompleted={editCompleted}
        removeItem={removeItem}
        setEditId={setEditId}
      />
    </section>
  );
};

export default App;
```

**Create `src/App.css`**

```css
.section-center {
  margin: 0 auto;
  margin-top: 8rem;
  max-width: 30rem;
  background: #fff;
  border-radius: 0.25rem;
  padding: 2rem;
}

.Toastify__toast {
  text-transform: capitalize;
}
```

### Step 8: Run Both Applications

**Terminal 1 - Start Django Backend:**

```bash
cd grocery-api
venv\Scripts\activate
python manage.py runserver
```

**Terminal 2 - Start React Frontend:**

```bash
cd grocery-bud
npm run dev
```

Visit `http://localhost:5173` to see your Grocery Bud app in action, now connected to the Django REST Framework backend!

---

## Key Differences: Local Storage vs Fetch API

| Aspect               | Local Storage  | Fetch API (Backend)        |
| -------------------- | -------------- | -------------------------- |
| **Data Persistence** | Browser only   | Server database            |
| **Data Sharing**     | Single browser | Any client can access      |
| **Storage Limit**    | ~5-10 MB       | Database capacity          |
| **Operations**       | Synchronous    | Asynchronous (async/await) |
| **Error Handling**   | Minimal        | Try/catch required         |
| **Offline Support**  | Works offline  | Requires network           |
| **Scalability**      | Limited        | Highly scalable            |

## Fetch API Operations Summary

### GET - Fetch All Items

```javascript
const response = await fetch(API_URL);
const data = await response.json();
```

### POST - Create Item

```javascript
const response = await fetch(API_URL, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: itemName }),
});
const newItem = await response.json();
```

### PATCH - Update Item

```javascript
const response = await fetch(`${API_URL}${itemId}/`, {
  method: "PATCH",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ completed: true }),
});
const updatedItem = await response.json();
```

### DELETE - Remove Item

```javascript
const response = await fetch(`${API_URL}${itemId}/`, {
  method: "DELETE",
});
// No response body for 204 status
```

---

## Summary

This full-stack Grocery Bud project demonstrates:

1. **Django REST Framework Backend:**
   - Model definition for grocery items
   - Serializer for data validation and transformation
   - ViewSet for CRUD operations
   - CORS configuration for cross-origin requests

2. **React Frontend with Fetch API:**
   - `useEffect` for fetching data on mount
   - `async/await` for all API operations
   - Proper error handling with try/catch
   - Loading states while fetching
   - Toast notifications for user feedback

3. **Full-Stack Integration:**
   - RESTful communication between frontend and backend
   - JSON data exchange
   - Real-time updates reflected in the database

This architecture is the foundation for building production-ready web applications with separate frontend and backend services.

---
