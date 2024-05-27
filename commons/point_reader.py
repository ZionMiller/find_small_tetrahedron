from typing import List

from dto.types import Points

class PointReader:
	@staticmethod
	def read_points_from_file(filename: str) -> List[Points]:
		print("reading points")
		points = []
		with open(filename, 'r') as file:
				for line in file:
						x, y, z, n = map(float, line.strip().strip('()').split(', '))
						points.append((x, y, z, int(n)))
		return points
