from models.extensions import db
from uuid import uuid4
from datetime import datetime
import enum


class EventStatus(enum.Enum):
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    HYBRID = "HYBRID"


class EventType(enum.Enum):
    HACKATHON = "hackathon"
    MEETUP = "meetup"
    WORKSHOP = "workshop"


class Events(db.Model):
    __tablename__ = "events"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))

    event_name = db.Column(db.String(100), nullable=False, index=True)
    event_description = db.Column(db.String(255), nullable=False)

    event_start_date = db.Column(db.DateTime, nullable=False, index=True)
    event_end_date = db.Column(db.DateTime, nullable=False)
    event_registration_deadline = db.Column(db.DateTime, nullable=False)

    members = db.relationship("Members", back_populates="event")

    event_type = db.Column(
        db.Enum(EventType, name="event_type_name"),
        nullable=False,
        default=EventType.HACKATHON
    )

    event_assignees = db.Column(db.JSON, nullable=True, default=lambda: {})
    event_organization = db.Column(
        db.String(255),
        nullable=False,
        default="Aurenith.team"
    )

    event_status = db.Column(
        db.Enum(EventStatus, name="event_status_name"),
        nullable=False,
        default=EventStatus.HYBRID,
        index=True
    )

    event_location = db.Column(db.String(255), nullable=True, default="TBD")
    event_themes = db.Column(db.JSON, nullable=True, default=lambda: {})
    event_rules = db.Column(db.JSON, nullable=True, default=lambda: {})

    @property
    def event_duration(self):
        return (self.event_end_date - self.event_start_date).days


