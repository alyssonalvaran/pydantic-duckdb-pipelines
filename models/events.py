"""
Data models for event validation and schema enforcement.
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class BaseEvent(BaseModel):
    """Base schema for all tracking events to ensure standard metadata."""
    event_id: str = Field(..., description="Unique UUID for the event.")
    event_name: str = Field(..., description="Standardized event name in dot notation (e.g., 'user.signup').")
    timestamp: datetime = Field(..., description="UTC timestamp of the event.")
    tenant_id: str = Field(..., description="Subdomain or unique identifier for the tenant.")


class UserSignupEvent(BaseEvent):
    """Schema specifically for user signup payload validation."""
    user_id: int = Field(..., description="Unique ID assigned to the new user.")
    plan_type: str = Field(..., pattern="^(free|pro|enterprise)$", description="Subscription plan selected during signup.")
    referral_source: Optional[str] = Field(None, description="Origin of the referral, if applicable.")
