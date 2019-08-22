def solution(roman):
  """complete the solution by transforming the roman numeral into an integer"""
  d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  count = 0
  for i in range(len(roman) - 1):
      num = d[roman[i]]
      if num < d[roman[i+1]]:
          count -= d[roman[i]]
      else:
          count += d[roman[i]]
  return count + d[roman[-1]]
