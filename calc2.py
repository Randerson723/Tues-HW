def circum(r):
    return r*2*3.14
print("""Circumference Calculator.
Enter 'r' to calculate circumference.
It will calculate circumference."""
      )

r = float(input("enter the radius:"))
circum(r*3.142*2)
print(circum(r))
