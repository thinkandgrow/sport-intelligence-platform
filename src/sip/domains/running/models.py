from dataclasses import dataclass


@dataclass
class Runner:
    """
    Represents a race participant.
    """

    bib_number: str
    name: str
    city: str
    country: str
    team: str | None