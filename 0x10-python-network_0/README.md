# Network

## URL

URL - Uniform Resource Locator, an address on the web.
It's a specific way of referencing a resource, like a webpage, image, or video, on the internet.

### reading a URL

URL is like a roadmap to specific location on the internet:

1. Scheme: indicates the protocol used - http/https
2. domain name: like the main address
3. path: specifies the location of a specific file/resource within the web's structure.
4. parameters:  like additional instructions appended to the URL with a question mark ("?") followed by key-value pairs separated by ampersands ("&").
5. anchor: preceded by a hash symbol ("#"), links to a specific section within a webpage.  It's not essential for the page to load but helps jump to a particular spot.  For instance, a long webpage might have an anchor linking to its "Conclusion" section.

## HTTP

HTTP - Hypertext Transfer Protocol, foundation of communication on the web.
language that web browsers and servers use to talk to each other.

### scheme for a HTTP URL

it indicates the protocol used to access the resource.

### domain name

the address of a website on the internet.
It's like a nickname for a website's complex numerical address, which is called an IP address.

### sub-domain name

an optional part of a domain name that appears before the main domain name itself. It acts like a further categorization or organization within a website.

subdomain would be like an apartment number within that address. For instance, in "mail.google.com", "mail" is the subdomain specifying the email section of the overall Google website.

### port number in URL

the port number is specified after the hostname and separated by a colon.

`protocol://hostname:port/path`

* Default ports:
 By default, certain protocols have specific ports they use. For instance, HTTP traffic typically uses port 80, and HTTPS traffic uses port 443.  If you don't specify a port number in a URL for these protocols, the browser automatically assumes the default port.

* Importance:
 Specifying the port number is important when a server runs multiple services on different ports.  Without the port number, the browser wouldn't know which service to connect to.

```bash
http://example.com:8080/path/to/resource
```

### query string

also known as a URL parameter string, is a part of a URL that attaches information to the end of a web address.

`https://www.example.com/search?q=flowers&sort=price`

eg:

* `https://www.example.com/search` is the base URL.
* `?` indicates the start of the query string.
* `q=flowers` is the first parameter, specifying a search query for "flowers".
* `&sort=price` is the second parameter, indicating sorting by price.

## HTTP request

HTTP (Hypertext Transfer Protocol) request is a message sent by a client (typically a web browser or an application) to a server, requesting a specific action or resource.

consists of the following components:

1. request line:

    * specifies the HTTP method (such as GET, POST, PUT, DELETE, etc.)
    * the resource being requested (such as a URL or path)
    * the version of the HTTP protocol being used

    ```bash
    GET /example/resource HTTP/1.1
    ```

2. Headers:

    provide additional information about the request or the client making the request.
    can include information such as the user agent (the client software), content type, authentication credentials, and more

    Headers are key-value pairs separated by a colon.

    ```bash
    Host: www.example.com
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36
    ```

3. Optional Body:
    HTTP methods (such as POST, PUT, PATCH) may include a message body.
    which contains additional data sent by the client to the server.

    in a POST request, the body might contain form data or JSON payload.

    ```bash
    GET /example/resource HTTP/1.1
    Host: www.example.com
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    ```

    In this example:

    * client is making a GET request for the resource /example/resource from the server `www.example.com.`
    * client's user agent is Chrome running on Windows 10.
    * client indicates that it can accept HTML, XHTML, XML, WebP images, and more.

## HTTP response

An HTTP (Hypertext Transfer Protocol) response is a message sent by a server to a client (such as a web browser or an application) in response to an HTTP request.

It contains the data requested by the client or provides information about the success or failure of the request.

consists of the following components:

1. status line:
    contains the HTTP version, a numeric status code indicating the outcome of the request, and a brief textual description of the status.

    ```bash
    HTTP/1.1 200 OK
    ```

2. headers:
    headers provide additional information about the response.
    They include details such as the content type, content length, server information, caching directives,

    ```bash
    Content-Type: text/html; charset=UTF-8
    Content-Length: 1234
    Server: Apache
    ```

3. Optional Body:
    body of the response contains the requested data or additional information sent by the server.

    in a response to a GET request for an HTML page, the body would contain the HTML content of the page.

    ```bash
    HTTP/1.1 200 OK
    Content-Type: text/html; charset=UTF-8
    Content-Length: 1234
    Server: Apache

    <!DOCTYPE html>
    <html>
    <head>
    <title>Example Page</title>
    </head>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </html>
    ```

    in the example:

    * server is responding with a status code 200 OK, indicating that the request was successful.
    * response includes a Content-Type header specifying that the content is HTML, a Content-Length header indicating the size of the response body, and a Server header indicating the server software.
    * body of the response contains an HTML document with a simple "Hello, World!" message.

## HTTP Cookie

HTTP cookie (commonly referred to as a "cookie") is a small piece of data sent by a web server to a web browser and stored locally on the user's device.

They enable websites to remember user preferences, track user interactions, and maintain user sessions.

Cookies typically consist of a name-value pair and optional attributes such as expiration time, domain, and path.

While cookies provide valuable functionality for web applications, they also raise privacy concerns, as they can be used to track users across websites and collect personal information without their consent.

## make a request with cURL

To make a request using cURL (Client URL), you can use the curl command-line tool, which is available on most Unix-like operating systems (including Linux and macOS) and can also be installed on Windows.

```bash
curl [options] [URL]
```

```bash
curl https://www.example.com
```

This command will send a GET request to `https://www.example.com` and display the response body on the terminal.

### options in cURL

* `-X, --request`: Specifies the HTTP method to use (e.g., GET, POST, PUT, DELETE).
* `-H, --header`: Adds a custom header to the request (e.g., -H "Content-Type: application/json").
* `-d, --data`: Sends data in the request body for methods such as POST or PUT.
* `-o, --output`: Specifies a file to write the response body to instead of displaying it on the terminal.
* `-v, --verbose`: Displays verbose output, including information about the request and response headers.

example of making a POST request with cURL and sending JSON data:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' https://www.example.com/api
```
