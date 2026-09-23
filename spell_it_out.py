word = input("Enter a word: ")

print("\nLetters in word:")
# First loop: Print each letter on its own line
for letter in word:
    print(letter)

print("\nNumbered letters:")
# Second loop: Print numbered letters using enumerate
for index, letter in enumerate(word, start=1):
    print(f"{index}. {letter}")

# Print total letter count
print(f"\nThe word '{word}' has {len(word)} letters.")
