from odoo import models, fields, api, _
from odoo.exceptions import UserError
import datetime


class Appointment(models.Model):
    _name = 'patient.appointment'
    name = fields.Char(string="Reference", readonly=True)
    clinic_id = fields.Many2one('res.clinic', string='clinic')
    patient_id = fields.Many2one('res.patient', string='patient')
    doctor_id = fields.Many2one('res.users', string='doctors')
    date = fields.Datetime(default=datetime.date.today())
    notes = fields.Text()
    state = fields.Selection([
        ('new', 'new'),
        ('confirmed', 'confirmed'),
        ('cancelled', 'cancelled'),
        ('draft', 'draft'),
    ])

    @api.onchange('clinic_id')
    def clinic_id_onchange(self):
        for record in self:
            return {'domain': {'doctor_id': [('id', 'in', record.clinic_id.doctors_ids.ids)]}}

    def action_new(self):
        self.state = 'new'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_cancelled(self):
        self.state = 'cancelled'

    def action_draft(self):
        self.state = 'draft'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('patient.appointment') or _('New')
        return super(Appointment, self).create(vals)

    def unlink(self):
        for record in self:
            if 'state' in record:
                if record.state == 'confirmed':
                    raise UserError('sorry , you can\'t delete confirmed appointment ')
        return super(Appointment, self).unlink()
