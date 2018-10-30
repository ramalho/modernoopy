import dataclasses


@dataclasses.dataclass
class Country:
    """Represents a country with some metadata"""

    name: str
    population: float
    area: float

    def density(self) -> float:
        """population density in persons/km²"""
        return self.population / self.area
