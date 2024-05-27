from itertools import combinations
from commons.tetrahedron_volume import volume_of_tetrahedron
from typing import List, Tuple
from tqdm import tqdm
import multiprocessing

from dto.types import Points

def process_combinations(comb_chunk, points):
	local_smallest_volume = float('inf')
	local_best_combination = None

	for comb in comb_chunk:
			indices, selected_points = zip(*comb)
			if sum(p[3] for p in selected_points) == 100:
					vol = volume_of_tetrahedron(*selected_points)
					if vol < local_smallest_volume:
							local_smallest_volume = vol
							local_best_combination = indices
	return local_smallest_volume, local_best_combination

class FindTetrahedron:
	def __init__(self, points: List[Points]):
		self.points = points

	def find_smallest_tetrahedron(self) -> Tuple[List[int], float]:
		smallest_volume = float('inf')
		best_combination = None

		num_processes = multiprocessing.cpu_count()
		combs = list(combinations(enumerate(self.points), 4))
		comb_chunks = [combs[i::num_processes] for i in range(num_processes)]

		with multiprocessing.Pool(processes=num_processes) as pool:
				results = list(tqdm(pool.starmap(process_combinations, [(chunk, self.points) for chunk in comb_chunks]), total=num_processes))

		for local_smallest_volume, local_best_combination in results:
				if local_smallest_volume < smallest_volume:
						smallest_volume = local_smallest_volume
						best_combination = local_best_combination

		return (sorted(best_combination), smallest_volume) if best_combination else ([], 0.0)


# from itertools import combinations
# from commons.tetrahedron_volume import volume_of_tetrahedron

# class FindTetrahedron:
# 	def __init__(self, points):
# 		self.points = points

# 	def find_smallest_tetrahedron(self):
# 		smallest_volume = float('inf')
# 		best_combination = None
# 		for comb in combinations(enumerate(self.points), 4):
# 				indices, selected_points = zip(*comb)
# 				if sum(p[3] for p in selected_points) == 100:
# 						vol = volume_of_tetrahedron(*selected_points)
# 						if vol < smallest_volume:
# 								smallest_volume = vol
# 								best_combination = indices
# 		return sorted(best_combination), smallest_volume if best_combination else []