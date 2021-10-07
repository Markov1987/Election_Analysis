#Printing

print("Hello World")

#Variables
type(3)
ballots=1,341
ballots
type(ballots)

#Integer
num_candidate=3

#Float
Winning_Percentage=73.81

#String
candidate="Diana"

#Boolean
won_election=True

#Words that can't be used as variables' names
help("keywords")

5 + (9 * 3 / 2 - 4)
5 + (9 * 3 / (2 - 4))

#Lists

counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties[-2])
len(counties)

#To add items to an empty list we need to declare it first
my_list=[]

#Get sublist

counties[0:2]
#Add items at the end of a list

counties.append("El Salto")

#Add item at an specific place

counties.insert(2,"El Paso")

#Remove items

counties.remove("El Paso")
counties.pop(3)

#Change Elements of a list

counties[2]="El Paso"
print(counties)

#Tuples are like lists but inmutable

my_tuple=()

counties_tuple=("Arapahoe","Denver","Jefferson")
# we can use the same len, indexing, and slicing such as in list using []

# Dictionaries 

My_Dictionary={}
my_dictionary=dict()

counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict

len(counties_dict) #Longitud
counties_dict.keys() #Obtiene keys
counties_dict.values() #Obtiene valores
counties_dict.get("Denver") #Get specific value


#List [] of dictionaries {}

voting_data=[]

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

len(voting_data)
#En las listas de diccionarios se puede usar apprend(), insert() y remove()

voting_data.insert(2,{"El Paso:461149"}) 
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data


#Create algorithm that crea calculates percentages of votes a candidate receive.
#Includes Input and computations

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")



#For
x=1
y=10

if x==1:
    print("x is equarl to 1")

if !=1:
    print("y is not equal to 1")

if x<y:
    print("x is less than y")

if x>=y:
    print("x is greater or equal to y")

if x==1 or y==10:
    print("Both are equal")


if x<10:
    if y<5:
        print("x is less than 10 and y is less than 5")
    

#Loop

for x in range(5):
    print(x)

for x in range(2,7):
    print(x)

