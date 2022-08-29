# copyright 2022 Sodexis
# license OPL-1 (see license file for full copyright and licensing details).

from odoo import models, fields, api


class TutorialJavascript(models.Model):
    _name = 'tutorial.javascript'
    _description = 'tutorial.javascript'

    name = fields.Char(
        string="Name",
    )
    field_one = fields.Integer('Field One', default=1)
