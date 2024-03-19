## GoIT, Python WEB, Homework number 10 - Django, PostgreSQL, Docker, MongoDB

# Django Quotes Website

This project implements a website similar to http://quotes.toscrape.com using Django, PostgreSQL, Docker, and MongoDB.

## Homework Assignment Description
In this assignment, you are tasked with creating a Django website that mimics the functionality of http://quotes.toscrape.com. Additionally, you are required to implement user registration, login, and the ability for registered users to add authors and quotes to the site. Furthermore, you need to migrate the MongoDB database to PostgreSQL and implement various features like tag-based search, displaying popular tags, pagination, and data scraping directly into the website's database.

## Features
- User registration and login.
- Ability for registered users to add authors and quotes.
- Migration of MongoDB database to PostgreSQL.
- Access to each author's page without authentication.
- Viewing all quotes without authentication.
- Search functionality for quotes by tags.
- Displaying the top ten tags.
- Pagination for quotes.
- Data scraping functionality.

## Setup Instructions
1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd django-quotes-website`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up Docker containers for PostgreSQL and MongoDB.
5. Run migrations: `python manage.py migrate`
6. Start the Django development server: `python manage.py runserver`

## Usage
1. Visit the site and register/login.
2. Explore the available quotes and authors.
3. Add new authors and quotes if registered.
4. Utilize search functionality by tags.
5. View the top ten tags and navigate through pagination.
6. Scrape data by clicking the specified button.

## Contributors
- Babenko Anton https://github.com/bobantonbob/DZ10_web_gpt.git

