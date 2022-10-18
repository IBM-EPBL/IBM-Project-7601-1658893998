import requests
import random
from time import *
gate=True
def run_city():
  city = input('input the city name')
  print(city)
  print('Displaying Weater report for: ' + city)
  url = 'https://wttr.in/{}'.format(city)
  res = requests.get(url)
  print(res.text)
while(gate):
    temperature = random.randint(0,50)
    humidity = random.randint(10,50)
    if temperature>45 and humidity<50:
        print("Temperature =",temperature,"Humidity =",humidity)
        print("Alert message in Activate")
        gate=False
    else:
        print("Temperature =",temperature,"Humidity",humidity)
    sleep(1);
x= int(input("Enter the Humidity value :"))
y= int(input("Enter the temperature value  :"))
z=print(x,y)
print(z)
if x == 36.5:
    print("Due to Temperature report you are in normal days")
if x < 36:
        print("your Temperature is low compare to normal days")
if x > 36:
            print("your Temperature is high compare to normal days")
if y == 45:
    print("Due to Humidity report you are in normal place")
if y < 45:
        print("your Humidity is low compare to normal days")
if y > 45:
            print("your Humidity is high compare to normal days")
while True:
    run_city()