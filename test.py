tolerance = 0.000001
def newton(x):
   estimate = 1.0
   while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
   return estimate

x = float(input ("what is the test number"))
print (newton(x))