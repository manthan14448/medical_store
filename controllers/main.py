from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers import main


class TempTest(http.Controller):
    @http.route('/shop/bodypart', website=True, auth='public')
    def temphome(self, **kw):
        # return "Hello, im done"
        tdata = request.env['product.public.body.part'].sudo().search([])
        values = {
            'tdata': tdata
        }
        print(tdata)
        return request.render("medical_store.shop_templet", values)

    @http.route('/shop/<int:filter>', website=True, auth='public')
    def temphome1(self, filter=None, **kw):
        print("filter ingthin sucessfull")
        print("Body Part "+str(filter))
        tdata = request.env['product.template'].sudo().search([])
        values = {
            'tdata': tdata
        }
        print(tdata)
        return request.render("medical_store.shop_templet", values)

    @http.route('/shop/bodypart/<int:bodypart>', website=True, auth='public')
    def temphome1(self, bodypart=None, **kw):
        print("Filter sucessfull")
        print("Body Part "+str(bodypart))
        #    values = {
        #     'search': search,
        #     'category': category,
        #     'attrib_values': attrib_values,
        #     'attrib_set': attrib_set,
        #     'pager': pager,
        #     'pricelist': pricelist,
        #     'products': products,
        #     'bins': table_compute().process(products),
        #     'rows': main.PPR,
        #     'styles': styles,
        #     'categories': categs,
        #     'attributes': attributes,
        #     'compute_currency': compute_currency,
        #     'keep': keep,
        #     'style_in_product': lambda style, product: style.id in [s.id for s in product.website_style_ids],
        #     'attrib_encode': lambda attribs: werkzeug.url_encode([('attrib',i) for i in attribs]),
        #     'shop_home_page': shop_home_page,
        #     'bodypart': bodypart,
        #     'view': view,
        # }
        return request.website.render("WebsiteSale.products")
