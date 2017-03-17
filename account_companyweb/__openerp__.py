# -*- coding: utf-8 -*-
#
##############################################################################
#
#    Authors: Adrien Peiffer
#    Copyright (c) 2014 Acsone SA/NV (http://www.acsone.eu)
#    Copyright (c) 2015 BCIM sprl (http://www.bcim.be)
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
##############################################################################

{
    "name": "Companyweb",
    "version": "1.0",
    "author": "ACSONE SA/NV,BCIM sprl,Odoo Community Association (OCA)",
    "category": "Generic Modules/Accounting",
    "website": "http://www.acsone.eu",
    "depends": [
        'account_financial_report_webkit',
        'base_vat',
        'account',
        # TODO: account voucher is required
        #       for the test suite only
        #       (need to refactor the test suite)
        'account_voucher',
    ],
    'external_dependencies': {
        'python': ['lxml', 'xlwt', 'xlrd'],
    },
    "data": [
        "views/companyweb_history.xml",
        "views/res_config_view.xml",
        "views/res_partner_view.xml",
        "wizard/partner_update_companyweb.xml",
        "wizard/companyweb_follow_customer.xml",
        "data/cron_fetch_new_modification.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
}
