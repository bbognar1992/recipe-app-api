# Recipe-app-api

This repository contains a fully-featured REST API built with Django and Django REST Framework, containerized with Docker, and developed using Test-Driven Development (TDD). It serves as a comprehensive example of building APIs with a scalable, maintainable, and testable structure.

## Features

- **Django REST Framework**: Provides a robust and flexible toolkit for building Web APIs.
- **Test-Driven Development (TDD)**: Ensures all features are built alongside tests, improving code quality and maintainability.
- **Dockerized Setup**: Simplifies setup, scaling, and deployment, with Docker and Docker Compose.
- **Modular Design**: Separate Django apps for different functionalities, including `user`, `recipe`, and `core`.
- **Production Ready**: Ready for production use with clear separation between development and production dependencies.

## Project Structure

The project is organized into a modular structure:

```plaintext
./
├── Dockerfile                # Dockerfile for building the application container
├── LICENSE                   # License information
├── README.md                 # Project documentation (this file)
├── app                       # Django project directory
│   ├── app                   # Main project settings and URLs
│   │   ├── asgi.py
│   │   ├── settings.py       # Django settings
│   │   ├── urls.py           # Root URL configurations
│   │   └── wsgi.py
│   ├── core                  # Core functionality for the API
│   │   ├── models.py         # Data models
│   │   ├── admin.py          # Admin configurations
│   │   └── management        # Custom management commands
│   ├── recipe                # Recipe-related endpoints
│   │   ├── serializers.py    # Serializers for data validation and transformation
│   │   ├── views.py          # View logic for handling recipe requests
│   │   └── tests             # Test cases for recipe features
│   └── user                  # User management endpoints
│       ├── serializers.py    # Serializers for user data
│       ├── views.py          # Views for user-related requests
│       └── tests             # Test cases for user features
├── docker-compose.yml        # Docker Compose file for multi-container setup
├── requirements.txt          # Application dependencies
└── requirements.dev.txt      # Development dependencies
```

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker is installed. [Download Docker](https://www.docker.com/get-started)
- **Python 3.8+**: Required for Django and related dependencies

### Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Build and run the Docker containers**:
   ```bash
   docker-compose up --build
   ```

3. **Run the database migrations**:
   ```bash
   docker-compose run app sh -c "python manage.py migrate"
   ```

4. **Create a superuser**:
   ```bash
   docker-compose run app sh -c "python manage.py createsuperuser"
   ```

5. **Access the API**:
   The API will be accessible at `http://localhost:8000`.

### Running Tests

Tests are implemented to cover all functionalities and can be run using:
```bash
docker-compose run app sh -c "python manage.py test"
```

## Usage

The API includes various endpoints for managing users, authentication, recipes, and ingredients. You can explore and test endpoints using tools like `curl`, Postman, or directly in your browser.

## Technologies Used

- **Python**: Core programming language.
- **Django & Django REST Framework**: Main frameworks for building and managing the API.
- **Docker**: Containerizes the app, ensuring consistent environments.
- **SQLite/PostgreSQL**: For database storage (configured in `settings.py`).
- **Test-Driven Development**: Ensures each feature is built with corresponding tests for reliability and maintainability.

## License

This project is licensed under the terms of the MIT license.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements.