from odoo import api, fields, models

# It will automatically create a school_student (name) table with this fields
class SchoolStudent(models.Model):
  _name = 'school.student'
  _description = 'School Student'

  name = fields.Char(string = 'Name')
  age = fields.Integer(string = 'Age')
  gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string = 'Gender')