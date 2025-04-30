Assignment 4 – Number Statistics Web Application:

Objective:

To build a Django web application that allows users to input or upload a list of numbers and return statistical data such as sum, mean, median, mode, range, prime numbers, and Armstrong numbers. The application also includes a cart system to track unique numbers entered, with a user-friendly UI.

Features Implemented:

- Input field and file upload support for number entry (comma-separated).
- Cart button showing count of unique numbers.
- Results page displaying:
  -  Sum
  -  Mean
  -  Median
  -  Mode
  -  Range
  -  Prime numbers
  -  Armstrong numbers
- A cart page displaying unique numbers in square containers.
- Clear Cart option.
- Responsive UI with background image and centered, transparent content box.

Technologies Used:

- Django 5.2
- Python 3.13
- HTML5 & CSS3
- Sessions for cart data

Folder Structure:

assignment/
├── assignment/              
├── Statistics/              
│   ├── static/
│   │   └── Statistics/
│   │       ├── css/
│   │       │   └── styles.css
│   │       └── images/
│   │           └── bgas4-1.png
│   ├── templates/
│   │   └── Statistics/
│   │       ├── homepage.html
│   │       ├── results.html
│   │       └── cart.html
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── ...
├── db.sqlite3
└── manage.py


1. Setup Environment

cd assignment
python3 -m venv env
source env/bin/activate  
pip install django (If not installed)
```

2. Run the Server

python3 manage.py runserver


3. Open in Browser
Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
