{
    'name': "Sale package label",
    'version': '1.0',
    'category' : 'Website',
    'website' : 'http://www.zynthian.org',
    'summary': 'Package Label to paste in the package. Included FROM and TO address',
    'description': """
        Modification of:
        """,
    'author': 'mumaker',
    'depends': ['website'],
    'data': [
        'views/sale_package_label_report.xml',
        'views/sale_package_label_template.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
