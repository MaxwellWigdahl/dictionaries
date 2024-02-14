"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""

import json

infile = open('school_data.json', 'r')

list_of_schools = json.load(infile)

print(type(list_of_schools))

conference_schools = [372, 108, 107, 130]

for school in list_of_schools:
    conference_number = school['NCAA']["NAIA conference number football (IC2020)"]
    if conference_number is not None:
        if int(conference_number) in conference_schools:
            women_graduation = school["Percent of total enrollment that are women (DRVEF2020)"]
            if women_graduation is not None:
                if int(women_graduation) > 50:
                    print(f"University: {school['instnm']}")
                    print(f"Graduation Rate for Women: {women_graduation}")
                    print()

for school in list_of_schools:
    conference_number = school['NCAA']["NAIA conference number football (IC2020)"]
    if conference_number is not None:
        if int(conference_number) in conference_schools:
            off_campus = school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
            if off_campus is not None:
                if int(off_campus) > 50000:
                    print(f"University: {school['instnm']}")
                    print(f"Total Price for in-state students living off campus $ : {off_campus:,.2f}")
                    print()

    
    
        

