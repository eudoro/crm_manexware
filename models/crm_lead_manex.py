# -*- coding: utf-8 -*-

import logging
from odoo import fields, models
from odoo.tools.translate import _
from odoo.exceptions import UserError, AccessError

_logger = logging.getLogger(__name__)

class LeadManex(models.Model):
    _inherit = 'crm.lead'

    planned_revenue_recurrent = fields.Float('Expected Revenue Recurrent', track_visibility='always')
    recurrent_months = fields.Integer('Recurrent Months', help="Tiempo del servicio")