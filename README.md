# cineos SaaS

***_Coming soon_***

cineos is a comprehensive SaaS application designed specifically for cinematographers. Built on the solid foundation of the codingforentrepreneurs/SaaS-Foundations repository, cineos leverages cutting-edge technologies to streamline the film production process. Our stack includes Django for robust backend development, Tailwind CSS for sleek and responsive design, and htmx for dynamic content loading. We utilize Neon Postgres for efficient data management and Redis for high-performance caching.

## Features

- Script Breakdown: Easily analyze and break down scripts into manageable chunks.
- Shot List Creation: Intuitive tools for creating and managing comprehensive shot lists.
- Resource Management: Efficiently manage equipment, locations, and crew schedules.
- Storyboard Integration: Create and visualize storyboards directly within the application.
- Collaboration Tools: Streamline communication between team members.
- Scalable Architecture: Designed to handle projects of any size, from indie films to blockbusters.

## Technology Stack

- Backend: Django
- Frontend: Tailwind CSS, htmx
- Database: Neon Postgres
- Caching: Redis
- Hosting: [To be determined]

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Git
- Pip (Python package installer)
- A Neon account for Postgres database
- A Stripe account for payment processing

### Clone the Repository

```bash
mkdir -p ~/dev/cineos
cd ~/dev/cineos
git clone https://github.com/yourusername/cineos.git .
```

### Create and Activate Virtual Environment

*macOS/Linux*
```bash
python3 -m venv venv
source venv/bin/activate
```

*Windows*
```bash
python -m venv venv
.\venv\Scripts\activate
```

### Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Configure Environment Variables

1. Copy the sample environment file:
   ```bash
   cp .env.sample .env
   ```

2. Open `.env` and update the following values:
   - `DJANGO_DEBUG`: Set to 1 for development, 0 for production
   - `DJANGO_SECRET_KEY`: Generate a new secret key (instructions below)
   - `DATABASE_URL`: Your Neon Postgres connection string
   - `EMAIL_*`: Configure your email settings
   - `ADMIN_USER_EMAIL`: Set the admin email address
   - `STRIPE_SECRET_KEY`: Your Stripe secret key

### Generate Django Secret Key

Run one of the following commands and copy the output to `DJANGO_SECRET_KEY` in `.env`:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
or
```bash
openssl rand -base64 64
```
or
```bash
python -c 'import secrets; print(secrets.token_urlsafe(64))'
```

### Set Up Neon Postgres Database

1. Install Neon CLI:
   ```bash
   brew install neonctl  # For macOS, use appropriate method for your OS
   ```

2. Authenticate with Neon:
   ```bash
   neonctl auth
   ```

3. Create a new Neon project (optional):
   ```bash
   neonctl projects create --name cineos
   ```

4. Get your project ID:
   ```bash
   PROJECT_ID=$(neonctl projects list | grep "cineos" | awk -F '│' '{print $2}' | xargs)
   ```

5. Get the database connection string:
   ```bash
   neonctl connection-string --project-id "$PROJECT_ID"
   ```

6. Set the `DATABASE_URL` in `.env` with the obtained connection string.

### Run Migrations

```bash
cd src
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Install Vendor Static Files

```bash
python manage.py vendor_pull
```

### Set Up Stripe

1. Sign up for a Stripe account at [stripe.com](https://www.stripe.com)
2. Obtain your Stripe Secret API Key from the Dashboard > Developers > API keys
3. Update `STRIPE_SECRET_KEY` in `.env` with your key

### Run the Development Server

```bash
python manage.py runserver
```

Your cineos instance should now be running at `http://127.0.0.1:8000/`.

## Deployment

Detailed deployment instructions will be provided soon. We are currently evaluating the best hosting solutions for cineos.

## Contributing

We welcome contributions to cineos! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for details on our code of conduct and the process for submitting pull requests.

## Support

If you encounter any issues or have questions, please file an issue on our GitHub repository or contact our support team at support@cineos.io.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgments

- [Coding for Entrepreneurs](https://www.codingforentrepreneurs.com/) for the SaaS-Foundations repository
- All the open-source projects that make cineos possible

Stay tuned for more updates as we continue to develop and enhance cineos! 🎥🚀
