# FastAPI_blogs
This is a simple blog API built using FastAPI, MongoDB, and Docker.

Setup Instructions
Clone the repository:

bash

git clone <repository-url>
Navigate to the project directory:

bash

cd fastapi-blog-api
Build and run the Docker containers:



docker-compose up --build
API Endpoints
Authentication
Register New User
URL: /register/
Method: POST
Description: Registers a new user.
Body:
json

{
    "username": "example_user",
    "email": "user@example.com",
    "password": "password123",
    "tags": ["tag1", "tag2"]
}
Response:
json

{
    "access_token": "your-access-token",
    "token_type": "bearer"
}
Login
URL: /token/
Method: POST
Description: Logs in an existing user.
Body:
json

{
    "username": "example_user",
    "password": "password123"
}
Response:
json

{
    "access_token": "your-access-token",
    "token_type": "bearer"
}
User Profile
Get User Profile
URL: /profile/
Method: GET
Description: Retrieves the profile of the currently logged-in user.
Headers:
makefile

Authorization: Bearer your-access-token
Response:
json

{
    "username": "example_user",
    "email": "user@example.com",
    "tags": ["tag1", "tag2"]
}
Blog Operations
Create Blog
URL: /blogs/
Method: POST
Description: Creates a new blog post.
Headers:
makefile

Authorization: Bearer your-access-token
Body:
json

{
    "title": "Example Blog Title",
    "content": "This is the content of the blog post.",
    "tags": ["tag1", "tag2"]
}
Response:
json

{
    "message": "Blog created successfully"
}
Get All Blogs
URL: /blogs/
Method: GET
Description: Retrieves all blog posts.
Response:
json

[
    {
        "title": "Example Blog Title",
        "content": "This is the content of the blog post.",
        "author": "example_user",
        "tags": ["tag1", "tag2"]
    },
    ...
]
Get Blog by ID
URL: /blogs/{post_id}
Method: GET
Description: Retrieves a specific blog post by its ID.
Response:
json

{
    "title": "Example Blog Title",
    "content": "This is the content of the blog post.",
    "author": "example_user",
    "tags": ["tag1", "tag2"]
}
Update Blog
URL: /blogs/{post_id}
Method: PUT
Description: Updates an existing blog post.
Headers:
makefile

Authorization: Bearer your-access-token
Body:
json

{
    "title": "Updated Blog Title",
    "content": "Updated content of the blog post.",
    "tags": ["updated_tag1", "updated_tag2"]
}
Response:
json

{
    "message": "Blog updated successfully"
}
Delete Blog
URL: /blogs/{post_id}
Method: DELETE
Description: Deletes a blog post by its ID.
Headers:
makefile

Authorization: Bearer your-access-token
Response:
json

{
    "message": "Blog deleted successfully"
}
Dashboard
Get Dashboard
URL: /dashboard/
Method: GET
Description: Retrieves blogs matching user's followed tags sorted by relevance.
Headers:
makefile

Authorization: Bearer your-access-token
Query Parameters:
page: Page number (default: 1)
page_size: Number of blogs per page (default: 10)
Response:
json

[
    {
        "title": "Example Blog Title",
        "content": "This is the content of the blog post.",
        "author": "example_user",
        "tags": ["tag1", "tag2"]
    },
    ...
]