from pydantic import BaseModel, Field
from typing import Optional
from pydantic import field_validator
from app.utils.normalizer import Normalizer

class FNOLClaim(BaseModel):

    policyNumber: Optional[str] = Field(default=None)
    policyholderName: Optional[str] = Field(default=None)
    effectiveDates: Optional[str] = Field(default=None)

    incidentDate: Optional[str] = Field(default=None)
    incidentTime: Optional[str] = Field(default=None)
    location: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)

    claimant: Optional[str] = Field(default=None)
    thirdParties: Optional[str] = Field(default=None)
    contactDetails: Optional[str] = Field(default=None)

    assetType: Optional[str] = Field(default=None)
    assetId: Optional[str] = Field(default=None)

    estimatedDamage: Optional[float] = Field(default=None)

    claimType: Optional[str] = Field(default=None)

    attachments: Optional[str] = Field(default=None)

    initialEstimate: Optional[float] = Field(default=None)

    @field_validator("estimatedDamage", mode="before")
    @classmethod
    def validate_damage(cls, value):
        return Normalizer.parse_currency(value)


    @field_validator("initialEstimate", mode="before")
    @classmethod
    def validate_estimate(cls, value):
        return Normalizer.parse_currency(value)