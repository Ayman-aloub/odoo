from odoo import fields,models,api
from odoo.exceptions import ValidationError
class Crm_customer(models.Model):
    _inherit = 'res.partner'
    related_patient_id=fields.Many2one('hms.patient',ondelete='restrict')

    def unlink(self):
        for customer in self:
            if  customer.related_patient_id:
                raise ValidationError('can\'t delete , there are related patients')
        return super(Crm_customer, self).unlink()

    _sql_constraints = [
            ('taxId_required', 'REQUIRED(vat)', 'TAX ID is required')
    ]
    @api.constrains('email')
    def check_email(self):
        for customer in  self:
            if customer.email:
                cus=self.env['hms.patient'].search([('email','=',f'{customer.email}')])
                print(cus)
                if self.env['hms.patient'].search([('email','=',f'{customer.email}')],limit=1).id :
                    raise ValidationError(f"duplicated email")
