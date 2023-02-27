{
    'name': 'Mediacal Store',
    'version': '1.0.0',
    'category': 'Advance Medical Management App',
    'author': 'manthan',
    'summary': 'Medical Store Management App with advance Search',
    'description': """""",
    'depends': ['mail', 'website_sale','account', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/product_view.xml',
        'views/patient.xml',
        'views/shop_views.xml',
        'data/body_parts_data.xml',
        'data/products_data.xml',
        'data/advance_search_template.xml',
    ],
    'demo': [],
    'sequence': -200,
    'application': True,
    'installable': True,
    'auto_install': False,
}
