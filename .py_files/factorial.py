class MyFactorial:
  def __call__(self, n):
    if n == 1 or n == 0:
      return 1
    else:
      return n * self(n-1)


# def test_factorial():
#   # this would create an instance of the MyFactorial class - Christina Lee
#   fac = MyFactorial()
#   print(fac(3))

# make a def tester - Christina Lee
def testF():
  factData = [3,1,4,9,3,11,14,5,20,]
  for facts in factData:
    # mypal = MyPal()
    fac = MyFactorial()
    print(facts,"! = ", fac(facts))
