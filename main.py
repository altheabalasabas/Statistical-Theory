# CURVE FITTING AND LEAST SQUARES
# Compatible with MyCompiler Python

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------
# 1. STRAIGHT LINES
# ---------------------------------------------------

print("1. STRAIGHT LINES")

x1, y1 = 3, -2
x2, y2 = -1, 6

# a. slope
m = (y2 - y1) / (x2 - x1)

# b. equation y = mx + b
b = y1 - m * x1

print("a. Slope =", round(m, 2))
print("b. Equation: y =", round(m, 2), "x +", round(b, 2))

# c. intercepts
# y-intercept = b
y_intercept = b

# x-intercept when y = 0
x_intercept = -b / m

print("c. x-intercept =", round(x_intercept, 2))
print("   y-intercept =", round(y_intercept, 2))

# d. verification
check1 = m * x1 + b
check2 = m * x2 + b

print("d. Verification:")
print("   For (3,-2): y =", round(check1, 2))
print("   For (-1,6): y =", round(check2, 2))


# ---------------------------------------------------
# 2. LEAST SQUARES LINE
# ---------------------------------------------------

print("\n2. LEAST SQUARES LINE")

X = np.array([3, 5, 6, 8, 9, 11])
Y = np.array([2, 3, 4, 6, 5, 8])

n = len(X)

sumX = np.sum(X)
sumY = np.sum(Y)
sumXY = np.sum(X * Y)
sumX2 = np.sum(X ** 2)

print("a.")
print("ΣX =", sumX)
print("ΣY =", sumY)
print("ΣXY =", sumXY)
print("ΣX² =", sumX2)

# regression coefficients
a1 = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX**2)
a0 = (sumY - a1 * sumX) / n

print("\nb. Regression Line:")
print("Y =", round(a0, 2), "+", round(a1, 2), "X")

# predictions
y5 = a0 + a1 * 5
y12 = a0 + a1 * 12

print("\nc. Predicted Y values:")
print("When X = 5, Y =", round(y5, 2))
print("When X = 12, Y =", round(y12, 2))

print("\nd. Interpretation:")
print("For every 1-unit increase in X, Y increases by",
      round(a1, 2), "units on average.")


# ---------------------------------------------------
# 3. REAL-WORLD LEAST SQUARES APPLICATION
# ---------------------------------------------------

print("\n3. REAL-WORLD LEAST SQUARES APPLICATION")

alg = np.array([75, 80, 93, 65, 87, 71, 98, 68, 84, 77])
phy = np.array([82, 78, 86, 72, 91, 80, 95, 72, 89, 74])

# scatter plot
plt.scatter(alg, phy)
plt.xlabel("Algebra Grades")
plt.ylabel("Physics Grades")
plt.title("Algebra vs Physics Grades")
plt.grid(True)
plt.show()

# regression Y on X
m1, b1 = np.polyfit(alg, phy, 1)

print("b. Regression Line (Y on X):")
print("Y =", round(m1, 2), "X +", round(b1, 2))

# prediction when algebra = 75
pred_phy = m1 * 75 + b1

print("\nc. Predicted Physics grade when Algebra = 75:")
print("Predicted Physics Grade =", round(pred_phy, 2))

# regression X on Y
m2, b2 = np.polyfit(phy, alg, 1)

pred_alg = m2 * 95 + b2

print("\nd. Predicted Algebra grade when Physics = 95:")
print("Predicted Algebra Grade =", round(pred_alg, 2))

# correlation
r = np.corrcoef(alg, phy)[0, 1]

print("\ne. Comment:")
print("Correlation coefficient r =", round(r, 2))

if r > 0:
    print("The relationship is positive.")
else:
    print("The relationship is negative.")

if abs(r) > 0.7:
    print("The relationship is strong.")
elif abs(r) > 0.4:
    print("The relationship is moderate.")
else:
    print("The relationship is weak.")


# ---------------------------------------------------
# 4. LEAST SQUARES CURVE
# ---------------------------------------------------

print("\n4. LEAST SQUARES CURVE")

Xc = np.array([0, 1, 2, 3, 4, 5, 6])
Yc = np.array([2.4, 2.1, 3.2, 5.6, 9.3, 14.6, 21.9])

# quadratic fit
coef = np.polyfit(Xc, Yc, 2)

a2 = coef[0]
a1 = coef[1]
a0 = coef[2]

print("a. Quadratic Model:")
print("Y =", round(a0, 2), "+", round(a1, 2),
      "X +", round(a2, 2), "X²")

# predict when X = 7
y7 = a2 * (7**2) + a1 * 7 + a0

print("\nb. Predicted Y when X = 7:")
print("Y =", round(y7, 2))

print("\nc. Description:")
print("The data show an upward curving trend,")
print("so a quadratic model is appropriate.")