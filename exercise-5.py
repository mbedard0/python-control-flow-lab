# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

n = 0
t = 0
n_q = 1
n_h = 0

while t < 50:
  print(f'term: {t} / number: {n}')
  # n = 0
  # n = 1
  # n = 1
  t += 1
  n_h = n
  #  n_h = 0
  #  n_h = 1
  #  n_h = 1
  n += n_q
  # 0 += 1 -> n = 1
  # 1 += 0 -> n = 1
  # 1 += 1 -> n = 2
  n_q = n_h
  #  n_q = 0
  #  n_q = 1