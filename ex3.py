skills_candidate1 = { " Python " , " SQL " , " Git " , " Docker " }
skills_candidate2 = { " Python " , " HTML " , " CSS " , " Git " }

# 1. Add " JavaScript " to candidate1 ’s skills .
skills_candidate1.add(" JavaScript ")
print("Candidate 1 skills after adding JavaScript:", skills_candidate1)

# 2. Find the union of both skill sets .
union_skills = skills_candidate1 | skills_candidate2
print("Union of skills:", union_skills)

# 3. Find the intersection ( common skills ).
intersection_skills = skills_candidate1 & skills_candidate2
print("Intersection of skills:", intersection_skills)

# 4. Find the difference ( skills only candidate1 has).
difference_skills = skills_candidate1 - skills_candidate2
print("Skills only candidate 1 has:", difference_skills)

# 5. Discard " Docker " from candidate1 ’s skills ( safely ).
skills_candidate1.discard(" Docker ")
print("Candidate 1 skills after discarding Docker:", skills_candidate1)
