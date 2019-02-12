# -*- coding: utf-8 -*-
from odoo import http

# class Bote(http.Controller):
#     @http.route('/bote/bote/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bote/bote/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bote.listing', {
#             'root': '/bote/bote',
#             'objects': http.request.env['bote.bote'].search([]),
#         })

#     @http.route('/bote/bote/objects/<model("bote.bote"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bote.object', {
#             'object': obj
#         })