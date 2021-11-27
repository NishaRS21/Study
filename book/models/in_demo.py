from odoo import models, fields, api


class MyTest(models.Model):
    _name = 'my.test'
    _description = 'My Test'

    name = fields.Char()
    address = fields.Text()
    email = fields.Char()
    pincode = fields.Integer()

# after checking above add class


# class inheritance
'''class M1(models.Model):
    _inherit = 'my.test'
    
    country = fields.Char()
    state = fields.Char()
    city = fields.Char()'''

# prototype inheritance
'''class M2(models.Model):
    _name = 'm2'
    _inherit = 'M1'
    
    pancard = fields.Char()
    Aadhaar = fields.Char()'''
