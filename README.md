# Money Heist
The Money Heist is a spending tracking application. The project is being used to track your incomes spending and current balance. 

## User can<hr>
- add spending;
- select category of spending;
- select and change date;
- delete spending;
- filter by date;
- to search by spendings;
- filter by category or sending date;
- to export all spendings into .csv file

## Packages
+ `django`
+ `environs`
+ `psycopg2-binary`
+ `django-cors-headers `
+ `djangorestframework-simplejwt`
+ `djangorestframework-camel-case`
+ `drf-yasg`
+ `celery`
+ `redis`

## Development
+ Python 3.9
+ Docker
+ Postgres 12.3
+ Postman
+ JWT
+ MailJet API


## .env file

SECRET_KEY= your secret key

POSTGRES_USER= your postgres username

POSTGRES_PASSWORD= your postgres password

POSTGRES_DB= your database name

DB_HOST= your host

DB_PORT=. your port e.g 5433

BROKER_URL= your redis url e.g. "redis://localhost:6379/0"


MAILJET_PUBLIC_KEY= your API key from MailJet

MAILJET_SECRET_KEY= your secret key from MailJet

MAILJET_USER= your email address from MailJet

USER_ACTIVATION_URL= http://127.0.0.1:8000/v1/auth/activate/
