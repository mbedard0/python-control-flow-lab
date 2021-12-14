# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print('Enter the lengths of three side of a triangle:')
side_a = input('a:')
side_b = input('b:')
side_c = input('c:')

if side_a == side_b and side_b == side_c:
  print(f'A triangle with sides of {side_a}, {side_b} & {side_c} is a equilateral triangle')

if side_a != side_b and side_b != side_c:
  print(f'A triangle with sides of {side_a}, {side_b} & {side_c} is a scalene triangle')

if side_a == side_c and side_b != side_c or side_a == side_b and side_a != side_c or side_c == side_b and side_c != side_a:
  print(f'A triangle with sides of {side_a}, {side_b} & {side_c} is a isosceles triangle')