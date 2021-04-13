def greedy_frac_knapsack(porfit, weight, max_weight):
    if len(profit) != len(weight):
        return 'lengths should be equal'
    if max_weight <= 0:
        return 'max weight should be positive'

    for prof, wgt in zip(profit, weight):
        if prof < 0 or wgt < 0:
            return 'profit and weight should be positive'

    prof_by_wgt = []
    for prof, wgt in zip(profit, weight):
        prof_by_wgt.append([(prof / wgt), wgt, prof])

    sorted_prof_by_wgt = sorted(prof_by_wgt, key=lambda x: x[0], reverse=True)
    print(sorted_prof_by_wgt)

    total_gain = 0
    curr_weight = 0
    for val in sorted_prof_by_wgt:
        if curr_weight == max_weight:
            break
        if (curr_weight + val[1]) < max_weight:
            total_gain += val[2]
            curr_weight += val[1]
        else:
            fraction = (max_weight - curr_weight) / val[1]
            total_gain += (val[2] * fraction)
            break
    return total_gain


profit = [int(x) for x in input("Input profits separated by spaces: ").split()]
weight = [int(x) for x in input("Input weights separated by spaces: ").split()]
max_weight = int(input("Max weight allowed: "))

print(greedy_frac_knapsack(profit, weight, max_weight))
