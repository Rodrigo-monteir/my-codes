import math

vel_norte= 3
vel_oeste= 4

tempo= 15

dist_norte= vel_norte * tempo
dist_oeste= vel_oeste * tempo

distancia= math.sqrt(dist_norte**2 + dist_oeste**2)

print(int(distancia))
