from odoo import models,fields,api
class Clinic(models.Model):
    _name = 'res.clinic'
    name = fields.Char(string="clinic name")
    clinic_no = fields.Integer(string="clinic number")
    doctors_ids=fields.Many2many('res.users',)



