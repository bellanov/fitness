"""Exercise Model."""

from pydantic import Field

from api.domain.models.camel_case import CamelCaseModel

# TODO: Going to have an enumeration of all exercises, but for now, just a string will suffice.

class Exercise(CamelCaseModel):
    """Represents an exercise.

    Attributes:
        id: The ID of the exercise.
        name: The name of the exercise.
    """

    name: str = Field(..., min_length=1, max_length=100)