# -*- coding: utf-8 -*-

##############################################################################
#
# Trading As Email Branding
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

from openerp import fields

class BrandableModelMixin(object):
    """Mixin to add a brand field with the correct lookup semantincs
    for branding emails.
    """
    brand = fields.Many2one(
        related=['partner_id', 'brand'],
        comodel_name='res.company.brand',
        readonly=True,
        required=False,
    )



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
