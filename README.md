# SaaS Foundations

Build the foundations for a Software as a Service business by leveraging Django, Tailwind, htmx, Neon Postgres, Redis, and more.

The goal of this project is to learn how to create a reusable foundation for building SaaS products. When release, this course will span multiple topics and give you a solid foundation into build your business.


## References

- Deploy Django on [Railway](https://kirr.co/qysgeu) with [this Dockerfile and guide](https://www.codingforentrepreneurs.com/blog/deploy-django-on-railway-with-this-dockerfile/)
- Create a One-Off Secret Key for Django [blog post](https://www.codingforentrepreneurs.com/blog/create-a-one-off-django-secret-key/)


Thank you to [Neon](https://kirr.co/eu0b31) for helping bring this course to life!


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

### Install Requirements
```bash
# with venv activated
pip install pip --upgrade && pip install -r requirements.txt
```

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


### Create [Neon](https://kirr.co/eu0b31) Postgres Database


#### Install Neon CLI
Using the [Neon cli](https://neon.tech/docs/reference/cli-install) via [homebrew](https://brew.sh/):

```bash
brew install neonctl
```

#### Login to Neon CLI

```bash
neonctl auth
```
This will open a browser window to login.

####  Create a new Neon project (optional)
```bash
neonctl projects create --name saas
```

#### Get the Project ID

Once created, get the project id: 

```bash
neonctl projects list
```
Projects

```bash
┌──────────────────────────┬────────────────────────────┬───────────────┬──────────────────────┐
│ Id                       │ Name                       │ Region Id     │ Created At           │
├──────────────────────────┼────────────────────────────┼───────────────┼──────────────────────┤
│ steep-base-11409687      │ saas                       │ aws-us-east-2 │ 2024-06-02T04:03:07Z │
└──────────────────────────┴────────────────────────────┴───────────────┴──────────────────────┘
```

```bash
PROJECT_ID=steep-base-11409687
```
Replace `steep-base-11409687` with your project id.

Or using the shortcut:

```bash
PROJECT_ID=$(neonctl projects list | grep "saas" | awk -F '│' '{print $2}' | xargs)
```

#### Get the Database Connection String

```bash
neonctl connection-string --project-id "$PROJECT_ID"
```
Set this value to `DATABASE_URL` in `.env`. 


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

Much more coming soon!