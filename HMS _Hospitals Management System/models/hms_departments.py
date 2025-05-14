from odoo import models, fields

class Departments(models.Model):
    _name = 'hms.departments'

    name = fields.Char(required=True)
    capacity = fields.Integer()
    is_open = fields.Boolean()
    #patients_ids = fields.One2many('hms.patient', 'department_id')
