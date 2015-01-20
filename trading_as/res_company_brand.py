# -*- coding: utf-8 -*-

##############################################################################
#
# Trading As Brands
# Copyright (C) 2015 OpusVL (<http://opusvl.com/>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api

class ResCompanyBrand(models.Model):
    _name = 'res.company.brand'

    legal_entity = fields.Many2one(
        comodel_name='res.company',
        required=True,
    )

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        required=True,
    )

    name = fields.Char(
        related=['partner_id', 'name'],
        string='Brand Name',
        required=True,
        readonly=True,
    )

    # HEADER
    logo = fields.Binary(related=['partner_id', 'image'])
    rml_header1 = fields.Text(string='Tagline')

    # FOOTER
    custom_footer = fields.Boolean(
        string='Custom footer?',
        help=(  'Check this to define the report footer manually.  ' +
                'Otherwise it will be filled in automatically.'
        ),
    )
    rml_footer = fields.Text(string='Report Footer')
    rml_footer_readonly = fields.Text(string='Report Footer', related=['rml_footer'],)
    phone = fields.Char(related=['partner_id', 'phone'])
    fax = fields.Char(related=['partner_id', 'fax'])
    email = fields.Char(related=['partner_id', 'email'])
    website = fields.Char(related=['partner_id', 'website'])



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
