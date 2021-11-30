import matplotlib.pyplot as plt
import numpy as np
import datetime


def query_restaurant():
    with open('../dataset/data_20211119.txt', 'r') as input_file:
        time_value_pair = [line.rstrip('\n').split(' ') for line in input_file.readlines()]

    time_value_pair = [(int(t), float(v)) for t, v in time_value_pair]
    time_value_pair = [(t, v) for t, v in time_value_pair if v < 2000]

    goal_time = 1637301060
    MINUTE = 60
    HOUR = 3600

    value_list = [(13.5, 15.5)]

    time_range = [(goal_time - i * MINUTE, goal_time + i * MINUTE) for i in [x/2 for x in range(1, 31)]]

    for time_lower, time_upper in time_range:
        print(datetime.datetime.utcfromtimestamp(time_lower).strftime('%Y-%m-%d %H:%M:%S'),
              datetime.datetime.utcfromtimestamp(time_upper).strftime('%Y-%m-%d %H:%M:%S'))

    for value_lower, value_upper in value_list:
        print('For transactions between USD {:.2f} and {:.2f}:'.format(value_lower, value_upper))
        for time_lower, time_upper in time_range:
            count = len([None for timestamp, value in time_value_pair
                         if value_lower <= value <= value_upper and time_lower <= timestamp <= time_upper])
            print(count)
        print()


def query_with_fixed_usd():
    with open('../dataset/data_20211118.txt', 'r') as input_file:
        time_value_pair = [line.rstrip('\n').split(' ') for line in input_file.readlines()]

    time_value_pair = [(int(t), float(v)) for t, v in time_value_pair]
    time_value_pair = [(t, v) for t, v in time_value_pair if v < 2000]

    min_time = min([item[0] for item in time_value_pair])
    time_value_pair = [(t - min_time, v) for t, v in time_value_pair]

    timestamps = [item[0] for item in time_value_pair]

    middle_time = (min(timestamps) + max(timestamps)) / 2  # Average of the min and max

    MINUTE = 60
    HOUR = 3600

    usd_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    usd_ratio = [0.075]
    value_list = [(usd * (1 - ratio), usd * (1 + ratio)) for usd in usd_range for ratio in usd_ratio]
    print(value_list)

    timestamp_set = [middle_time + i * 30 * MINUTE for i in range(-22, 23)]

    time_range = [(-i * MINUTE, i * MINUTE) for i in [2.5, 5, 7.5, 10]]

    for value_lower, value_upper in value_list:
        print('For transactions between USD {:.2f} and {:.2f}:'.format(value_lower, value_upper))

        for lower_offset, upper_offset in time_range:
            count = np.average([
                len([None for t, v in time_value_pair
                         if value_lower <= v <= value_upper and
                     lower_offset + timestamp <= t <= upper_offset + timestamp])
                for timestamp in timestamp_set])
            print(count)
        print()


if __name__ == '__main__':
    # query_restaurant()
    query_with_fixed_usd()
