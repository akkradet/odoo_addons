 # -*- coding: utf-8 -*-
{
    'name': "Sarabun font",

    'summary': """
        change default font to Sarabun font""",

    'description': """
        change default font to Sarabun font
 ,
    """,
    'author': "Akkradet.K",
    'website': "https://github.com/akkradet/odoo_addons",
    'category': 'Localization',
    'version': '15.0.0.1',
    'depends': ['web'],
    'qweb': [],
    'images': ['static/description/banner.png'],
    'assets': {
        'web.assets_common': [
            'sarabun_font/static/src/scss/sarabunfont.scss',
            'sarabun_font/static/src/css/web_style.css',
        ],
        'web.report_assets_common': [
            'sarabun_font/static/src/scss/sarabunfont.scss',
        ],
    },
    'license': 'AGPL-3',
    'auto_install': True,
    'installable': True,
}