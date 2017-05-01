# Charlie wants to purchase office-space. He does a detailed survey of the 
# offices and corporate complexes in the area, and tries to quantify a lot 
# of factors, such as the distance of the offices from residential and 
# other commercial areas, schools and workplaces; the reputation of the 
# construction companies and builders involved in constructing the apartments; 
# the distance of the offices from highways, freeways and important roads; 
# the facilities around the office space and so on.


# Link: https://www.hackerrank.com/challenges/predicting-office-space-price
# Reference: http://onlinestatbook.com/2/regression/intro.html
# Developer: Murillo Grubler

# Import library
from sklearn import linear_model

# Set data
features, rows = map(int, input().split())
X, Y = [], []

# Get the parameters X and Y for discovery the variables a and b
for i in range(rows):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < features:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)

# Set the model LinearRegression
model = linear_model.LinearRegression()
model.fit(X, Y)
a = model.intercept_
b = model.coef_

# Get the parameters X for discovery the Y
new_rows = int(input())
new_X = []
for i in range(new_rows):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        x.append(elements[j])
    new_X.append(x)

# Gets the result and show on the screen
result = model.predict(new_X)
for i in range(len(result)):
    print(round(result[i],2))