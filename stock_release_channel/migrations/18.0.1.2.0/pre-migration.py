# Copyright 2025 Jacques-Etienne Baudoux (BCIM) <je@bcim.be>

from openupgradelib import openupgrade

from odoo.tools.sql import column_exists, create_column


@openupgrade.migrate()
def migrate(env, version):
    if not column_exists(env.cr, "stock_picking", "delivery_date"):
        create_column(env.cr, "stock_picking", "delivery_date", "date")
    env.cr.commit()
    return True
