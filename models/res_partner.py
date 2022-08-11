from odoo import models, fields


class PartnerFilter(models.Model):

    _inherit = 'res.partner'

    products_list_id = fields.Many2many(
        comodel_name='product.template',
        string='Products List',
        help='List of products this partner can see.'
    )

