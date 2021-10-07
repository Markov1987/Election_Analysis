

#If Statements 

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])


#If Else Statement

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")    


#Nested If Else 

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')


#Membership operators
counties = ["Arapahoe","Denver","Jefferson"]

if "Arapahoe" in counties: 
    print("True") 
else: 
    print("False")

if "El Paso" not in counties: 
    print("True") 
else: 
    print("False")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#Logical

x = 5
y = 5
if x == 5 and y == 5:
    print("True") 
else:
    print("False")

x = 5
y = 5
if not(x > y):
    print("True")
else:
    print("False")

#Combine

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")



if "Arapahoe" in counties and "El Paso" not in counties:
       print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")


#Repetition Statements

x = 0
while x <= 5:
    print(x)
    x = x + 1

counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])


#Interate through a Dictionary

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#Get keys from Dictionary
for county in counties_dict.keys():
    print(county)

for county in counties_dict:
    print(county)


#Get values from Dictionary
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

#Get both keys and values

for key, values in counties_dict.items():
    print(key, values)

#Get Each Dictionary in a List of Dictionaries

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

#Nested For
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#Print Values
for county_dict in voting_data:
         print(county_dict['registered_voters'])

#Print keys
for county_dict in voting_data:
    print(county_dict['county'])


#Formatting with F Strings

#ORIGINAL
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#SIMPLIFIED WITH F STRING
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")


#USE F STRING WITH DICTIONARIES

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")



candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2F}% of the total votes.")

print(message_to_candidate)