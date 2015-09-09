# -*- encoding: utf-8 -*-
#
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2013 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#
#    Coded by: Jorge Angel Naranjo (jorge_nr@vauxoo.com)
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from openerp.osv import osv, fields


class res_partner(osv.Model):
    _inherit = 'res.partner'

    def _supplier_customer_advance_get(self, cr, uid, ids, field, arg, context=None):
        res = {}
        for id in ids:
            res = {id: {'customer_advance': 0.0, 'supplier_advance': 0.0}}
        return res
    _columns = {
        'property_account_supplier_advance': fields.property(
            type='many2one',
            relation='account.account',
            string="Advance Supplier Account",
            domain="[('type','in',('other', 'payable'))]",
            help="This account will be used for payment in advance of suppliers",
            required=False),
        'property_account_customer_advance': fields.property(
            type='many2one',
            relation='account.account',
            string="Advance Customer Account",
            domain="[('type','in',('other', 'receivable'))]",
            help="This account will be used for payment in advance of custom",
            required=False),
    
        'customer_advance': fields.function(
            _supplier_customer_advance_get,
            type='float',
            string='Total Customer Advance',
            multi='sc',
            help="Total amount of advance payment of custom."),
        'supplier_advance': fields.function(
            _supplier_customer_advance_get,
            type='float',
            string='Total Supplier Advance',
            multi='sc',
            help="Total amount of advance payment of suppliers."),

        }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: