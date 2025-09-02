# SaaS Foundations

Build the foundations for a Software as a Service business by leveraging Django, Tailwind, htmx, Neon Postgres, Redis, and more.

The goal of this project is to learn how to create a reusable foundation for building SaaS products. When release, this course will span multiple topics and give you a solid foundation into build your business.


## References

- Deploy Django on [Railway](https://kirr.co/qysgeu) with [this Dockerfile and guide](https://www.codingforentrepreneurs.com/blog/deploy-django-on-railway-with-this-dockerfile/)
- Create a One-Off Secret Key for Django [blog post](https://www.codingforentrepreneurs.com/blog/create-a-one-off-django-secret-key/)
- This repo started as a course [SaaS Foundations](https://www.codingforentrepreneurs.com/courses/saas-foundations).
- Need a more advanced SaaS template? Check out [CFE Run](https://run.codingforentrepreneurs.com/).


## Getting Started

### Clone
```bash
mkdir -p ~/dev/saas
cd ~/dev/saas
git clone https://github.com/codingforentrepreneurs/SaaS-Foundations .
```

### Create Virtual Environment

*macOS/Linux*
```bash
python3 --version # should be 3.11 or higher
python3 -m venv venv
source venv/bin/activate
```

*Windows*
```bash
c:\Python312\python.exe -m venv venv
.\venv\Scripts\activate
```

### Install Requirements with Rav
[Rav](https://github.com/jmitchel3/rav) is a simple way to run commands and download static files (css, images, js, etc) from external sources.

```bash
# with venv activated
pip install pip rav --upgrade
rav run install
```
> Use `python -m rav run install` if for some reason `rav` is not in your path.

### Sample dotenv to dotnev

```bash
cp .env.sample .env
cat .env
```
Values include:
- `DJANGO_DEBUG=1`
- `DJANGO_SECRET_KEY=""`
- `DATABASE_URL=""`
- `EMAIL_HOST="smtp.gmail.com"`
- `EMAIL_PORT="587"`
- `EMAIL_USE_TLS=True`
- `EMAIL_USE_SSL=False`
- `EMAIL_HOST_USER=""`
- `EMAIL_HOST_PASSWORD=""`
- `ADMIN_USER_EMAIL=""`
- `STRIPE_SECRET_KEY=""`


### Create the _DJANGO_SECRET_KEY_

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

Once you have this value, add update `DJANGO_SECRET_KEY` in `.env`.


### Run Migrations

```bash
source venv/bin/activate 
# or .\venv\Scripts\activate if windows
cd src
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Pull Vendor Static Files

```bash
python manage.py vendor_pull
```


### Create a Stripe Account

1. Sign up on [Stripe.com](https://www.stripe.com) for an account
2. Get or create a Stripe Secret API Key (Dashboard > Developers > API keys > _Secret key_ )
3. Update _dotenv_ (`.env`) with the value `STRIPE_SECRET_KEY` with your key.


### Run the Server

```bash
python manage.py runserver
```

Ready to roll! 🚀


### Useful Rav Commands

Review the [rav.yaml](./rav.yaml) (or [rav](https://github.com/jmitchel3/rav) documentation) for available command shortcuts, here are some useful ones:

- `rav run install` - Install requirements based on `scripts.install`
- `rav run install_dev` - Install requirements for development
- `rav run makemigrations` - Make migrations
- `rav run migrate` - Run migrations
- `rav run dev` - Run the development server
- `rav run test` - Run the tests
- `rav run vendors_pull` - Download vendor static files
- `rav run collectstatic` - Collect static files
- `rav download staticfiles_prod` - Download vendor static files for production
- `rav download staticfiles_dev` - Download vendor static files for development


### Upcoming Changes
- [] Remove Django Allauth-UI and Slippers. While these tools can be great, they have been causing more issues than they have been worth.
- [] Docker Compose support for Postgres, Redis, and more.


### Changelog

- 2025-09-02: 
  - Upgraded to Django 5.2
  - Added Slippers for better AllAuth UI Support
  - Implemented Rav to manage requirements and static files
  - Updated Dockerfile to use Rav
  - Updated README to include Rav
  - Dropped only Neon in favor of any Postgres database (aim to make it more generic)