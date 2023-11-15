# Calendar App

The Calendar App is a web application built with Django that allows users to select a date and fetch interesting facts associated with that date.

## Features

- Select a date using a date picker.
- Fetch interesting facts related to the selected date.
- View the facts in a bulleted list format.

## Project Structure

The project is organized into two main components:

1. **calendar_events**: Django app responsible for handling the core functionalities.
   - `admin.py`: Admin configurations for managing models in the Django admin interface.
   - `apps.py`: Configuration for the app.
   - `migrations`: Database migration files.
   - `models.py`: Defines data models for the app.
   - `templates`: HTML templates for rendering views.
   - `tests.py`: Unit tests for the app.
   - `urls.py`: URL patterns for the app.
   - `views.py`: Defines the views for rendering HTML pages.

2. **calendar_project**: Django project settings and configurations.
   - `asgi.py`: ASGI configuration.
   - `settings.py`: Project-wide settings.
   - `urls.py`: Project-level URL patterns.
   - `wsgi.py`: WSGI configuration.

## Getting Started

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd calendar-app
   python manage.py migrate
   python manage.py runserver
    ```

## Usage
1. Access the main page and select a date.
2. Click the "Fetch Facts" button to retrieve interesting facts.
3. View the facts in a bulleted list format.


