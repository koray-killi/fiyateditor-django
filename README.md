# 🌶️ Price Editor Django 🍅

📊 Agricultural product price tracking and visualization system 📈

## 📋 About the Project

Price Editor is a Django web application designed to monitor, record, and visualize the daily prices of agricultural products (vegetables) through visuals. The application tracks price changes (increase, decrease, stable) and displays these changes visually.

This project is a version of an application originally developed using the Flask framework, ported to Django.

## ✨ Features

-   🥬 Categorize different types of vegetables (pepper, tomato, cucumber, eggplant, zucchini)
-   🔄 Compare previous and current prices
-   📊 Visually track price changes (increase ⬆️, decrease ⬇️, stable ➡️)
-   🖼️ Automatically generate price information in visual format
-   💾 Store product prices in the database

## 🗂️ Project Structure
```
fiyateditor-django/
├── FiyatEditor/
│   ├── FiyatEditor/           # Django project main directory
│   │   ├── init.py
│   │   ├── asgi.py
│   │   ├── settings.py        # Django configuration file
│   │   ├── urls.py            # Main URL routing
│   │   └── wsgi.py
│   ├── Main/                  # Main application directory
│   │   ├── init.py
│   │   ├── admin.py           # Admin panel configuration
│   │   ├── apps.py
│   │   ├── models.py          # Data models
│   │   ├── static/            # Static files (CSS, JS, images)
│   │   │   └── pillow/        # Image templates and fonts
│   │   ├── templates/         # HTML templates
│   │   ├── tests.py           # Test file
│   │   ├── urls.py            # Application URL routing
│   │   ├── utils.py           # Helper functions and visualization
│   │   └── views.py           # View functions
│   ├── db.sqlite3             # SQLite database
│   ├── manage.py              # Django management scripts
│   └── test.py                # Additional test file
├── venv/                      # Virtual environment folder
└── requirements.txt           # Dependencies list
```
## 🚀 Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/username/fiyateditor-django.git](https://github.com/username/fiyateditor-django.git)
    cd fiyateditor-django
    ```
2.  Create and activate a virtual environment:
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Linux/macOS
    python -m venv venv
    source venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Apply database migrations:
    ```bash
    cd FiyatEditor
    python manage.py migrate
    ```
5.  Start the application:
    ```bash
    python manage.py runserver
    ```
6.  View the application in your browser at `http://127.0.0.1:8000/`.

## 🎮 Usage

1.  On the main page, you can enter the previous and current prices for each vegetable type.
2.  Enter the date information and submit the form.
3.  The system will automatically generate a visual based on the entered prices.
4.  The generated visual will be displayed on the success page.

## 📦 Requirements

-   Python 3.8+
-   Django 4.0+
-   Pillow 9.0+ (For image processing)
-   Other dependencies are listed in the `requirements.txt` file.

## 🤝 Contributing

1.  Fork the project
2.  Create your Feature Branch (`git checkout -b feature/amazing-feature`)
3.  Commit your Changes (`git commit -m 'Add some amazing feature'`)
4.  Push to the Branch (`git push origin feature/amazing-feature`)
5.  Open a Pull Request

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## Contact

Project owner: [Your Name](https://github.com/username)

Project link: [https://github.com/username/fiyateditor-django](https://github.com/username/fiyateditor-django)
