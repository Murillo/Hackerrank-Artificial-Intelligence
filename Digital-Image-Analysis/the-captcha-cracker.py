# You are provided a set of twenty-five captchas, such that, 
# each of the characters A-Z and 0-9 occur at least once in one 
# of the Captchas' text. From these captchas, you can identify 
# texture, nature of the font, spacing of the font, morphological 
# characteristics of the letters and numerals, etc. 

# Link: https://www.hackerrank.com/challenges/digital-camera-day-or-night
# Developer: Murillo Grubler

# Import libraries
from sklearn.linear_model import LogisticRegression

# Define functions
def readData(directory_name):
    return []

def trainData(data):
    return []

# Read the captchas
data = readData(directory)

# Separate data for training
train =  trainData(data)

# Create the classifier model
clf = LogisticRegression()
clf.fit(train[0], train[1])

# Set new captcha
captcha = input().split(" ")

# Predict new captcha
print(clf.predict(captcha))