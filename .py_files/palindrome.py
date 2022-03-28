class MyPal:
  def __call__(self, str1):
	# Run loop from 0 to len/2
    str = ''
    for i in range(0, len(str1)):
      c = str1[i].upper()
      if c>= 'A' and c <= 'Z':
        str += c                                  
    for i in range(0, int(len(str)/2)):
      if str[i] != str[len(str)-i-1]:
        return False
    return True

# main function
# def myPalTest():
#   #s = "malayalam"
#   # s = "asdfjlh 49786*&A"
#   mypal = MyPal()
#   ans = mypal(s)
#   if (ans):
#     print(s, "is a palindrome")
#   else:
#     print(s, "is not a palindrome")

def test():
  testData = ["foobar", "A man, a plan, a canal -- Panama!", "apsdfoi", "asddsa", "iTopiNonAvevanoNipoti", "Alabaster Night", "iGattiNonAvevanoCugini", "redivider", "Borrow or rob?", "Able was I ere I saw Elba" ]
  for stuff in testData:
    mypal = MyPal()
    ans = mypal(stuff)
    if (ans):
      print(stuff, "is a palindrome")
    else:
      print(stuff, "is not a palindrome")
  
# tester method
# put string into method
