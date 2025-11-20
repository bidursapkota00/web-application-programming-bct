# Web Application Programming

![Bidur Sapkota](https://www.bidursapkota.com.np/_next/image?url=%2Fimages%2Fprofile3.png&w=48&q=75 "Bidur Sapkota - Developer")&nbsp;[Bidur Sapkota](https://www.bidursapkota.com.np/)

![Web Application Programming by Bidur Sapkota](/11-web-application-programming.jpg "Web Application Programming – Blog by Bidur Sapkota")

## Table of Contents

1. [Introduction](#introduction)
2. [JavaScript and Client-Side Programming](#javaScript-and-client-side-programming)

## Introduction

**1.1 Overview of Web Applications and Evolution of Web Architecture**
<br>

**World Wide Web (WWW)**

World Wide Web (WWW), commonly known as the Web, is an **information system enabling information to be shared over the Internet** through simplified ways meant to appeal to users beyond IT specialists and hobbyists, as well as documents and other web resources to be accessed over the Internet **according to specific rules, the Hypertext Transfer Protocol (HTTP).**
<br>

**What are Web Applications?**

- Web applications are software **programs that run on web servers and are accessed through web browsers over a network** (typically the internet).
- Unlike traditional desktop applications, they **don't require installation on the user's device.**

**Key Characteristics:**

- Accessible from any device with a browser
- Centralized data storage and processing
- Automatic updates without user intervention
- Platform-independent operation
  <br>

**Evolution of Web**

**Web 1.0 (1990s - Early 2000s) - Static Web**

- Read-only content
- Static HTML pages
- Limited interactivity
- One-way information flow from server to client
- Examples: Early corporate websites, online brochures (like newspaper with text and images)

**Web 2.0 (Mid 2000s - 2010s) - Dynamic & Social Web**

- User-generated content
- Rich user interfaces with AJAX
- Social networking and collaboration
- Two-way communication
- Corps monetizing your data
- Examples: Facebook, YouTube, Gmail

**Web 3.0 (2010s - Present) - Semantic & Intelligent Web**

- Artificial intelligence integration
- Semantic web technologies (web pages is structured and tagged in such a way that it can be read directly by computers)
- Users monetize their data
- Personalized experiences
- Machine learning and data analytics
- Decentralized applications (emerging)
- Examples: Voice assistants, recommendation systems, blockchain apps

**Modern Web Applications - Current Trends**

- Single Page Applications (SPAs)
- Progressive Web Apps (PWAs)
  - Features—like offline access, push notifications, and installability—that make it behave like a native mobile or desktop app.
- Microservices architecture
- Cloud-native applications taking full advantage of cloud computing's scalability and flexibility. (Google Colab, Google Docs, Figma)
- Real-time collaborative tools
- API-first design

---

**Evolution of Web Architecture**

- **Monolithic Architecture:**

  - The entire application (UI, business logic, data access) is built as a single, unified code base.
  - Easy to develop initially, simple to deploy (one file), easier debugging.
  - Hard to scale (must scale the whole app, not just bottlenecks),
  - A single bug can crash the whole system.

- **Microservices:**

  - Breaking the application into small, independent services that communicate via APIs (REST or gRPC). Each service can have its own database and technology stack.
  - Highly scalable, fault-tolerant (if one service fails, the app survives)
  - Enables independent teams to work on different features.
  - High complexity in DevOps, monitoring, and inter-service communication.

- **Event-Driven Architecture (EDA):**

  - Services do not call each other directly (coupling). Instead, they emit "events" (e.g., "Order Placed") to a message broker (like Kafka or RabbitMQ), and other services listen and react.
  - Extreme decoupling, real-time responsiveness, high throughput.
  - Hard to trace the flow of logic; requires complex infrastructure.

- **Serverless (FaaS):**
  - Developers write individual functions (e.g., AWS Lambda) triggered by events. The cloud provider manages the servers entirely.
  - Zero server management, pay-only-for-execution.
  - Cold start problem (to boot up containers), vendor lock-in, distributed complexity
    <br>

**Summary Table**

| Evolution Factor | **Past / Traditional** | **Transitional**       | **Modern / Cutting Edge**  |
| :--------------- | :--------------------- | :--------------------- | :------------------------- |
| **Generation**   | Web 1.0 (Read)         | Web 2.0 (Social/Cloud) | Web 3.0 (Decentralized/AI) |
| **Architecture** | Monolithic             | Microservices          | Event-Driven / Serverless  |
| **Rendering**    | Full Page SSR (PHP)    | Client-Side (SPA)      | Hybrid / Edge (Next.js)    |

---

**1.2 Client-Server Architecture**

Client-server architecture is a distributed computing model where tasks are divided between service providers (servers) and service requesters (clients).

**Components:**

**Client (Frontend):**

- User interface and presentation layer
- Sends requests to server
- Processes and displays responses
- Examples: Web browsers, mobile apps

**Server (Backend):**

- Processes client requests
- Manages business logic
- Handles data storage and retrieval
- Sends responses back to clients
- Examples: Web servers, application servers, database servers

### Request-Response Cycle

1. Client initiates a request
2. Request travels through the network
3. Server receives and processes the request
4. Server sends back a response
5. Client receives and displays the response

### Advantages

- Centralized data management
- Easy maintenance and updates
- Better security control
- Resource sharing among multiple clients
- Scalability

---

## HTTP (HyperText Transfer Protocol)

### What is HTTP?

HTTP is the foundation protocol of the World Wide Web, defining how messages are formatted and transmitted between web browsers and servers.

### Key Features

- **Stateless Protocol:** Each request is independent
- **Request-Response Model:** Client requests, server responds
- **Text-Based:** Human-readable format
- **Port:** Default port 80

### HTTP Methods (Verbs)

| Method  | Purpose        | Description                             |
| ------- | -------------- | --------------------------------------- |
| GET     | Retrieve data  | Requests data from server, read-only    |
| POST    | Submit data    | Sends data to server, creates resources |
| PUT     | Update data    | Updates existing resource completely    |
| PATCH   | Partial update | Updates part of existing resource       |
| DELETE  | Remove data    | Deletes specified resource              |
| HEAD    | Get headers    | Like GET but only retrieves headers     |
| OPTIONS | Get options    | Describes communication options         |

### HTTP Status Codes

**1xx - Informational:**

- 100 Continue
- 101 Switching Protocols

**2xx - Success:**

- 200 OK
- 201 Created
- 204 No Content

**3xx - Redirection:**

- 301 Moved Permanently
- 302 Found (Temporary Redirect)
- 304 Not Modified

**4xx - Client Errors:**

- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 429 Too Many Requests

**5xx - Server Errors:**

- 500 Internal Server Error
- 502 Bad Gateway
- 503 Service Unavailable

### HTTP Request Structure

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Accept-Language: en-US
```

### HTTP Response Structure

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234
Server: Apache/2.4

<html>...</html>
```

---

## HTTPS (HTTP Secure)

### What is HTTPS?

HTTPS is the secure version of HTTP, using encryption to protect data transmission between client and server.

### How it Works

1. **SSL/TLS Handshake:** Client and server establish secure connection
2. **Encryption:** Data is encrypted using SSL/TLS protocols
3. **Transmission:** Encrypted data travels over the network
4. **Decryption:** Recipient decrypts the data

### Key Features

- **Encryption:** Data is encrypted in transit
- **Authentication:** Verifies server identity using SSL certificates
- **Data Integrity:** Prevents data tampering
- **Port:** Default port 443

### SSL/TLS Certificates

- Issued by Certificate Authorities (CAs)
- Contains public key and website identity
- Browsers verify certificate validity
- Types: Domain Validation (DV), Organization Validation (OV), Extended Validation (EV)

### Benefits

- Protects sensitive data (passwords, credit cards)
- Builds user trust
- SEO benefits (Google ranks HTTPS higher)
- Required for modern web features (geolocation, camera access)

---

## URLs (Uniform Resource Locators)

### Structure of a URL

```
https://www.example.com:443/path/to/page?query=value#section

Protocol: https://
Subdomain: www
Domain: example
TLD: .com
Port: :443
Path: /path/to/page
Query String: ?query=value
Fragment: #section
```

### Components Explained

**Protocol (Scheme):**

- Defines how to access the resource
- Examples: http, https, ftp, mailto, file

**Domain Name:**

- Human-readable address
- Maps to IP address via DNS
- Can include subdomains (www, blog, api)

**Port:**

- Optional, defaults to 80 (HTTP) or 443 (HTTPS)
- Specifies which service on the server to connect to

**Path:**

- Location of specific resource on server
- Organized hierarchically with forward slashes

**Query String:**

- Starts with "?"
- Key-value pairs separated by "&"
- Example: ?id=123&category=books

**Fragment (Hash):**

- Starts with "#"
- Points to specific section within a page
- Not sent to server

### URL Encoding

Special characters must be encoded:

- Space: %20 or +
- &: %26
- =: %3D
- #: %23

---

## DNS (Domain Name System)

### What is DNS?

DNS is the internet's phone book, translating human-readable domain names into IP addresses that computers use to communicate.

### How DNS Works

1. **User enters URL:** www.example.com in browser
2. **Browser checks cache:** Looks for recently resolved IP
3. **Recursive resolver:** ISP's DNS server receives request
4. **Root nameserver:** Directs to TLD nameserver (.com)
5. **TLD nameserver:** Directs to authoritative nameserver
6. **Authoritative nameserver:** Returns IP address
7. **Browser connects:** Uses IP to reach website

### DNS Record Types

| Type  | Purpose                     | Example                    |
| ----- | --------------------------- | -------------------------- |
| A     | Maps domain to IPv4 address | example.com → 192.0.2.1    |
| AAAA  | Maps domain to IPv6 address | example.com → 2001:0db8::1 |
| CNAME | Alias to another domain     | www → example.com          |
| MX    | Mail exchange servers       | Mail server for email      |
| TXT   | Text information            | SPF, DKIM records          |
| NS    | Nameserver records          | Authoritative DNS servers  |

### DNS Hierarchy

```
Root (.)
  └── Top-Level Domain (.com, .org, .net)
      └── Second-Level Domain (example.com)
          └── Subdomain (www.example.com)
```

### DNS Caching

- **Browser cache:** Short-term local storage
- **OS cache:** System-level DNS cache
- **ISP cache:** Service provider's DNS servers
- **TTL (Time To Live):** Determines cache duration

---

## Web Browsers

### What is a Web Browser?

A web browser is a software application that retrieves, presents, and navigates information resources on the World Wide Web.

### Popular Browsers

- Google Chrome
- Mozilla Firefox
- Safari
- Microsoft Edge
- Opera
- Brave

### Browser Components

**1. User Interface:**

- Address bar
- Back/forward buttons
- Bookmarks
- Tabs and windows

**2. Browser Engine:**

- Marshals actions between UI and rendering engine
- Queries and manipulates rendering engine

**3. Rendering Engine:**

- Displays requested content
- Parses HTML and CSS
- Examples: Blink (Chrome), Gecko (Firefox), WebKit (Safari)

**4. Networking:**

- Handles HTTP/HTTPS requests
- Manages cookies
- Implements caching

**5. JavaScript Engine:**

- Parses and executes JavaScript code
- Examples: V8 (Chrome), SpiderMonkey (Firefox)

**6. Data Storage:**

- Cookies
- LocalStorage
- SessionStorage
- IndexedDB
- Cache API

### How Browsers Render Pages

1. **Parse HTML:** Creates DOM (Document Object Model) tree
2. **Parse CSS:** Creates CSSOM (CSS Object Model) tree
3. **Construct Render Tree:** Combines DOM and CSSOM
4. **Layout:** Calculates positions and sizes
5. **Paint:** Draws pixels on screen
6. **Composite:** Combines layers for final display

### Browser Features

**Developer Tools:**

- Inspect HTML/CSS
- Debug JavaScript
- Monitor network activity
- Analyze performance

**Security Features:**

- Same-origin policy
- HTTPS enforcement
- Pop-up blockers
- Phishing protection

**Modern Capabilities:**

- Progressive Web App support
- Service Workers
- WebRTC for real-time communication
- WebAssembly for high-performance code
- Geolocation API
- Notifications API

---

## JavaScript and Client-Side Programming
