import pandas as pd
import pathlib as pb
import matplotlib.pyplot as plit

#This is a project by the beautiful ben, hilarious hilary, magical mahi, and exciting emily

fastfashion_df = pd.read_csv("fastfashion.csv")

#Ask the user which info they would like to see
user_input = input("Would you like to see carbon emissions over time from fast fashion companies, monthly production in tonnes over time from countries, annual waste in tonnes from countries, or the monthly average worker wage? Enter carbon emissions, monthly production, annual waste, or average worker wage: ").lower()

#Cleaning Data (Removing columns that are not needed)
fastfashion_df.drop(['Release_Cycles_Per_Year', 'Transparency_Index', 'Instagram_Mentions_Thousands', 'TikTok_Mentions_Thousands', 'Sentiment_Score', 'Social_Sentiment_Label', 'Compliance_Score', 'Env_Cost_Index','Shopping_Frequency_Per_Year'], inplace=True, axis = 1)

#Which year had the greatest carbon emissions?

carbon_dict = {} #Create an empty dictionary that will store years, its total carbon emissions, and a counter
for index, row in fastfashion_df.iterrows():
#If the year already exists in the dictionary, add to the total carbon emissions as the zeroth value in the list 
#and add 1 to the counter to show that its appeared another time
    if row['Year'] in carbon_dict:
        carbon_dict[row['Year']][0] += float(row['Carbon_Emissions_tCO2e'])
        carbon_dict[row['Year']][1] += 1
#If the year doesn't exist in the dictionary, create a new key and a list 
#of two values with carbon emissions and a counter
    else:
        carbon_dict[row['Year']] = [float(row['Carbon_Emissions_tCO2e']), 1]
sorted_list = sorted(carbon_dict.items())
sorted_dict = dict(sorted_list)
carbon_emissions = []
for key,value in sorted_dict.items():
    value = sorted_dict[key][0] / sorted_dict[key][1] #Divide total carbon emissions per year by the counter
    carbon_emissions.append(value)

# Line plot showing carbon emission over the years
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

if user_input == "carbon emissions": 
    plit.plot(years, carbon_emissions, color = "#28a225")  
    plit.title("Average Yearly Carbon Emissions from Fast Fashion Companies")    
    plit.xlabel("Years")
    plit.ylabel("Carbon Emissions (Tonnes)")
    plit.show()
  
    
#On average, which country had the greatest average monthly textile production in tonnes

#Count number of countries
total_countries = {}
count_countries = {}
monthly_production = []
for index, row in fastfashion_df.iterrows():
   if row['Country'] in total_countries:
       total_countries[row['Country']] += int(row['Monthly_Production_Tonnes'])
       count_countries[row['Country']] += 1
   else:
       total_countries[row['Country']] = int(row['Monthly_Production_Tonnes'])
       count_countries[row['Country']] = 1
for key,value in total_countries.items():
#Divide total monthly production by counter to find average
    production = total_countries[key] / count_countries[key]
    monthly_production.append(production) 
    
#Bar graph showing average monthly production in each country
countries = ['Indonesia', 'Vietnam', 'India', 'USA', 'Turkey', 'Brazil', 'Bangladesh', 'China', 'Germany', 'UK']
my_colors = ['#BAFFCA',"#452FB0", "#C132AC","#2A803E","#978ADB", "#32A4C1", "#FF4848","#1A6E46", "#F7FF1B", "#FF005D","#FFA527", "#165462"]
if user_input == "monthly production":
    print(monthly_production)
    plit.bar(countries, monthly_production, color = my_colors)
    plit.title("Average Monthly Textile Production in Countries")
    plit.xlabel("Countries")
    plit.ylabel("Average Monthly Production (Tonnes)")
    plit.ylim(485, 505)
    plit.show()

#On average (relative to number of fast fashion companies), what is the average annual waste directed to landfills in tonnes

total_countries = {}
count_countries = {}
annual_waste = []
for index, row in fastfashion_df.iterrows():
   if row['Country'] in total_countries:
       total_countries[row['Country']] += int(row['Landfill_Waste_Tonnes'])
       count_countries[row['Country']] += 1
   else:
       total_countries[row['Country']] = int(row['Landfill_Waste_Tonnes'])
       count_countries[row['Country']] = 1
for key,value in total_countries.items():
    waste = total_countries[key] / count_countries[key] #Divide total annual waste by counter to find average  
    annual_waste.append(waste) 


#Bar graph showing average annual waste to landfills in each country
countries = ['Indonesia', 'Vietnam', 'India', 'USA', 'Turkey', 'Brazil', 'Bangladesh', 'China', 'Germany', 'UK']

if user_input == "annual waste":
    print(annual_waste)
    plit.bar(countries, monthly_production, color = my_colors)
    plit.title("Average Annual Waste to Landfills in Countries")
    plit.xlabel("Countries")
    plit.ylabel("Average Anuual Waste (Tonnes)")
    plit.ylim(485, 505)
    plit.show()
if user_input != 'annual waste' and user_input != 'monthly production' and user_input != 'carbon emissions' and user_input != 'average worker wage': 
    print("Please enter monthly production, carbon emissions, annual waste, or average worker wage:")

#Which brand has the lowest average worker wage?
total_brands = {}
count_brands = {}
average_wage = []
for index, row in fastfashion_df.iterrows():
   if row['Brand'] in total_countries:
       total_brands[row['Brand']] += int(row['Avg_Worker_Wage_USD'])
       count_brands[row['Brand']] += 1
   else:
       total_brands[row['Brand']] = int(row['Avg_Worker_Wage_USD'])
       count_brands[row['Brand']] = 1
for key,value in total_brands.items():
    wage = total_brands[key] / count_brands[key] #Divide total wage by counter to find average  
    average_wage.append(wage) 

#Bar Graph showing average worker age in each brand
brands = ['Shein', 'Forever 21', 'Uniqlo', 'Zara', 'H&M']
if user_input == "average worker wage":
    plit.bar(brands, average_wage, color = my_colors)
    plit.title("Average Worker Wage per Brand")
    plit.xlabel("Brands")
    plit.ylabel("Average Worker Wage (USD)")
    plit.ylim(90, 250)
    plit.show()