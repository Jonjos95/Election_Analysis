print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
    counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
       
for county in counties:
     print(county)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}    
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for county, voters in counties_dict.items():
    print(county, voters)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)



