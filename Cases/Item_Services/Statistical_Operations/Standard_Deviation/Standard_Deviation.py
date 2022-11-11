import math

## use this to get the std dev for historic market data


def Running_Standard_Deviation(price_entries):

    calculations = len(price_entries)
    deviations = []
    total = 0

    for entry in range(calculations):

        total += price_entries[entry]
        deviations.append(Single_Standard_Deviation(total/(entry+1), price_entries[:entry]))

    return deviations


def Single_Standard_Deviation(mean, points):

    total = 0

    for point in points:

        total+= ((point-mean)**2)
    
    return math.sqrt(total/(len(points)+1))