# Advanced API Project - Book API

## Overview
This Django REST Framework API manages books and authors. Each view has permissions applied to restrict certain operations to authenticated users.

## Views and Permissions

### BookListView
- **Purpose:** List all books
- **Permissions:** Read-only access (AllowAny)
- **Custom behavior:** Supports search and ordering

### BookDetailView
- **Purpose:** Retrieve a specific book by ID
- **Permissions:** Read-only access (AllowAny)

### BookCreateView
- **Purpose:** Create a new book
- **Permissions:** Authenticated users only (IsAuthenticated)
- **Custom behavior:** Validates publication_year cannot be in the future

### BookUpdateView
- **Purpose:** Update an existing book
- **Permissions:** Authenticated users only (IsAuthenticated)
- **Custom behavior:** Validates publication_year cannot be in the future

### BookDeleteView
- **Purpose:** Delete a book
- **Permissions:** Authenticated users only (IsAuthenticated)

## Authentication
- Basic Authentication using superuser credentials
- Example header: Authorization: Basic <Base64(username:password)>

## Testing
- Test views using Postman, curl, or PowerShell Invoke-WebRequest.
- Confirm permissions are enforced by attempting operations with and without credentials.

## Notes
- Future-year validation ensures publication_year is not greater than the current year.
- List and Detail views are accessible to everyone, while Create, Update, and Delete are restricted to authenticated users.
