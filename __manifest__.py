{
    'name': 'Mediacal Store',
    'version': '1.0.0',
    'category': 'Advance Medical Management App',
    'author': 'manthan',
    'summary': 'Medical Store Management App with advance Search',
    'description': """""",
    'depends': ['mail', 'base', 'account', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/product_view.xml',
        'views/patient.xml',
        'views/shop_views.xml',
        'data/data.xml',
       
    ],
    'demo': [],
    'sequence': -200,
    'application': True,
    'installable': True,
    'auto_install': False,
}
