from odoo import models, fields
class Pateint(models.Model):
    _name = 'res.patient'
    _rec_name = 'name'
    _inherits = {'res.partner': 'partner_id'}
    _inherit = ['mail.thread', 'mail.activity.mixin']
    partner_id = fields.Many2one('res.partner', required=True, ondelete='restrict', auto_join=True, index=True,
                                 string='Related Partner', help='Partner-related data of the user')
    # name = fields.Char(related="partner_id.name")
    # mobile = fields.Char(related="partner_id.mobile")
    # email = fields.Char(related="partner_id.email")
    age = fields.Integer(tracking=True,)
    blood_type = fields.Selection(
        [("A-", "A-"),
         ("A+","A+"),
         ("B+", "B+"),
         ("B-", "B-"),
         ("O+", "O+"),
         ("O-", "O-"),
         ("AB+", "AB+"),
         ("AB-", "AB-")]
    )
    gender = fields.Selection(
        [("male", "Male"),
         ("female", "Female")]
    )
    height = fields.Float()
    width = fields.Float()
    # _sql_constraints = [('unique_partener','UNIQUE(partner)','partner already exist')]

