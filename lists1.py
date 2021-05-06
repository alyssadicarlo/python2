family_members = []
family_members.append("Alyssa")
family_members.append("Gina")
family_members.append("Van")
family_members.append("Rita")

print(len(family_members))

index = 0
# WHILE loop
print("------WHILE LOOP------")
while index < len(family_members):
    print(family_members[index])
    index = index + 1

# FOR loop
print("------FOR LOOP------")
for member in family_members:
    print(member)