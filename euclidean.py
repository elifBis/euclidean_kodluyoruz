import math

points = [(1,2),(3,4),(5,6),(7,8)]
distances = []

def euqlideanDistance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 +(point1[1]-point2[1])**2)

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euqlideanDistance(points[i], points[j])
        distances.append(distance)

minDistance = min(distances)
print(minDistance)