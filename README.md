# Features
* ⁠Customer Management: Register and manage customer details.
* ⁠Dish Management: Add and categorize dishes with descriptions and prices.
* ⁠Order Processing: Create, update, and track customer orders with order items and total price calculations.
* ⁠Reservations: Handle table reservations with availability validation.
* ⁠Table Management: Assign and manage tables within the restaurant.
# Installation
## Prerequisites
Ensure you have the following installed:
* ⁠Python 3.10+
* ⁠Django
* ⁠Django REST Framework
* ⁠SQLite (default)
# Setup
1.⁠ ⁠Clone the repository:
```
git clone https://github.com/immarcosmorais/restaurant-django-api.git
cd restaurant-order-management
```
3.⁠ ⁠Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
4.⁠ ⁠Install depedencies:
```
pip install -r requirements.txt
```
5.⁠ ⁠Apply databases migrations:
```
python manage.py migrate
```
6.⁠ ⁠Create a supersuser to admin access:
```
python manage.py createsuperuser
```
7.⁠ ⁠Run the development server:
```
python manage.py runserver
```
# Technologies Used
* Django (Backend framework)
* Django REST Framework (API development)
* SQLite (Default database, can be replaced with PostgreSQL)
* Postman (API testing)
