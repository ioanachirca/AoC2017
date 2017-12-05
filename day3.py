import sys
x = input("Enter a number: ")

# first determine the number of the ring x is in
k = 1
while x > pow((2 * k + 1), 2):
	k += 1

# midpoint values of the square edges
mid_bottom_val = pow((2 * k + 1), 2) - k
mid_left_val = pow((2 * k + 1), 2) - 3 * k
mid_up_val = pow((2 * k + 1), 2) - 5 * k
mid_right_val = pow((2 * k + 1), 2) - 7 * k

# need to determine closest midpoint
dist = sys.maxint
if (abs(x - mid_bottom_val)) < dist:
	dist = abs(x - mid_bottom_val)
if (abs(x - mid_left_val)) < dist:
	dist = abs(x - mid_left_val)
if (abs(x - mid_up_val)) < dist:
	dist = abs(x - mid_up_val)
if (abs(x - mid_right_val)) < dist:
	dist = abs(x - mid_right_val)

print (dist + k)



