1. Versions:
odoo ver. 13
Python ver. 3.7.9 (compatible with the latest odoo version)
PostgreSQL ver. 12.22 (compatible with the latest odoo version)

2. Implementation
 Clone the whole odoo app from here --> https://github.com/odoo/odoo/tree/13.0
 Clone my https://github.com/mcepulis/odoo.git content to --> odoo/addons/Project_management

.
|-- __init__.py
|-- __manifest__.py
|-- __pycache__
|   `-- __init__.cpython-37.pyc
|-- data
|   |-- demo_data.xml
|   `-- email_templates.xml
|-- models
|   |-- __init__.py
|   |-- project_management.py
|   `-- task_management.py
|-- reports
|   |-- task_report.py
|   `-- task_report_template.xml
|-- security
|   |-- ir.model.access.csv
|   `-- record_rules.xml
|-- tests
|   |-- __init__.py
|   `-- test_task_management.py
|-- views
|   |-- project_views.xml
|   |-- task_views.xml
|   `-- task_wizard_views.xml
`-- wizards
    |-- __init__.py
    `-- task_filter_wizard.py
