# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers import main
from odoo.addons.website_sale.controllers.main import WebsiteSale


class filter_router_medical(http.Controller):
    @http.route('/shop/bodypart', website=True, auth='public')
    def advance_search(self, **kw):
        return request.render("medical_store.shop_templet")

    @http.route(['/shop/bodypart/<int:bodypart>', '/bodypart/<int:bodypart>'], website=True, auth='public')
    def advance_search_redirect(self, bodypart=None, **kw):
        category = request.env['product.public.category'].browse(bodypart)
        url = f'/shop/category/{category.name}-{bodypart}'
        return request.redirect(url)


class PaymentDemoController(http.Controller):
    @http.route('/payment/cod/simulate_payment', type='json', auth='public')
    def cod_simulate_payment(self, **data):
        value = data['reference']
        if value:
            rec = request.env['payment.transaction'].search(
                [('reference', '=', value)])
            rec.sudo().write({'state': 'delivery'})
            rec.sudo().sale_order_ids.write({'client_order_ref': value})
            rec.sudo().sale_order_ids.action_confirm()

    @http.route('/delivery/status', type='http', auth="public", website=True, sitemap=False)
    def shop_delivery_confirmation(self, **post):
        return request.render('medical_store.delivery_status')


class WebsiteSale(WebsiteSale):

    def _prepare_product_values(self, product, category, search, **kwargs):
        product_val = super()._prepare_product_values(product, category, search, **kwargs)
        if request.uid != 4:
            user = request.env['res.users'].sudo().browse(request.uid)
            if user.country_id.name == "India":
                    product_cat_id = product_val['main_object'].public_categ_ids.ids
                    read_doctors = request.env['res.partner'].sudo().search_count([
                        ('expertIn', 'in', product_cat_id), ('function', '=', 'Doctor'), ('premium', '=', 'True')])
                    if read_doctors >= 4 :
                        doctors = request.env['res.partner'].sudo().search_read([
                            ('expertIn', 'in', product_cat_id), ('function', '=', 'Doctor'), ('premium',  '=', 'True')],
                                ['id', 'name', 'Rank', 'mobile', 'email', 'contact_address', 'image_1920','images_ids', 'website'],limit=4)
                    else:
                        doctors = request.env['res.partner'].sudo().search_read([
                            ('expertIn', 'in', product_cat_id), ('function', '=', 'Doctor')],
                            ['id', 'name', 'Rank', 'mobile', 'email', 'contact_address', 'image_1920', 'images_ids', 'website'], order='premium', limit=4)
                    for doctor in doctors:
                        if doctor.get('images_ids'):
                            for doctor_image_index in range(len(doctor.get('images_ids'))):
                                doctor_image_id = doctor['images_ids'][doctor_image_index]
                                doctor_image_obj = request.env['doctor.image'].sudo().browse(doctor_image_id)
                                doctor['images_ids'][doctor_image_index] = doctor_image_obj.images
                    product_val['doctors'] = doctors
        return product_val
