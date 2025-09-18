students = {
" Alice " : 85 ,
" Bob " : 92 ,
" Charlie " : 78 ,
" Diana " : 88
}

# 1. Retrieve the score for " Charlie " using get ().
x = students.get(" Charlie ")
print(f" Charlie 's score: {x}")

# 2. Try to retrieve a score for "Eve" using get () with a default of 0.
y = students.get(" Eve ", 0)
print(f" Eve 's score: {y}")

# 3. Remove "Bob" from the dictionary using pop ().
z = students.pop(" Bob ", None)
print(f" Removed Bob 's score: {z}")

# 4. Print all student names using keys ().
for i in students.keys():
    print(i)

# 5. Print all scores using values ().
  
for i in students.values():
    print(i)

# 6. Print all (name , score ) pairs using items ().    
print("Student scores:")
for n, s in students.items():
    print(f"{n}: {s}")