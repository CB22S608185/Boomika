#leap year

def isleapyear(year):
  if(year%4==0 and year%100 !=0) or year%400 == 0:
    return True
  else:
    return False

year=int(input("Enter a value:"))

if isleapyear(year):
  print('{} is a leap year. '. format(year))
else:
  print('{} is not aleap year year. '.format(year))