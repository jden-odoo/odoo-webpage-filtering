from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale, TableCompute


class WebsiteSaleFilter(WebsiteSale):

    def sitemap_shop(env, rule, qs):
        return super(WebsiteSale, self).sitemap_shop(env, rule, qs)


    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True, sitemap=sitemap_shop)
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        res = super(WebsiteSaleFilter, self).shop(page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post)

        current_uid = request.env.user.id
        user = request.env['res.users'].browse(current_uid)
        partner_record = request.env['res.partner'].search([('name', '=', user.name)])

        if partner_record:
            context = res.qcontext
            products = context['products'].filtered(lambda p: partner_record.id in p.partners_list.ids)
            ppg = context['ppg']
            ppr = context['ppr']
            bins = TableCompute().process(products, ppg, ppr)
            context['products'] = products
            context['bins'] = bins
            return request.render("website_sale.products", context)
        else:
            return res

    
    #TODO: override shop method is WebsiteSale, modify records