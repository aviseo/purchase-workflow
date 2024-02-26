# Copyright 2019 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields
import base64

class TierReview(models.Model):
    _inherit = "tier.review"

    signature = fields.Image()

    signature_b64 = fields.Char(compute="_compute_signature_b64")

    @api.depends("signature")
    def _compute_signature_b64(self):
        for rec in self:
            rec.signature_b64 = rec.signature and base64.b64encode(rec.signature).decode("utf-8") or False
    