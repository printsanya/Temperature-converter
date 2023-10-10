print("enter the type of conversion   1.celcuis to fahrenheit   2.fahrenheit to celcius")
num=int(input("enter"))
if num==1:
    temp=float(input("enter temp in celcius"))
    f=(temp*1.8)+32
    print(f"{temp:.2f} degree celcius is equal to {f:.2f} degree fahrenheit") 
if num==2:
    temp=float(input("enter temp in fahrenheit"))
    c=5/9*(temp-32)
    print(f"{temp:.2f} degree fahrenheit is equal to {c:.2f} degree celcius") 