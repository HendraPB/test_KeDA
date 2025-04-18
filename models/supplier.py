from odoo import models, fields

class supplier(models.Model):
    _inherit = 'res.partner'

    material_ids = fields.One2many(
        comodel_name="keda.material",
        string="Materials",
        inverse_name="supplier_id",
    )