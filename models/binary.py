
import odoo
from odoo import http, _

class Binary(http.Controller):

    def content_image(self, xmlid=None, model='ir.attachment', id=None, field='raw',
                                filename_field='name', filename=None, mimetype=None, unique=False,
                                download=False, width=0, height=0, crop=False, access_token=None,
                                nocache=False):
                record = super().content_image(xmlid, model, id, field,filename_field, filename, mimetype, unique,download, width, height, crop, access_token,nocache)
                print("called here")
                return record
