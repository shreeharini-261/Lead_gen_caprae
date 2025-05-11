# routes/client_dashboard_controller.py
from flask_login import current_user
from models.user_model import Lead, Subscription
from flask import render_template
from sqlalchemy import and_
from . import db

def get_client_stats():
    leads = Lead.query.filter_by(user_id=current_user.id).all()
    high_score = [lead for lead in leads if lead.score and lead.score > 80]

    subscription = Subscription.query.filter_by(user_id=current_user.id).first()
    used = len(leads)
    limit = subscription.lead_limit if subscription else 0

    return {
        "subscription_name": subscription.package_name if subscription else "None",
        "lead_limit": limit,
        "leads_used": used,
        "percentage": (used / limit) * 100 if limit else 0,
        "total_leads": used,
        "high_scoring_leads": len(high_score),
        "leads": leads
    }
