import matplotlib.pyplot as plt


def display_restaurant_example(filename):
    plt.figure(figsize=(6.5, 4.55))
    plt.yticks(fontsize=14)
    plt.xlabel('Time Interval (Minutes)', fontsize=14)
    plt.ylabel("Count", fontsize=14)
    plt.tight_layout()

    timestamps = [x for x in range(1, 31)]
    count = [
        2,
        4,
        4,
        4,
        5,
        6,
        7,
        9,
        9,
        11,
        12,
        14,
        14,
        14,
        15,
        17,
        17,
        18,
        19,
        19,
        19,
        19,
        19,
        20,
        20,
        20,
        20,
        21,
        23,
        23,
    ]
    plt.plot(timestamps, count, marker='o', markersize='6')

    plt.ylim(min(min(count), min(count)) * 0.4,
             max(max(count), max(count)) * 1.1)

    plt.savefig(f'{filename}.pdf', format='pdf')
    print(f'saved to {filename}.pdf')
    plt.show()


def display_count_with_fixed_usd(filename):
    plt.figure(figsize=(6.5, 4.55))
    plt.yticks(fontsize=14)
    plt.xlabel('USD', fontsize=14)
    plt.ylabel("Count", fontsize=14)
    plt.tight_layout()

    timestamps = [x*10 for x in range(1, 11)]
    count_5min = [
        0.866666667, 2.155555556, 2.133333333, 2.644444444, 4.333333333, 4.2, 2.8, 3.311111111, 4.2, 7.533333333
    ]
    count_10min = [
        1.644444444, 3.577777778, 4.6, 5.133333333, 9.177777778, 8.622222222, 5.688888889, 6.777777778, 7.533333333, 16.24444444
    ]
    count_15min = [
        2.422222222, 5.088888889, 7.266666667, 7.555555556, 14.35555556, 12.33333333, 8.266666667, 10.06666667, 11.93333333, 23.26666667
    ]
    count_20min = [
        3.177777778, 7.111111111, 10.04444444, 10, 19.11111111, 15.88888889, 11.33333333, 13.33333333, 15.15555556, 31.11111111
    ]

    plt.plot(timestamps, count_5min, marker='o', markersize='6', label="5 minutes")
    plt.plot(timestamps, count_10min, marker='o', markersize='6', label="10 minutes")
    plt.plot(timestamps, count_15min, marker='o', markersize='6', label="15 minutes")
    plt.plot(timestamps, count_20min, marker='o', markersize='6', label="20 minutes")

    plt.ylim(min(min(count_5min), min(count_10min), min(count_15min), min(count_20min)) * 0.4,
             max(max(count_5min), max(count_10min), max(count_15min), max(count_20min)) * 1.1)
    plt.legend(fontsize=14, loc='upper left')

    plt.savefig(f'{filename}.pdf', format='pdf')
    print(f'saved to {filename}.pdf')
    plt.show()


def display_count_with_fixed_time(filename):
    plt.figure(figsize=(6.5, 4.55))
    plt.yticks(fontsize=14)
    plt.xlabel('USD', fontsize=14)
    plt.ylabel("Count", fontsize=14)
    plt.tight_layout()

    timestamps = [x*10 for x in range(1, 11)]
    count_5percent = [
        5.666666667, 11.22222222, 15.73333333, 16.08888889, 28.95555556, 24.4, 19.35555556, 20.51111111, 23.75555556, 45.46666667
    ]
    count_10percent = [
        11.68888889, 20.62222222, 27.15555556, 29.11111111, 51.68888889, 42.11111111, 37.71111111, 39.64444444, 46.48888889, 76.66666667
    ]
    count_15percent = [
        16.6, 30.22222222, 37.46666667, 43.35555556, 72.24444444, 61.22222222, 57.35555556, 58.95555556, 73.13333333, 104.8444444
    ]

    plt.plot(timestamps, count_5percent, marker='o', markersize='6', label="5%")
    plt.plot(timestamps, count_10percent, marker='o', markersize='6', label="10%")
    plt.plot(timestamps, count_15percent, marker='o', markersize='6', label="15%")

    plt.ylim(min(min(count_5percent), min(count_10percent), min(count_15percent)) * 0.4,
             max(max(count_5percent), max(count_10percent), max(count_15percent)) * 1.1)
    plt.legend(fontsize=14, loc='upper left')

    plt.savefig(f'{filename}.pdf', format='pdf')
    print(f'saved to {filename}.pdf')
    plt.show()


if __name__ == '__main__':
    display_restaurant_example("../figures/restaurant_example")
    display_count_with_fixed_usd("../figures/fixed_usd_3percent")
    display_count_with_fixed_time("../figures/fixed_time_20min")
