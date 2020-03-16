# -*- coding: utf-8 -*-
from odoo import http

# class MqProperty(http.Controller):
#     @http.route('/mq_property/mq_property/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mq_property/mq_property/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mq_property.listing', {
#             'root': '/mq_property/mq_property',
#             'objects': http.request.env['mq_property.mq_property'].search([]),
#         })

#     @http.route('/mq_property/mq_property/objects/<model("mq_property.mq_property"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mq_property.object', {
#             'object': obj
#         })