class MyMath:
  def findFactors(self, number):
    print("OOPFactors of a Given Number {0} are:".format(number))
    for value in range(1, number + 1):
      if number % value == 0:
        print("{0}".format(value), end=" ")
    print()

def factors():
  print("hello from factors")
  num = int(input("Enter any Number to find its factors: "))
  findFactors(num)
  mat = MyMath()
  mat.findFactors(num)
  

def findFactors(number):
  print("ImpFactors of a Given Number {0} are:".format(number))
  for value in range(1, number + 1):
    if number % value == 0:
      print("{0}".format(value), end=" ")
  print()
