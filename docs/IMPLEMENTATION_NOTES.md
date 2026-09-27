# Implementation Notes

## Project

Pocket Smart AI is a FastAPI-based smart budget and recommendations assistant.

## Backend

The application uses:

- FastAPI for the web API
- SQLAlchemy for database operations
- SQLite for local data storage
- Pydantic for request validation
- Passlib and bcrypt for password hashing

## AI

Google Gemini is used to generate budget recommendations based on the user's income and expenses.

## Frontend

The application uses:

- Jinja2 templates
- HTML
- CSS
- JavaScript

The static files are stored in:

```text
app/static/