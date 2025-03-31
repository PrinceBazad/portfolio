# Portfolio Website

A modern and responsive portfolio website built with Django.

## Features

- Responsive design that works on all devices
- Dynamic content management through Django admin
- About section with multiple content sections
- Projects showcase
- Skills section with progress bars
- Contact form
- Social media integration
- Beautiful animations and transitions

## Technologies Used

- Python 3.x
- Django 5.x
- HTML5
- CSS3
- JavaScript

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Admin Panel

Access the admin panel at http://127.0.0.1:8000/admin/ to manage:
- Profile information
- About content
- Projects
- Skills
- Contact information

## License

This project is licensed under the MIT License - see the LICENSE file for details. 