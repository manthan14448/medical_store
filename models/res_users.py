from odoo import  models


class ResUsers(models.Model):
    _inherit = "res.users"

    # send Invitation email to user 
    def action_send_invitation_email(self):
        self.ensure_one()
        portal_wizard = self.env['portal.wizard'].with_context(active_ids=[self.partner_id.id]).create({})
        portal = self.env['portal.wizard.user'].create(
            {'wizard_id': portal_wizard.id, 'partner_id': self.partner_id.id})
        portal.with_context(active_test=True)._send_email()
        portal.sudo().unlink()