import math

def main():
    

    num_sensors, max_distance = input().split(' ')

    sensors = []
    sensor_lists = []

    for _ in range(0, int(num_sensors)):
        x, y = input().split(' ')
        sensors.append((int(x), int(y)))

    for index_a, sensor_a in enumerate(sensors):
        sensors_near = []
        for index_b, sensor_b in enumerate(sensors):
            if is_within_range(sensor_a, sensor_b, int(max_distance)):
                sensors_near.append(index_b + 1)
        sensor_lists.append(sensors_near)

    max = 0
    sensor_list = []
    for sensors in sensor_lists:
        if len(sensors) > max:
            max = len(sensors)
            sensor_list = sensors

    print(len(sensor_list))
    sensor_list = [str(sensor) for sensor in sensor_list]
    print(' '.join(sensor_list))

    
def is_within_range(sensor_a: tuple, sensor_b: tuple, range: int) -> bool:

    if math.sqrt(((abs(sensor_a[0] - sensor_b[0]) ** 2) + (abs(sensor_a[1] - sensor_b[1])) ** 2)) <= range:
        return True
    return False

if __name__ == '__main__':
    main()