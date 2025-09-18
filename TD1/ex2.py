languages = [ " Python " , " JavaScript " , " SQL " ]

# 1. Append " Java " to the list .
languages.append(" Java ")

# 2. Extend the list with [" HTML " , "CSS "].
languages.extend([" HTML " , " CSS "])

# 3. Sort the list alphabetically .
languages.sort()
print("Sorted languages:", languages)

# 4. Find the index of "SQL ".
sql_index = languages.index(" SQL ")
print(f"Index of 'SQL': {sql_index}")

# 5. Check if "C++" is in the list .
cpp_exists = " C++ " in languages
print(f"Is 'C++' in the list? {cpp_exists}")

# 6. Remove " JavaScript " from the list .
languages.remove(" JavaScript ")
print("Updated languages:", languages)