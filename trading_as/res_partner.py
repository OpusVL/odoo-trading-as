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

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_trading_name = fields.Boolean(
        help='Tick this if this partner represents a trading name of your company',
    )
    trading_as_partner = fields.Many2one(
        help=(
            'The trading name to use for branding documents for this partner.\n' +
            'If blank, the default company branding will be used.'
        ),
        comodel_name='res.partner',
        domain=[
            ('is_trading_name', '=', True),
        ],
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
