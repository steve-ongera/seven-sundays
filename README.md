# Seven Sundays E-commerce Platform

A modern e-commerce platform built with Django for Seven Sundays, featuring a complete online shopping experience with product catalog, shopping cart, user authentication, and order management.

## 🌟 Features

- **Product Management**: Comprehensive product catalog with categories, variants, and inventory tracking
- **User Authentication**: Registration, login, password reset, and profile management
- **Shopping Cart**: Add to cart, quantity updates, and persistent cart sessions
- **Checkout Process**: Secure checkout with multiple payment options
- **Order Management**: Order tracking, history, and status updates
- **Admin Dashboard**: Complete admin interface for managing products, orders, and users
- **Search & Filtering**: Advanced product search and category filtering
- **Responsive Design**: Mobile-friendly interface built with Bootstrap
- **Email Notifications**: Automated emails for order confirmations and updates
- **Reviews & Ratings**: Customer product reviews and rating system

## 🛠️ Tech Stack

- **Backend**: Django 4.2+, Python 3.9+
- **Database**: PostgreSQL (production), SQLite (development)
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Payment Processing**: Stripe API
- **Image Storage**: Cloudinary or AWS S3
- **Email Service**: SendGrid or Django SMTP
- **Deployment**: Docker, Gunicorn, Nginx

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.9 or higher
- pip (Python package manager)
- PostgreSQL (for production)
- Git
- Node.js (for frontend dependencies)

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/seven-sundays-ecommerce.git
cd seven-sundays-ecommerce
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://username:password@localhost/seven_sundays_db
# For development, you can use SQLite:
# DATABASE_URL=sqlite:///db.sqlite3

# Email Settings
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True

# Payment Gateway
STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_publishable_key
STRIPE_SECRET_KEY=sk_test_your_stripe_secret_key

# Media Storage (Optional - for production)
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name

# Security
SECURE_SSL_REDIRECT=False  # Set to True in production
SESSION_COOKIE_SECURE=False  # Set to True in production
CSRF_COOKIE_SECURE=False  # Set to True in production
```

### 5. Database Setup

```bash
# Create and run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load sample data (optional)
python manage.py loaddata fixtures/sample_data.json
```

### 6. Collect Static Files

```bash
python manage.py collectstatic
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

## 📁 Project Structure

```
seven-sundays-ecommerce/
├── apps/
│   ├── accounts/          # User authentication and profiles
│   ├── products/          # Product catalog and management
│   ├── cart/             # Shopping cart functionality
│   ├── orders/           # Order processing and management
│   ├── reviews/          # Product reviews and ratings
│   └── core/             # Core utilities and base classes
├── static/
│   ├── css/              # Custom stylesheets
│   ├── js/               # JavaScript files
│   └── images/           # Static images
├── templates/
│   ├── base.html         # Base template
│   ├── accounts/         # Authentication templates
│   ├── products/         # Product templates
│   ├── cart/             # Cart templates
│   └── orders/           # Order templates
├── media/                # User uploaded files
├── config/
│   ├── settings/         # Settings modules
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── requirements.txt      # Python dependencies
├── manage.py            # Django management script
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose configuration
└── README.md           # This file
```

## 🔧 Configuration

### Payment Gateway Setup

1. Create a Stripe account at [stripe.com](https://stripe.com)
2. Get your API keys from the Stripe dashboard
3. Add the keys to your `.env` file
4. Configure webhook endpoints for order status updates

### Email Configuration

Configure your email settings in the `.env` file. For Gmail:

1. Enable 2-factor authentication
2. Generate an app-specific password
3. Use the app password in the `EMAIL_HOST_PASSWORD` setting

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.products

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

## 📦 Deployment

### Using Docker

1. Build the Docker image:
```bash
docker build -t seven-sundays-ecommerce .
```

2. Run with Docker Compose:
```bash
docker-compose up -d
```

### Manual Deployment

1. Set up your production server (Ubuntu/CentOS)
2. Install Python, PostgreSQL, Nginx
3. Configure environment variables for production
4. Set up SSL certificates
5. Configure Gunicorn and Nginx
6. Set up automated backups

## 🔐 Security Considerations

- Always use HTTPS in production
- Keep Django and dependencies updated
- Use strong, unique SECRET_KEY
- Configure proper CORS settings
- Implement rate limiting for API endpoints
- Regular security audits and penetration testing
- Set up monitoring and logging

## 📊 Admin Interface

Access the Django admin at `/admin/` with superuser credentials to:

- Manage products and categories
- View and process orders
- Manage user accounts
- Monitor site analytics
- Configure site settings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Write comprehensive docstrings
- Add comments for complex logic
- Maintain test coverage above 80%

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support & Contact

- **Documentation**: [Link to detailed docs]
- **Issues**: [GitHub Issues](https://github.com/yourusername/seven-sundays-ecommerce/issues)
- **Email**: support@sevensundays.com
- **Discord**: [Community Discord Server]

## 🙏 Acknowledgments

- Django community for the amazing framework
- Bootstrap team for the responsive CSS framework
- Stripe for secure payment processing
- All contributors and testers

## 📈 Roadmap

- [ ] Mobile app development (React Native)
- [ ] Multi-vendor marketplace support
- [ ] Advanced analytics dashboard
- [ ] AI-powered product recommendations
- [ ] Multi-language support
- [ ] Subscription-based products
- [ ] Social media integration
- [ ] Advanced inventory management

---

**Happy Shopping with Seven Sundays! 🛍️**