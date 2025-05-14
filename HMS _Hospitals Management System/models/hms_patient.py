from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Patient(models.Model):
    _name = 'hms.patient'
    _rec_name= 'first_name'

    
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date()
    age = fields.Integer(compute="_compute_age", store=True)
    email = fields.Char(string="Email", required=True)
    blood_type = fields.Selection([
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-')
    ], string="Blood Type")
    pcr = fields.Boolean()
    cr_ratio = fields.Float()
    address = fields.Text()
    history = fields.Html()
    image = fields.Image()

    department_id = fields.Many2one(
        "hms.departments",
        string="Department",
        domain=[('is_open', '=', True)]
    )
    department_capacity = fields.Integer(related="department_id.capacity")
    
    state = fields.Selection([
        ("U", "Undetermined"),
        ("g", "Good"),
        ("f", "Fair"),
        ("s", "Serious"),
    ], default='undetermined')

    doctor_ids = fields.Many2many("hms.doctor", string="Doctors")
    log_history_ids = fields.One2many("hms.log.history","patient_log_history_id",string="Log History")

    _sql_constraints = [
        ('email_unique', 'UNIQUE(email)', 'Email must be unique!'),
    ]

    @api.constrains('email')
    def _check_email(self):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        for record in self:
            if record.email and not re.match(email_regex, record.email):
                raise ValidationError('Invalid email format: %s' % record.email)

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = fields.Date.today()
                record.age = today.year - record.birth_date.year - (
                    (today.month, today.day) < (record.birth_date.month, record.birth_date.day)
                )
            else:
                record.age = 0
                
        @api.constrains('state')
        def _log_state_change(self):
            for record in self:
                record.log_history_ids = [(0, 0, {'description': f"State changed to: {record.state}"})]
    @api.onchange('age')
    def _onchange_age(self):
        if self.age < 30:
            self.pcr = True
            return {
                'warning': {
                    'title': "PCR Checked Automatically",
                    'message': "The PCR field has been automatically checked because the patient's age is below 30."
                }
            }

    @api.constrains('pcr', 'cr_ratio')
    def _check_cr_ratio_required(self):
        for record in self:
            if record.pcr and not record.cr_ratio:
                raise ValidationError("CR Ratio must be filled when PCR is checked.")
