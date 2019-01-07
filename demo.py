from bosch_glm import GLMxxC

rangefinder = GLMxxC()
if not rangefinder.connected:
    exit(1)

distance = rangefinder.measure_from_tripod_socket()
if distance is not -1:
    print(distance, 'mm')
