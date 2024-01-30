def p():
    print("What do you want to see")
    print('''    1 for Sunrise
    2 for sunset
    3 for moonrise
    4 for moonset
    5 for current time
    6 for solar noon
    7 for daylength
    8 for longitude
    9 for latitude''')
def main(x):
    if x==1:print(imp["sunrise"])
    elif x==2:print(imp["sunset"])
    elif x==3:print(imp["moonrise"])
    elif x==4:print(imp["moonset"])
    elif x==5:print(imp['current_time'])
    elif x==6:print(imp["solar_noon"])
    elif x==7:print(imp["day_length"])
    elif x==8:print(imp["location"]["longitude"])
    elif x==9:print(imp["location"]["latitude"])
# a='https://api.ipgeolocation.io/timezone?apiKey=&tz=America/'
import requests
b='8b9283e832064d979613c632e78a5248'
d=input("enter the country")
c=input("Enter the City")
# e=input("enter language English (en),German (de),Russian (ru),Japanese (ja),French (fr),Chinese Simplified (cn),Spanish (es),Czech (cs),Italian (it) Default is english if entered sometheing else then it would be considered as english ")
api=requests.get(f'https://api.ipgeolocation.io/astronomy?apiKey={b}&location={c},%20{d}&lang=en')
print("Welcome")
if api.status_code==200:
    imp=api.json()
    op=dict(imp)
    print(type(imp))
    p()
    x=int(input("Enter Choice"))
    with open('bonus.txt','w') as file:
            file.write(str(op)+'\n')
    main(x)
    
else:
    print(api.json())
choice=input("Want to see any thing above on a specific date y/n")
if choice=="y":
    date=input("enter the date in format YYYY-MM-DD")
    api=requests.get(f'https://api.ipgeolocation.io/astronomy?apiKey={b}&location={c},%20{d}&date={date}')
    if api.status_code==200:
        p()
        imp=api.json()
        x=int(input("Enter Choice"))
        main(x)
        with open('bonus.txt','a') as file:
            file.write(str(imp)+'\n')
    else:
        print(api.json())

