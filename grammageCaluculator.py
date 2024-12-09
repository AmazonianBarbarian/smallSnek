# Grammage calculator
# Input Variables to hold measurements
xIn = float(input('width of oject in inches: '))
yIn = float(input('length of oject in inches: '))
g = float(input('how many grams does it weigh?:'))

xM = xIn * 0.0254 # These hold the value in meters
yM = yIn * 0.0254
#note: add error handling later for if results are
#less than zero ""
result = g / (xM * yM)

print(result)