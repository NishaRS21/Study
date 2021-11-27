from odoo import fields, models


class Test(models.Model):
    _name = 'test'

    name = fields.Char(required=True)
