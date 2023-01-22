def get_medal(my_time, time1, time2, time3):
    times = [my_time, time1, time2, time3]
    times.sort()
    if my_time == times[0]:
        return "gold"
    elif my_time == times[1]:
        return "silver"
    elif my_time == times[2]:
        return "bronze"
    else:
        return "no medal"

print(get_medal(1,4,11,12))