# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tradeIguKwitansi(models.Model):
    _name="trade.kwitansi"
    _description = "Kwitansi Module"
    name = fields.Char("Nomor Kwitansi")
    docdate = fields.Date("Document Date")
    partner_id = fields.Char("Partner ID")
    
# class addons/igu_kwitansi/(models.Model):
#     _name = 'addons/igu_kwitansi/.addons/igu_kwitansi/'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100