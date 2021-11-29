from odoo import models, fields


class Author(models.Model):
    _name = 'author'
    _description = 'Author'

    author_name = fields.Char(required=True)
    address = fields.Text()


class BookDepartment(models.Model):
    _name = 'book.department'
    _description = 'Book Department'

    department_name = fields.Char(required=True)


class BookCategory(models.Model):
    _name = 'book.category'
    _description = 'Book Category'

    Category_name = fields.Char(required=True)


class BookPublisher(models.Model):
    _name = 'book.publisher'
    _description = 'Book Publisher'

    publisher_name = fields.Char(required=True)


class Rack(models.Model):
    _name = 'rack'
    _description = 'Rack'

    name = fields.Char(required=True)


# sheld_ids = fields.One2many('rack', 'rack_id')


class Shelf(models.Model):
    _name = 'shelf'
    _description = 'Shelf'

    name = fields.Char(required=True)
    rack_id = fields.Many2one('rack')


class bookProperty(models.Model):
    _name = 'book.property'
    _description = 'Books'
    _sql_constraints = [('isbn_unique', 'unique(isbn)', 'Duplicate isbn not allowed')]

    name = fields.Char()
    price = fields.Float()
    author = fields.Many2many('author_name')
    author_ids = fields.Many2many('author')
    isbn = fields.Integer()
    category_id = fields.Many2one('book.category')
    department_id = fields.Many2one('book.department')
    barcode = fields.Char()
    publisher_id = fields.Many2one('book.publisher')
    edition = fields.Char()
    date = fields.Date()
    shelf_id = fields.Many2one('shelf')
