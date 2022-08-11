from odoo import models, fields, api


class ProductPartnerList(models.Model):
    _inherit = 'product.template'

    partners_list = fields.Many2many(
        comodel_name='res.partner', 
        string='Partners List', 
        help='List of partners this product can be seen by')

