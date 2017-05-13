# You are given the scores of N students in three different subjects - 
# Mathematics,*Physics* and Chemistry; all of which have been graded 
# on a scale of 0 to 100. Your task is to compute the Pearson 
# product-moment correlation coefficient between the scores of different 
# pairs of subjects (Mathematics and Physics, Physics and Chemistry, 
# Mathematics and Chemistry) based on this data. This data is based on 
# the records of the CBSE K-12 Examination - a national school leaving 
# examination in India, for the year 2013.

# Link: https://www.hackerrank.com/challenges/computing-the-correlation
# Reference: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
# Developer: Murillo Grubler

# Import library
import math as m

# Define functions
def mean(data):
    return sum(data) / len(data)

def var(data):
    sum = 0
    for i in range(len(data)):
        sum = sum + (data[i] - mean(data)) ** 2
    return sum

def cov(dt1, dt2):
    sum = 0
    for i in range(len(dt1)):
        sum += (dt1[i] - mean(dt1)) * (dt2[i] - mean(dt2))
    return sum

# Set data
total = int(input())
mathematics = []
physics     = []
chemistry   = []
for i in range(total):
    elements = list(map(float, input().split()))
    mathematics.append(elements[0])
    physics.append(elements[1])
    chemistry.append(elements[2])

# Get mean
mean_mathematics    = mean(mathematics)
mean_physics        = mean(physics)
mean_chemistry      = mean(chemistry)

# Get variance
var_mathematics = var(mathematics)
var_physics     = var(physics)
var_chemistry   = var(chemistry)

# Get Correlation between Mathematics and Physics
cov_math_phys   = cov(mathematics, physics)
std_math_phys   = m.sqrt(var_mathematics * var_physics)
r_math_phys     = cov_math_phys / std_math_phys
print (round(r_math_phys,2))

# Get Correlation between Physics and Chemistry
cov_phys_chem   = cov(physics, chemistry)
std_phys_chem   = m.sqrt(var_physics * var_chemistry)
r_phys_chem     = cov_phys_chem / std_phys_chem
print (round(r_phys_chem,2))

# Get Correlation between Chemistry and Mathematics
cov_chem_math   = cov(chemistry, mathematics)
std_chem_math   = m.sqrt(var_chemistry * var_mathematics)
r_chem_math     = cov_chem_math / std_chem_math
print (round(r_chem_math,2))