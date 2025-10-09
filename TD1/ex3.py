l1 = {" Python ", " SQL ", " Git ", " Docker "}
l2 = {" Python ", " HTML ", " CSS ", " Git "}

# 1. Add " JavaScript " to candidate1 ’s skills .
l1.add(" JavaScript ")
print("Candidate skills ", l1)

# 2. Find the union of both skill sets .
y = l1 | l2
print("Union of skills:", y)

# 3. Find the intersection ( common skills ).
intersection = l1 & l2
print("Intersection of skills:", intersection)

# 4. Find the difference ( skills only candidate1 has).
difference = l1 - l2
print("Skills only candidate 1 has:", difference)

# 5. Discard " Docker " from candidate1 ’s skills ( safely ).
l1.discard(" Docker ")
print("Candidate 1 skills after discarding Docker:", l1)
