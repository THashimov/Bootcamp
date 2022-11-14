abbreviations = {"kg": "Kilogram", "mm": "Millimeter", "mi": "Mile", "kph": "Kilometers per hour"}

abbreviations["mph"] = "Miles per hour"
abbreviations["ms"] = "Meters per second"

user_abbrv = input("Please enter an abbreviation\n")

if user_abbrv.lower() in abbreviations :
    print(f"{user_abbrv} {abbreviations.get(user_abbrv)}")
else :
    print("Abbreviation not found")