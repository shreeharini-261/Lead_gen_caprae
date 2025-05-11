from datetime import datetime
from . import db

class Subscription(db.Model):
    __tablename__ = 'subscriptions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    package_name = db.Column(db.String(50), default='Basic')
    lead_limit = db.Column(db.Integer, default=100)
    leads_used = db.Column(db.Integer, default=0)
    expires_at = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def remaining_leads(self):
        return max(0, self.lead_limit - self.leads_used)

    def __repr__(self):
        return f'<Subscription {self.package_name} for User {self.user_id}>'