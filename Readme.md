# FastAPI Demo App

This is a demo application built with [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance) web framework for building APIs with Python 3.9+ based on standard Python type hints. The project is structured to follow best practices for scalability and maintainability.

## Project Structure

The project is organized as follows:

```
FastAPI-DemoApp/
├── app/
│   ├── main.py                # Entry point for the FastAPI application
│   ├── api/                   # API-related modules
│   │   ├── dependencies.py    # Dependency injection for routes
│   │   └── v1/                # API version 1
│   │       └── user_router.py # User-related API routes
│   ├── celery_app/            # Celery configuration and tasks
│   │   ├── chains.py          # Celery task chains
│   │   ├── tasks.py           # Celery tasks
│   │   └── workers.py         # Celery worker setup
│   ├── core/                  # Core application settings and security
│   │   ├── config.py          # Application configuration
│   │   └── security.py        # Security utilities
│   ├── db/                    # Database setup and initialization
│   │   ├── base.py            # Base models for the database
│   │   ├── init_db.py         # Database initialization logic
│   │   └── session.py         # Database session management
│   ├── models/                # ORM models
│   │   └── user.py            # User model
│   ├── repository/            # Data access layer
│   │   └── user_repo.py       # User repository for database operations
│   ├── schemas/               # Pydantic schemas
│   │   ├── user_request.py    # Request schemas for user endpoints
│   │   └── user_response.py   # Response schemas for user endpoints
│   ├── service/               # Business logic layer
│   │   └── user_service.py    # User-related business logic
```

## Features

- **FastAPI**: High-performance API framework with automatic OpenAPI documentation.
- **Database Integration**: SQLAlchemy for ORM and database session management.
- **Celery**: Asynchronous task queue for background jobs.
- **Modular Design**: Separation of concerns with clear layers for API, services, repositories, and schemas.
- **Dependency Injection**: Simplified management of dependencies using FastAPI's built-in tools.
- **Pydantic**: Data validation and serialization using Pydantic models.

## Requirements

- Python 3.9+
- PostgreSQL (or any other database supported by SQLAlchemy)
- Redis (for Celery task queue)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/FastAPI-DemoApp.git
   cd FastAPI-DemoApp
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   Create a `.env` file in the root directory and configure the following variables:

   ```env
   DATABASE_URL=postgresql+psycopg2://user:password@localhost/dbname
   REDIS_URL=redis://localhost:6379/0
   ```

5. Initialize the database:

   ```bash
   python app/db/init_db.py
   ```

6. Start the FastAPI application:

   ```bash
   uvicorn app.main:app --reload
   ```

7. (Optional) Start the Celery worker:

   ```bash
   celery -A app.celery_app.workers worker --loglevel=info
   ```

## API Documentation

Once the application is running, you can access the API documentation at:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Celery](https://docs.celeryproject.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)