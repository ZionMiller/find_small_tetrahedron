import numpy as np
from itertools import combinations

# Proposed enhancment for volume calculation

def volume_of_tetrahedron(p1, p2, p3, p4):
    p1, p2, p3, p4 = np.array(p1[:3]), np.array(p2[:3]), np.array(p3[:3]), np.array(p4[:3])
    AB = p2 - p1
    AC = p3 - p1
    AD = p4 - p1
    volume = np.abs(np.dot(AD, np.cross(AB, AC))) / 6.0
    return volume

# Provided function for volume calculation
# def volume_of_tetrahedron(p1, p2, p3, p4):
#     AB = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
#     AC = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
#     AD = (p4[0] - p1[0], p4[1] - p1[1], p4[2] - p1[2])

#     cross_product_x = AB[1] * AC[2] - AB[2] * AC[1]
#     cross_product_y = AB[2] * AC[0] - AB[0] * AC[2]
#     cross_product_z = AB[0] * AC[1] - AB[1] * AC[0]

#     scalar_triple_product = (
#         AD[0] * cross_product_x +
#         AD[1] * cross_product_y +
#         AD[2] * cross_product_z
#     )

#     volume = abs(scalar_triple_product) / 6.0
#     print("volumes are", volume)
#     return volume