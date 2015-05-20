# -*- coding: utf-8 -*-
from openerp import http

# class Rentacar(http.Controller):
#     @http.route('/rentacar/rentacar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rentacar/rentacar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rentacar.listing', {
#             'root': '/rentacar/rentacar',
#             'objects': http.request.env['rentacar.rentacar'].search([]),
#         })

#     @http.route('/rentacar/rentacar/objects/<model("rentacar.rentacar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rentacar.object', {
#             'object': obj
#         })