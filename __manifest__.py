{
    'name': 'Test KeDA',
    'version': '1.0.0',
    'description': 'Test Odoo with topic material CRUD',
    'author': 'Hendra Pratama Budianto',
    'depends': ['base'],
    'data': [
        'views/menu.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/material.xml',
        'views/supplier.xml',
    ],
    'installable': True,
    'application': True,
}