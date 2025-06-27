
#ex:
country_capitals = {
  "India": 'Delhi',
  "Canada": 'Ottawa',
  "England": 'London'
}
#add new country
country_capitals["Austraila"]='canberra'
country_capitals["uk"]='london'
#modify country_capitals
country_capitals["Austraila"]='sydney'



print (country_capitals["India"])
print(country_capitals["Canada"])
print(country_capitals["England"])
print(country_capitals["Austraila"])
print(country_capitals["uk"])
#ex

state_capitals={
    "Tamilnadu":'Chennai',
    "Andhra Pradesh":'Amaravathi',
    "Telengana":'Hyderabad',
    }
print(state_capitals)

#ex
Employee1={
    "ID":1,
    "name":'sabeer'
    }
Employee2={
    "ID":2,
    "name":'surya'
}
Employees=[]
Employees.append(Employee1)
Employees.append(Employee2)
print(Employees)

#ex
Car_name={
    "Toyota":'Innova',
    "suzuki":'dzier',
    "Mahindra":'Thar',
    "Tata":'safari'
}
#add new car
Car_name["Ford"]="Endeavour"
#modify tata  car model
Car_name["Tata"]="Harrier"
#del car
Car_name["suzuki"]

print(Car_name['Toyota'])
print(Car_name['suzuki'])
print(Car_name['Mahindra'])
print(Car_name['Tata'])
print(Car_name['Ford'])


#ex
Bike_Showroom={
    "TVS":'starcity',
    "KTM":'Duke',
    "RoyalEnfield":'Classic350',
    "Honda":'shine'

}
print(Bike_Showroom)
