###################################################################################
#
#    Copyright (c) 2017-today MuK IT GmbH.
#
#    This file is part of MuK Theme
#    (see https://mukit.at).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

{
    'name': 'Inisiacore Theme', 
    'summary': 'Odoo Community Backend Theme',
    'version': '1.1.2', 
    'category': 'Themes/Backend', 
    'license': 'LGPL-3', 
    'author': 'MuK IT',
    'website': 'http://www.mukit.at',
    'live_test_url': 'https://mukit.at/r/SgN',
    'contributors': [
        'Mathias Markl <mathias.markl@mukit.at>',
    ],
    'depends': [
        'web',
        'base',
        'base_setup',
        'web_editor',
        'mail',
    ],
    'excludes': [
        'web_enterprise',
    ],
    'data': [
       'templates/webclient.xml',
       'views/res_config_settings_view.xml',
       'views/res_users.xml',
    #    'views/base.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            'inisiacore_theme/static/src/**/*.xml',
            'inisiacore_theme/views/base.xml',
        ],
        'web._assets_primary_variables': [
            'inisiacore_theme/static/src/colors.scss',
        ],
        'web._assets_backend_helpers': [
            'inisiacore_theme/static/src/variables.scss',
            'inisiacore_theme/static/src/mixins.scss',
        ],
        'web.assets_backend': [
            'inisiacore_theme/static/src/webclient/**/*.scss',
            'inisiacore_theme/static/src/webclient/**/*.js',
            'inisiacore_theme/static/src/search/**/*.scss',
            'inisiacore_theme/static/src/search/**/*.js',
            'inisiacore_theme/static/src/legacy/**/*.scss',
            'inisiacore_theme/static/src/legacy/**/*.js',
        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.png'
    ],
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'installable': True,
    'application': False,
    'auto_install': True,
    'uninstall_hook': '_uninstall_reset_changes',
}
