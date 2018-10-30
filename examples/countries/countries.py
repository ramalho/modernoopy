
import dataclasses

pop10 = [
    ('China', 1_394_897_526, 9_640_821),
    ('India', 1_338_906_197, 3_287_240),
    ('United States', 328_088_060, 9_833_517),
    ('Indonesia', 265_015_300, 1_904_569),
    ('Brazil', 209_780_729, 8_515_767),
    ('Pakistan', 202_499_217, 803_940),
    ('Nigeria', 195_875_237, 923_768),
    ('Bangladesh', 165_446_400, 143_998),
    ('Russia', 146_877_088, 17_125_242),
    ('Japan', 126_440_000, 377_944),
]

@dataclasses.dataclass
class Country:
	"""Represents a country with some metadata"""
	name: str
	population: float
	area: float

	def density(self) -> float:
		"""population density in persons/km²"""
		return self.population / self.area


