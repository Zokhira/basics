rivers = {'nile': 'Egypt', 'tigres': 'Iraq', 'amazon': 'Brazil', 'mississippi': 'Usa'}
for river, country in rivers.items():    #or key for values
    print(f"The {river.title()} runs through {country.title()}. ")