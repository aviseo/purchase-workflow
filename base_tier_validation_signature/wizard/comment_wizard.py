# Copyright 2019 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CommentWizard(models.TransientModel):
    _inherit = "comment.wizard"
    
    signature = fields.Image()

    def add_comment(self):
        self.ensure_one()
        rec = self.env[self.res_model].browse(self.res_id)
        self.review_ids.write({"comment": self.comment, "signature": self.signature})
        if self.validate_reject == "validate":
            rec._validate_tier(self.review_ids)
        if self.validate_reject == "reject":
            rec._rejected_tier(self.review_ids)
        rec._update_counter({"review_deleted": True})