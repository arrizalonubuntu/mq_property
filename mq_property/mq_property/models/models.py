# -*- coding: utf-8 -*-

from odoo import models, fields, api

class nup_data(models.Model):
    _name = 'nup.data'

    name = fields.Char(string="NUP", default="/", readonly=True)
    customer_id = fields.Many2one('res.partner', string="Pembeli")
    payment_date = fields.Date(string="Tanggal Pembayaran")
    property_id = fields.Many2one('product.template',string="Property")
    booking_fee = fields.Integer(string="Nominal Tanda Jadi", required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done'),
    ], string='Status', readonly=True, copy=False, default='draft', track_visibility='onchange')