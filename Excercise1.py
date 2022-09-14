val1 = int(input("Enter the first value: "))
val2 = int(input("Enter the second value: "))


add = val1+val2
sub = val1-val2
mul = val1*val2
div = val1/val2
pwr = val1**val2

print('Addition: '+ str(add))
print('Subraction: '+ str(sub))
print('Multiplication: '+ str(mul))
print('Division: '+ str(div))
print('Power: '+ str(pwr))

# Modified by Jai

val3 = int(input("Enter the third value: "))

add += val3
sub -= val3
mul *= val3
div /= val3
pwr **= val3

print('New Addition: '+ str(add))
print('New Subraction: '+ str(sub))
print('New Multiplication: '+ str(mul))
print('New Division: '+ str(div))
print('New Power: '+ str(pwr))
