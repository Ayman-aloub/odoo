from odoo import models, fields
class Doctor(models.Model):
    _name="res.doctor"
    _inherits = "res.users"
