
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

quantity_boy = len(boys)
quantity_girls = len(girls)
#print(f"мальчиков {quantity_boy}")
#print(f"девочек {quantity_girls}")
if quantity_boy > quantity_girls:
    print(f"{quantity_boy - quantity_girls} мальчика остануться без пары")
elif quantity_boy < quantity_girls:
    print(f"{quantity_girls-quantity_boy} девочки остануться без пары")
else:
    boys_sorted= sorted(boys)
    girls_sorted= sorted(girls)
    print(f"Идеальные пары:")
    for pair in zip(boys_sorted, girls_sorted):
        print(f"{pair[0]} и {pair[1]}")
