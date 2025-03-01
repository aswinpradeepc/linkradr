# LinkRadr - URL Shortener

A modern URL shortening service built with Django that provides secure URL management with user authentication and tracking capabilities.

## Key Features

- **URL Shortening**: Generate concise URLs for long web addresses
- **User Authentication**: Email-based signup/login with OTP verification
- **Custom Short URLs**: Create personalized memorable short links
- **Analytics**: Track clicks and usage statistics
- **Responsive Design**: Mobile-first interface that works on all devices
- **One-Click Copy**: Easy clipboard copying of shortened URLs
- **Profile Dashboard**: Manage all your shortened URLs in one place

## Technology Stack

- **Backend**: Django 5.1 with custom user authentication
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Server**: Nginx + Gunicorn
- **Containerization**: Docker + Docker Compose
- **CI/CD**: GitHub Actions for automated deployment

## Installation

1. Clone the repository and enter the directory:
    ```bash
    git clone https://github.com/yourusername/linkradr.git
    cd linkradr
    ```

2. Create a `.env` file with required variables:
    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    EMAIL_HOST=smtp.your-email-provider.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=your-email@example.com
    EMAIL_HOST_PASSWORD=your-email-password
    ```

3. Build and run with Docker Compose:
    ```bash
    docker-compose up --build
    ```

4. Access the application at [http://localhost:8000](http://localhost:8000)

## Local Development Setup

1. Create and activate virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run migrations:
    ```bash
    python manage.py migrate
    ```

4. Start development server:
    ```bash
    python manage.py runserver
    ```

## Project Structure

- `authapp` - Custom authentication app
- `shortener` - Core URL shortening functionality
- `templates` - HTML templates
- `static/` - CSS, JS and images
- `nginx` - Nginx configuration
- `scripts` - Deployment scripts

## Deployment

The project includes GitHub Actions workflow for AWS EC2 deployment:

1. Add required secrets to GitHub repository:
    - `EC2_HOST`: EC2 instance hostname/IP
    - `EC2_SSH_KEY`: SSH private key

2. Push to main branch to trigger deployment

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Acknowledgments

- Made at CUSAT (Cochin University of Science and Technology)
- Special thanks to all contributors
