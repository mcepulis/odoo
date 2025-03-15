
# Odoo Project Management Module

This repository contains a custom Odoo module for managing projects and tasks. It is designed to work with Odoo 13.0.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- **Python 3.7.9** (recommended for Odoo 13.0)
- **PostgreSQL 12.22** (recommended for Odoo 13.0)

## Setup Instructions

Follow these steps to set up the project on your local machine:


Clone the official Odoo 13.0 repository into a directory of your choice:

```bash
git clone -b 13.0 https://github.com/odoo/odoo.git
cd odoo/addons
git clone https://github.com/mcepulis/odoo.git Project_Management

cd odoo (back to odoo root folder)
python -m venv venv
venv\Scripts\activate
```

Creade DB: odoo13 and create configuration file odoo.conf in odoo root folder with content:
```bash
[options]
; Database settings
db_host = localhost
db_port = 5432
db_user = your_postgres_user
db_password = your_postgres_password
db_name = odoo13
```

start odoo with ability upgrade my project code at once:
```bash
python odoo-bin -c odoo.conf -u project_management
```

Start my project auto-testing:
```bash
python odoo-bin -c odoo.conf --test-enable --stop-after-init -d odoo13 -i project_management
```

For all functionalities that involve sending emails, all email messages are routed to the Technical --> Messages section in Odoo. This ensures that email-related notifications and communications are centralized and easily accessible for review.
