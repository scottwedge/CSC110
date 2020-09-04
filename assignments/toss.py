def round_sum(a, b, c):
  return round10(a)+round10(b)+round10(c)

def round10(str(num)):
  if num[-1] >= 5: 
    num[-1] = 0
    num[-2] += 1
  else:
    num[-1] = 0
    num[-2] -= 1
  return num

print(
    round_sum(16, 17, 18),# → 60
    round_sum(12, 13, 14),# → 30
    round_sum(6, 4, 4),# → 10
)