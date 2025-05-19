# GIS Flask

![GIS Flask Banner](https://storage.googleapis.com/replit/images/1747665498859_1b4d538a99a9d3f9c7dc9b35b3cb3be9.png)

A Flask-based GIS backend package with JWT authentication, role-based permissions, interactive maps, health monitoring, and API documentation.

## Features

- **JWT Authentication**: Secure authentication using JSON Web Tokens (JWT) for API access control
- **Role-Based Access Control**: Comprehensive permissions system for secure user access management
- **Interactive Maps**: Integration with Folium for interactive map visualizations
- **API Documentation**: Automatic Swagger/OpenAPI documentation
- **PostgreSQL Database**: Robust data storage with UUID primary keys
- **Health Monitoring**: Built-in health check endpoint
- **Modular Architecture**: Well-organized codebase with clear separation of concerns

## Getting Started

### Prerequisites

- Python 3.7+
- PostgreSQL database
- Required Python packages (see installation)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd gisflask
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   # Database connection
   export DATABASE_URL=postgresql://username:password@localhost:5432/gisflask
   
   # JWT secret
   export JWT_SECRET_KEY=your-secret-key
   
   # Session secret
   export SESSION_SECRET=your-session-secret
   ```

5. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. Run the application:
   ```bash
   python run.py
   ```

The application will be available at `http://localhost:5000`.

## Project Structure

```
app/
├── auth/               # Authentication related modules
│   ├── routes.py       # Auth endpoints (register, login, etc.)
│   ├── schemas.py      # Data validation schemas
│   └── utils.py        # Auth helper functions
├── main/               # Main application modules
│   ├── routes.py       # Main routes including map endpoints
│   └── schemas.py      # Data validation schemas
├── users/              # User management (placeholder)
│   └── routes.py       # User CRUD operations
├── products/           # Product management (placeholder) 
│   └── routes.py       # Product CRUD operations
├── services/           # Service modules
│   └── email.py        # Email service
├── templates/          # HTML templates
│   └── ...            
├── __init__.py         # Application factory
├── config.py           # Configuration settings
├── extensions.py       # Flask extensions
├── models.py           # Database models
└── utils.py            # Utility functions
```

## Key Components

### Authentication System

The application uses JWT-based authentication:

- **Registration**: Create a new user account
- **Login**: Authenticate and receive access/refresh tokens
- **Token Refresh**: Get a new access token using refresh token
- **Protected Routes**: Access control using JWT authentication

Default admin credentials:
- Username: `admin`
- Password: `admin123`

### Role-Based Access Control

The application implements a flexible permission system:

- **Roles**: Admin, User, etc.
- **Permissions**: Fine-grained control over actions
- **Access Control Decorators**: `@jwt_required()`, `@admin_required`

### Map Visualization

Interactive maps using Folium:

- View maps at `/map`
- Customize center coordinates and zoom level
- Save map preferences per user

### API Documentation

Swagger/OpenAPI documentation available at `/docs/`.

### Extending the Application

The application includes placeholder modules for adding custom functionality:

- **Users Module**: Example of user management functionality
- **Products Module**: Example of product management functionality

Each module includes placeholder templates and commented example code to help you understand how to implement your own features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask and its extensions
- Folium for interactive maps
- Swagger/OpenAPI for API documentation