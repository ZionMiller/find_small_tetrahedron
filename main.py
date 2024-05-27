from commons.point_reader import PointReader
from commons.find_tetrahedron import FindTetrahedron
from tqdm import tqdm

def process_points(points_file: str):
    points = PointReader.read_points_from_file(points_file)
    smallest_tetrahedron, smallest_volume = FindTetrahedron(points).find_smallest_tetrahedron()
    print(f"Smallest tetrahedron for {points_file}: {smallest_tetrahedron}, with a volume: {smallest_volume}")

def main():
    small_points_file = 'points_small.txt'
    large_points_file = 'points_large.txt'

    points_files = [small_points_file, large_points_file]

    for points_file in points_files:
        print(f"Processing {points_file}...")
        process_points(points_file)

if __name__ == "__main__":
    main()
