# -*- coding: utf-8 -*-
from odoo import http

# class Addons/iguKwitansi/(http.Controller):
#     @http.route('/addons/igu_kwitansi//addons/igu_kwitansi//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/igu_kwitansi//addons/igu_kwitansi//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/igu_kwitansi/.listing', {
#             'root': '/addons/igu_kwitansi//addons/igu_kwitansi/',
#             'objects': http.request.env['addons/igu_kwitansi/.addons/igu_kwitansi/'].search([]),
#         })

#     @http.route('/addons/igu_kwitansi//addons/igu_kwitansi//objects/<model("addons/igu_kwitansi/.addons/igu_kwitansi/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/igu_kwitansi/.object', {
#             'object': obj
#         })