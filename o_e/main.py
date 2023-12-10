def o_e():
  numbers = input("Enter your comma-seperated numbers: ").replace(" ", "").split(",")
  print(numbers)
  o_e_string = ""
  for num in numbers:
    if num.isdigit():
      if int(num) % 2 == 0:
        o_e_string += "e"
      else:
        o_e_string += "o"
  return o_e_string