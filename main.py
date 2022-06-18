import pandas as pd
from other import *

print("hello world!");
displayText();

# titanic = pd.read_csv("titanic.csv")
titanic = pd.read_excel('titanic-data.xlsx')
print(titanic);

num = input("Enter numer : ");
print(num);