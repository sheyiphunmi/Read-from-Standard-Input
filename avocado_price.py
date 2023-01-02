import sys
import numpy as np

"""
Run with python avocado_price.py in terminal.

Program reads line from standard input

Input:
    
    A sales data with three coulms: Date, Price, region.

    e.g
    date,price,region
    2016-11-09,1.39,LosAngeles
    2017-11-09,1.68,Mexico
    2015-11-16,1.31,SanDiego
    2016-11-04,1.99,LosAngeles
    2017-11-03,1.48,Mexico
    2015-11-19,1.21,SanDiego
    
Output:
     min
     max
     mean
     std (sample)

"""

data = []    
for line in sys.stdin:
    if 'exit' ==  line.rstrip():
        break
    else:
        data.append(line)

# Convert element with index 1 - price, in the list created from split 
    # then append the float to a price
price = []
for i in range(1, len(data)):
    new_data = data[i].split(",")
    #price.append(float(data[i].split(",")[1]))
    price.append(float(new_data[1]))

#print(price)
min_price = min(price)
#rounding off to 2dp
min_price = round(min_price,2)

###Maximum price
max_price = max(price)
#rounding off to 2dp
max_price= round(max_price,2)

####Mean####
mean_price = np.mean(price)
#rounding off to 3dp
mean_price= round(mean_price,3)

##Calculate sample standard deviation
n = len(price)
for num in price:
    deviations = [(num - mean_price) ** 2 for num in price]

std_price = (sum(deviations)/(n-1))**0.5

#rounding off to 4dp
std_price= round(std_price,4)

#Keep all trailing zeros
print('{:.2f}'.format(min_price))
print('{:.2f}'.format(max_price))
print('{:.3f}'.format(mean_price))
print('{:.4f}'.format(std_price))

