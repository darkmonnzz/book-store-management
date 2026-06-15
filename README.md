# Bookstore Management System

A menu-driven Python-MySQL application to manage a bookstore with separate functionalities for customers and employees.

## Features
- 📚 View all books in inventory
- 🔍 Search books by Book ID
- 💡 Customer book suggestion system
- 🧾 Automated bill/receipt generation with quantity and total price calculation
- 🔐 Password-protected employee portal (add/delete books)
- 📇 Contact information section

## Tech Stack
Python · MySQL · mysql-connector-python

## Database
- Database: `school`
- Table: `BookList`
- Fields: Book ID, Name, Author, Price, Quantity, Genre

## How to Run
1. Install MySQL and create a database named `school`
2. Create the `BookList` table with fields: b_id, name, author, price, quantity, genre
3. Install connector:
   pip install mysql-connector-python
4. Update host, user and password in the code
5. Run:
   python bookstore.py

## Project By
Purva Jain — GTBIT, Delhi# book-store-management
