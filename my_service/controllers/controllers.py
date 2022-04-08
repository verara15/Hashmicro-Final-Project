# -*- coding: utf-8 -*-
# from odoo import http


# class MyService(http.Controller):
#     @http.route('/my_service/my_service/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_service/my_service/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_service.listing', {
#             'root': '/my_service/my_service',
#             'objects': http.request.env['my_service.my_service'].search([]),
#         })

#     @http.route('/my_service/my_service/objects/<model("my_service.my_service"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_service.object', {
#             'object': obj
#         })
