{
    'name': 'Project Management',
    'version': '1.0',
    'category': 'Project',
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_views.xml',
        'views/task_views.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
}