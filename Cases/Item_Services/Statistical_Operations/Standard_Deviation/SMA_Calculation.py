
## use this to get the sma for historic market data

def Single_SMA_Calcuation(price_entries):

    calculations = len(price_entries)
    summation = 0

    for entry in price_entries:
        summation += entry
    
    SMA = summation/(calculations+1)

    return SMA


def Running_SMA_Calcuation(price_entries):

    calculations = len(price_entries)
    averages = []

    for entry in range(calculations):
        averages.append(Single_SMA_Calcuation(price_entries[:entry]))

    return averages