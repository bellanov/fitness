"""Schedule Model."""

from pydantic import Field

from api.domain.models.camel_case import CamelCaseModel

# TODO: Define the schedule model
#
# Make sense of the following concepts:
#
#   Exercise
#   Date
#   Sets
#   Reps
#   Duration


class Schedule(CamelCaseModel):
    """Represents a schedule.

    Attributes:
        id: The ID of the schedule.
        name: The name of the schedule.
    """

    name: str = Field(..., min_length=1, max_length=100)
