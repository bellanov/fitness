"""Organization Model."""

from pydantic import Field

from api.domain.models.camel_case import CamelCaseModel

# TODO: How to ensure organizations are unique?

class Organization(CamelCaseModel):
    """Represents an organization.

    Attributes:
        id: The ID of the organization.
        name: The name of the organization.
    """

    name: str = Field(..., min_length=1, max_length=100)
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    address: str = Field(..., min_length=1, max_length=100)
    state: str = Field(..., min_length=1, max_length=100)
    zip_code: str = Field(..., min_length=1, max_length=100)
    phone_number: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., min_length=1, max_length=100)
