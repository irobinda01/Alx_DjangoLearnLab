# This is a basic django project setup for development.
## I hope it works well.

## Permissions and Groups

### Groups
- **Viewers**: Can view articles.
- **Editors**: Can view, create, and edit articles.
- **Admins**: Can view, create, edit, and delete articles.

### Custom Permissions
- `can_view`: Allows viewing articles.
- `can_create`: Allows creating articles.
- `can_edit`: Allows editing articles.
- `can_delete`: Allows deleting articles.

### Testing
- Assign users to groups in the admin panel.
- Verify permissions by attempting actions like creating, editing, or deleting articles.


## Security Measures Implemented

- **DEBUG Disabled**: Ensures no sensitive information is exposed in production.
- **Secure Headers**: Configured XSS, content type, and frame protections.
- **CSRF Protection**: CSRF tokens included in all forms.
- **Data Validation**: Used Django ORM and forms to prevent SQL injection and sanitize inputs.
- **Content Security Policy (CSP)**: Configured CSP to prevent XSS attacks.
