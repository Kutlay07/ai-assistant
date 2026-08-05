from dataclasses import dataclass


@dataclass(frozen=True)
class Plan:
    steps: list[str]