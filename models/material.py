from odoo import models, fields, api
from odoo.exceptions import ValidationError

TYPES = [
    ('fabric', 'Fabric'),
    ('jeans', 'Jeans'),
    ('cotton', 'Cotton')
]

class material(models.Model):
    _name = "keda.material"

    code = fields.Char(
        string="Code",
        required=True
    )

    name = fields.Char(
        string="Name",
        required=True
    )

    type = fields.Selection(
        string="Type",
        selection=TYPES,
        required=True
    )

    buy_price = fields.Float(
        string="Buy Price",
        required=True
    )

    supplier_id = fields.Many2one(
        comodel_name="res.partner",
        string="Supplier",
        required=True
    )

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError('Buy price cannot be less than 100')

    @api.model
    def create(self, vals):
        if vals.get('buy_price', 0) < 100:
            raise ValidationError("Buy price cannot be less than 100")
        return super(material, self).create(vals)

    def write(self, vals):
        if 'buy_price' in vals and vals['buy_price'] < 100:
            raise ValidationError("Buy price cannot be less than 100")
        return super(material, self).write(vals)