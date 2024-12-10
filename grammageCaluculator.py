# Grammage calculator, Authot: Astird La Reine Lockhart
# Input Variables to hold measurements
xIn = float(input('width of oject in inches: '))
yIn = float(input('length of oject in inches: '))
g = float(input('how many grams does it weigh?: '))
basisInput = input('Select paper type(1: Copy, 2: Cardstock): ')

xM = xIn * 0.0254 # These hold the value in meters
yM = yIn * 0.0254
#note: add error handling later for if results are
#less than zero ""

result = g / (xM * yM)

match basisInput: #I used this to easily select options and pick the proper calculation for the paper type.
    case "1":
        basisResult = (result * (25 * 38)) / 1406.5 
      #calculation produces wrong results but case switch statement still works.
    case "2":
        basisResult = (result * (8.5 * 11)) / 1406.5

print("Grammage: {" + str(result) + " g/m^2}")
print("Basis Weight: {" + str(basisResult) + " lbs}")
