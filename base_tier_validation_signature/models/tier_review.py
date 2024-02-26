# Copyright 2019 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields

class TierReview(models.Model):
    _inherit = "tier.review"

    signature = fields.Binary()