def to_celsius(f):
  return (f - 32) * (5 / 9)

def to_farenheit(c):
  return c * (9/5) + 32

def convert_temp(unit_in, unit_out, temp):
    if(unit_in.lower() != 'c' and unit_in.lower() != 'f'):
      return f"Invalid unit {unit_in}"
    if(unit_out.lower() != 'c' and unit_out.lower() != 'f'):
      return f"Invalid unit {unit_out}"

    if(unit_in.lower() == 'c'):
      if(unit_out.lower() == 'c'):
        return temp
      return to_farenheit(temp)
    else: 
      if(unit_out.lower() == 'f'):
        return temp
      return to_celsius(temp)


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

