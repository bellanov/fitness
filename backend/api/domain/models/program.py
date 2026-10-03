"""Program Model."""

from pydantic import Field

from api.domain.models.camel_case import CamelCaseModel

# TODO: Define the program model
#
# Make sense of the following concepts:
#  Type => Fitness, Rehabilitation, Strength, Endurance, etc.
#  Schedule => Establish a concept of scheduling.


class Program(CamelCaseModel):
    """Represents a program.

    Attributes:
        id: The ID of the program.
        name: The name of the program.
    """

    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(None, min_length=1, max_length=200)
    type: str = Field(..., min_length=1, max_length=100)
