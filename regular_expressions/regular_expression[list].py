import re
text = """Afghanistan, America, Bangladesh, India, London, Pakistan, Maldives, Nepal, England, 
Poland, Finland, Chad, Netherlands, Denmark, NewZealand, Canada, Iceland, Sweden, Greenland"""
print("text <type 'str'> = ", text)
# countries = text.split(",")
# print("")
# print("countries <type 'list'> = ", countries)
match = re.findall("(\w+lands*)", text)  # land/lands finder with regular expression
print("")
print(match)




