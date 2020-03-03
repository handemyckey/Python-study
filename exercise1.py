composers = {'Johann':65,'Ludwig':56,'Frederic':39,'Wolfgang':35}
print(composers.items())
#Function 1
def sort_dict_by_value(d):
    d = {k: v
        for k,v in sorted(d.items(),key=lambda el:el)
    }
    print("\n")
    print(d)
sort_dict_by_value(composers)

#Function 2
def sort_dict(d):
    print("\n")
    print(dict(sorted(d.items(),key=lambda el:el[1])))
sort_dict(composers)
