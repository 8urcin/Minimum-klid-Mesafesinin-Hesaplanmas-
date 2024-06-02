import math


coords = [(1, 2), (4, 6), (5, 7), (8, 9)]


def calculateEuclideanDistance(pt1, pt2):
    return math.sqrt((pt2[0] - pt1[0])**2 + (pt2[1] - pt1[1])**2)


distance_list = []
for index1 in range(len(coords)):
    for index2 in range(index1 + 1, len(coords)):
        dist = calculateEuclideanDistance(coords[index1], coords[index2])
        distance_list.append(dist)


min_distance = min(distance_list)

# Sonucu yazdırma
print("En kısa mesafe:", min_distance)
