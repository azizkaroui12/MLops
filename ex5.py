undo_stack = []

# 1. Push actions : " Type ’Hello ’" , " Bold " , " Delete ’o ’" , " Undo, Bold "
undo_stack.append(" Type ’Hello ’")
undo_stack.append(" Bold ")
undo_stack.append(" Delete ’o ’")
undo_stack.append(" Undo, Bold ")

# 2. Pop the last action .
undo_stack.pop()

# 3. View the current top action .
if undo_stack:
    print("Current top action:", undo_stack[-1])
else:
    print("Undo stack is empty.")

# 4. Print the stack state .
print("Current undo stack:", undo_stack)
