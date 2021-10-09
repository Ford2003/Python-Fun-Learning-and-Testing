# Does BMI affect US Medical Insurance Costs?

import csv
import random

data = []
with open('insurance.csv') as df:
    for i in df.readlines():
        data.append([i])
#saving all data rows into 2D list
#print(data)
#random sampling to get random indexes to get from 'data'
samples_bad = []
for i in range(1, 1200, 4):
    samples_bad.append(data[i])

#print(samples_bad)
#print(len(samples_bad))

sample = []
for i in samples_bad:
    sample.append(i[0].split(','))

#print(samples)
samples = []
for i in sample:
    lst = [j.replace('\n', '') for j in i]
    samples.append(lst)
#Separate out the people who lie in each BMI category, in each category, find number of people, mean of costs, highest and lowest cost.
#Find standard deviation of costs to find the spread in order to back-up or disprove mean. then compare these values between each bmi category.

underweight = []
normal = []
overweight = []
obese = []
#Seperating people into BMI categories
for i in samples:
    if float(i[2]) < 18.4:
        underweight.append(i)
    elif float(i[2]) < 24.9 and float(i[2]) >= 18.5:
        normal.append(i)
    elif float(i[2]) < 29.9 and float(i[2]) >= 24.9:
        overweight.append(i)
    else:
        obese.append(i)
#How many people in each category
no_underweight = len(underweight)
no_normal = len(normal)
no_overweight = len(overweight)
no_obese = len(obese)

#function for finding mean of costs
def mean(category):
    total = 0
    for i in category:
        total += float(i[-1])
    return round(total / len(category), 2)

#print(mean(underweight))
#print(mean(normal))
#print(mean(overweight))
#print(mean(obese))

#function for standard deviation of costs. sqrt mean of squares - square of means
def deviation(category):
    squares = 0
    for i in category:
        squares += float(i[-1]) ** 2
    square_mean = mean(category) ** 2
    return round(((squares / len(category)) - square_mean) ** 0.5, 2)

#print(deviation(underweight))
#print(deviation(normal))
#print(deviation(overweight))
#print(deviation(obese))

#function to find highest and lowest
def high_and_low(category):
    highest = 0
    lowest = float('inf')
    for i in category:
        if float(i[-1]) > highest:
            highest = float(i[-1])
        elif float(i[-1]) < lowest:
            lowest = float(i[-1])
    print('Highest cost is ${highest}, and the lowest cost is ${lowest}.'.format(highest=str(round(highest, 2)), lowest=str(round(lowest, 2))))
high_and_low(underweight)
high_and_low(normal)
high_and_low(overweight)
high_and_low(obese)

bmi_ranges = """
BMI RANGES:
 <18.4 Underweight
 18.5 - 24.9 Normal Weight
 25 - 29.9 Overweight
 30< Obese
"""
