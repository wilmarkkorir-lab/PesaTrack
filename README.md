# PesaTrack Complete Django Backend

A complete database-schema and core REST API foundation for PesaTrack: personal finance plus small-business finance.

## Included Django apps
- `accounts`: registration, JWT login, profile and KES/USD setting
- `finance`: categories, transactions, budgets, goals, recurring records, bills, debts, attachments
- `business`: businesses, team roles, customers, suppliers, products, invoices, payments, expenses and audit log
- `billing`: plans, subscriptions, billing payments
- `notifications`: notification records/preferences
- `support`: support tickets
- `reports`: reporting endpoints

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
# copy .env.example .env then configure MySQL
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Use MySQL credentials in `.env` or `config/settings.py`. Do not commit `.env`.

## Important
This source project contains the full database model structure and core API endpoints, but real payment/M-Pesa/SMS/email-provider calls must be configured with your own approved provider credentials. Before production, add automated tests, run `python manage.py check --deploy`, set `DEBUG=False`, use HTTPS, restrict CORS and make backups.
