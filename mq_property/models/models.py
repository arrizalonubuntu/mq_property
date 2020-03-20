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


class customer_data(models.Model):
    _name = 'customer.data'

    name = fields.Char(string="Name")
    alamat = fields.Char(string="Alamat")
    pekerjaan = fields.Char(string="Pekerjaan")
    no_hp = fields.Integer(string="No Handphone")
    npwp = fields.Integer(string="NPWP")
    ktp = fields.Binary(string="FotoCopy KTP", attachment=True)
    kk = fields.Binary(string="FotoCopy KK", attachment=True)
    rekening = fields.Binary(string="FotoCopy Rekening", attachment=True)
    surat_nikah = fields.Binary(string="FotoCopy Surat Nikah", attachment=True)
    surat_kerja = fields.Binary(string="FotoCopy Keterangan Kerja", attachment=True)
    rekening_koran = fields.Binary(string="FotoCopy Rekening Koran", attachment=True)
    bukti_penghasilan = fields.Binary(string="FotoCopy Bukti Penghasilan", attachment=True)
    