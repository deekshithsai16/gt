# Kalthi's Little World - Django Project

A full-stack Django project configured to serve "Kalthi's Little World" with backend file uploads for photos, videos, and MP3 music tracks.

## Quick Start (in VS Code)

1. Open this folder in VS Code (`File > Open Folder...`).
2. Open a new terminal in VS Code (`Ctrl + ` ` / `Cmd + ` `).
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply database migrations:
   ```bash
   python manage.py makemigrations memories
   python manage.py migrate
   ```
6. Create an admin superuser to log into the Django backend:
   ```bash
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```
8. Visit:
   - **Frontend Site**: http://127.0.0.1:8000/
   - **Admin Panel**: http://127.0.0.1:8000/admin/ (Upload photos & MP3 tracks here!)
