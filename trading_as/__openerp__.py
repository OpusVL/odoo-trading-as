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


{
    'name': 'Trading As Brands',
    'version': '0.1',
    'author': 'OpusVL',
    'website': 'http://opusvl.com/',
    'summary': 'Allow company to present different branding on documents sent to different customers',
    
    'description': """Allow company to present different branding on documents sent to different customers,
""",
    'images': [
    ],
    'depends': [
    ],
    'data': [
        'res_partner_view.xml',
        'res_company_brand_view.xml',
        'res_company_view.xml',
        'report_external_layout_modification.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
