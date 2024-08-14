import matplotlib.pyplot as plt
import math

def collatz(end):
    n = []
    times = []
    maxes = []
    max_time = 0
    max_maxes = 0
    stop_time = {}
    max_number = {}
    stop_time[1] = 0
    max_number[1] = 1
    average_times = [0 for i in range(1000)]

    # Iterating for odd numbers in the range
    for i in range(1, 10**end):
        if i % 2 == 1:
            # Going through iterations till finding a know number
            num = i
            nums = []
            while num not in stop_time:
                nums.append(num)
                if num % 2 == 1:
                    num = 3 * num + 1
                else:
                    num //= 2

            # Updating variables
            count = 0
            j = len(nums)-1
            max = max_number[num]
            while j != -1:
                if nums[j] % 2 == 1:
                    if nums[j] > max:
                        max = nums[j]
                    count += 1
                stop_time[nums[j]] = count + stop_time[num]
                max_number[nums[j]] = max
                j -= 1
            if max_time < stop_time[i]:
                max_time = stop_time[i]
            if max_maxes < max_number[i]:
                max_maxes = max_number[i]
            n.append(i)
            times.append(stop_time[i])
            if i < 10**(end-3):
                maxes.append(max_number[i])
            average_times[i // 10**(end-3)] += stop_time[i] * 2 / 10**(end-3)

    #Graphs
    ax = plt.axes()
    #ax.set_xlim(0, max_time+1)
    #plt.xlabel("Stopping time")
    #plt.ylabel("Frequency")
    #plt.hist(times, max_time)
    ax.set_xlim(0, 10**end)
    #ax.set_ylim(0, max_time+1)
    #plt.xlabel("Number")
    #plt.ylabel("Stopping time")
    #plt.scatter(n, times, s=3)
    #ax.set_xlim(0, 10**(end-3))
    #ax.set_ylim(0, 10**(end-2))
    #plt.ylabel("Max reached")
    #plt.scatter(n[:5*10**(end-4)], maxes, s=3)

    plt.xlabel("Average Number in intervals of " + str(10**(end-3)))
    plt.ylabel("Average Stopping time")
    plt.scatter([5 * 10 ** (end - 4) + 10 ** (end - 3) * i for i in range(1000)], average_times, color = "green")
    x = [math.log(5 * 10 ** (end - 4) + 10 ** (end - 3) * i) for i in range(1000)]
    x_mean = 0
    mean_time = 0
    for i in range(1000):
        x_mean += x[i] / 1000
        mean_time += average_times[i] / 1000
    slope = 0
    x_deviation = 0
    for i in range(1000):
        slope += (x[i] - x_mean) * (average_times[i] - mean_time)
        x_deviation += (x[i] - x_mean) ** 2
    slope /= x_deviation
    intercept = mean_time - slope * x_mean
    plt.plot([5 * 10 ** (end - 4) + 10 ** (end - 3) * i for i in range(1000)], [slope*x[i] + intercept for i in range(1000)], label = "" + str(round(slope, 3)) + "ln(n) + " + str(round(intercept,3)))
    plt.legend()
    plt.show()

collatz(7)