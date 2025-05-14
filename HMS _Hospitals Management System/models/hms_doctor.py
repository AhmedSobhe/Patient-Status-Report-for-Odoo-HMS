from odoo import models, fields

class Departments(models.Model):
    _name = 'hms.doctor'
    _rec_name= "first_name"

    first_name = fields.Char()
    last_name = fields.Char()
    image = fields.Image()
    patient_ids = fields.Many2many("hms.patient",string="Patients")