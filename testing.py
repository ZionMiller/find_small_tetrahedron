from typing import List, Tuple
from tqdm import tqdm

# TODO Enhacements:
# 1) Add chunking and multi processing
# 2) further optimize volume method using numpy
# 3) adjust target to be more dynamic and handle future cases
# 4) Validate input to ensure we are receive everything we expect
# 5) 

def volume_of_tetrahedron(p1, p2, p3, p4):
    AB = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
    AC = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
    AD = (p4[0] - p1[0], p4[1] - p1[1], p4[2] - p1[2])

    cross_product = (
        AB[1] * AC[2] - AB[2] * AC[1],
        AB[2] * AC[0] - AB[0] * AC[2],
        AB[0] * AC[1] - AB[1] * AC[0]
    )

    scalar_triple_product = AD[0] * cross_product[0] + AD[1] * cross_product[1] + AD[2] * cross_product[2]

    volume = abs(scalar_triple_product) / 6.0
    return volume

def four_sum_tetrahedron(points: List[List[float]]) -> Tuple[float, List[List[float]]]:
    points.sort(key=lambda x: x[3])  

    n = len(points)
    min_volume = float('inf')
    min_volume_combination = None

    left, right = 0, n - 1

    while left < right - 2:
        p1 = points[left]
        p4 = points[right]

        i, j = left + 1, right - 1
        while i < j:
            p2, p3 = points[i], points[j]
            current_sum = p1[3] + p2[3] + p3[3] + p4[3]

            if current_sum == 100:
                volume = volume_of_tetrahedron(p1[:3], p2[:3], p3[:3], p4[:3])
                if volume < min_volume:
                    min_volume = volume
                    min_volume_combination = [p1, p2, p3, p4]
                i += 1
                j -= 1
            elif current_sum < 100:
                i += 1
            else:
                j -= 1

        if points[left][3] + points[left + 1][3] + points[left + 2][3] + points[right][3] >= 100:
            right -= 1
        else:
            left += 1

    return min_volume, min_volume_combination

data = []
with open("points_small.txt", "r") as file:
    for index, line in enumerate(file):
        point = [float(x.strip()) for x in line.strip()[1:-1].split(",")]
        point.append(index)  
        data.append(point)

min_volume, min_volume_combination = four_sum_tetrahedron(data)

print("Smallest volume combination:")
if min_volume_combination is not None:
    indices = sorted([point[4] for point in min_volume_combination])  
    for i, index in enumerate(indices):
        point = min_volume_combination[i][:3]
        print(f"Point {i}: Index {index} - Coordinates {point}")
    print(f"Volume: {min_volume}")
else:
    print("No valid combination found.")

