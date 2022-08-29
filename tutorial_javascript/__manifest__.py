# Copyright 2022 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    "name": "Tutorial Javascript",
    "summary": """
        Short (1 phrase/line) summary of the module"s purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    "version": "14.0.1.0.0",
    "category": "Uncategorized",
    "website": "http://sodexis.com/",
    "author": "Sodexis",
    "license": "OPL-1",
    "installable": True,
    "application": True,
    "depends": [
        "base",
        "web",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/tutorial_javascript_views.xml",
    ],
    "qweb": [
        "static/src/xml/widget_one_template.xml",
    ]
}
