def countMinPlatforms(arrivals, departures):
    arrs = []
    deps = []
    for idx in range(len(arrivals)):
        if arrivals[idx] != departures[idx]:
            arrs.append(arrivals[idx])
            deps.append(departures[idx])
    arrivals = sorted(arrs)
    departures = sorted(deps)
    min_count = 1
    count = 1
    arr_idx = 1
    depart_idx = 0
    while arr_idx < len(arrivals) and depart_idx < len(departures):
        if arrivals[arr_idx] < departures[depart_idx]:
            count += 1
            arr_idx += 1
            min_count = max(min_count, count)
        else:
            depart_idx += 1
            count -= 1
    return min_count

if __name__ == '__main__':
    assert countMinPlatforms([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]) == 3
    assert countMinPlatforms([900,1100,1235],[1000,1200,1240]) == 1

    