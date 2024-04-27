#set = collection which is unorderd, unindexed. No duplicate values:


utensils = {"fork", "sppon", "knife"}
dishes = {"bowl", "plate", "cup"}
dinner_table = utensils.union(dishes)
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)

# print(utensils.difference(dishes))
print(utensils.intersection(dishes))

#for x in utensils:
#    print(x)
