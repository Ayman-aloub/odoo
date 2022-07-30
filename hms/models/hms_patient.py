from odoo.exceptions import ValidationError
from odoo import models, fields, api
from odoo.exceptions import  UserError
from odoo.exceptions import ValidationError
import re
#eng.mohammedashraf96@gmail.com
class Pateint(models.Model):
    _name = 'hms.patient'
    _rec_name = 'first_name'
    first_name = fields.Char(string="First Name" ,required=True)
    second_name = fields.Char(string="Second Name",required=True)
    birth_date = fields.Date()
    email=fields.Char(default='')
    history = fields.Html()
    age = fields.Integer(compute='calculate_age')
    cr_ratio = fields.Float(string="CR Ratio")
    pcr = fields.Boolean()
    image = fields.Image()
    address = fields.Text()
    blood_typ = fields.Selection(
        [("a", "A"),
         ("b", "B"),
         ("o+", "O+"),
         ("a-", "A-")]
    )
    dep_id=fields.Many2one('hms.department')
    department_capicity=fields.Integer(related='dep_id.capicty', store=False)
    doctor_ids=fields.One2many('doctors.patient.line','patient_id')
    pateint_hsitory=fields.One2many('log.patient','patient_id')
    state = fields.Selection(
        [("undetermined", "Undetermined"),
         ("good", "Good"),
         ("fair", "Fair"),
         ("serious", "Serious")]
    )
    def action_undetermined(self):
        self.state = 'undetermined'
    def action_good(self):
        self.state = 'good'
    def action_fair(self):
        self.state = 'fair'
    def action_serious(self):
        self.state = 'serious'

    def unlink(self):
        for patient in self:
            if patient.state =='good':
                raise UserError('can\'t delete patient with good state')

        super(Pateint, self).unlink()


    def write(self,vals):
        print('oooooooooooooooooooooooo')
        for patient in self:
            if 'state' in vals:
                self.env['log.patient'].create({'descreption': f'{vals["state"]}', 'patient_id': f'{patient.id}'})
            return super(Pateint,self).write(vals)

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if 'email' in record:
                if record.email:
                    if not re.search("^[a-zA-Z_].+@.+\..+", record.email):
                        raise ValidationError(f"email must flow ___@___.___ {record.email}")

    @api.onchange('age')
    def change_pcr(self):
        if self.age !=0 :
            if self.age < 30:
                self.pcr = True

                return {
                    'warning': {
                        'title': 'Age Lower than 30 ',
                        'message': 'pcr is checked Age Lower than 30'
                    }
                }

    @api.depends('birth_date')
    def calculate_age(self):
        for patient in self:
            if patient.birth_date:
                today = fields.Date.today()
                delta = (today - patient.birth_date).days
                patient.age = delta // 365
            else:
                patient.age = 0


