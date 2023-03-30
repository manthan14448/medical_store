{
    'name': 'Mediacal Store',
    'version': '1.0.0',
    'category': 'Advance Medical Management App',
    'author': 'manthan',
    'summary': 'Medical Store Management App with advance Search',
    'description': """""",
    'depends': ['website_sale', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_action.xml',
        'views/product_view.xml',
        'views/patient_catogory.xml',
        'views/res_users.xml',
        'views/delivery_view.xml',
        'views/menu.xml',
        'views/advance_search_template.xml',
        'views/shop_views.xml',
        'views/delivery_templates.xml',
        
        'data/medical_cod_jounral.xml',
        'data/payment_icon_data.xml',
        'data/payment_provider_data.xml',
        'data/product_public_category.xml',
        'data/products_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'medical_store/static/src/js/payment_form.js'
        ],
    },
    'demo': [],
    'sequence': -200,
    'application': True,
    'installable': True,
    'auto_install': False,
}
