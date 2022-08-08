from dataclasses import fields
import datetime
from odoo import fields, models,_
class CreateAppointmentWiz(models.TransientModel):
    _name = "clinic.appointment.wizard"
    _description = "Create Appointment Wizard"
    name = fields.Char(string="Reference", readonly=True)
    clinic_id = fields.Many2one('res.clinic', string='clinic')
    patient_id = fields.Many2one('res.patient', string='patient')
    doctor_id = fields.Many2one('res.users', string='doctors')
    date = fields.Datetime(default=datetime.date.today())
    notes = fields.Text()

    def action_create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'doctor_id': self.doctor_id.id,
            'date': self.date,
            'clinic_id':self.clinic_id.id,
            'notes': self.notes,
        }
        appointment_rec = self.env['patient.appointment'].create(vals)
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'patient.appointment',
            'res_id': appointment_rec.id,
        }

    def action_view_appointment(self):
        # action = self.env.ref('clinic_management.clinic_management_appointment_action').read()[0]
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        # return action

    #     action = self.env['ir.actions.actions']._for_xml_id("clinic_management.clinic_management_appointment_action")
    #     action['domain'] = [('patient_id', '=', self.patient_id.id)]
    #     return action
    #
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'patient.appointment',
            'view_type': 'form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }
        return action
