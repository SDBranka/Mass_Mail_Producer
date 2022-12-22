#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

PLACEHOLDER = "[name]"


with open("Input/Letters/starting_letter.txt") as file:
    ex_letter = file.read()

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

# console test statement
# print(names)

# for each name in names replace PLACEHOLDER with name
for name in names:
    new_letter = ex_letter.replace(PLACEHOLDER, name.strip())
    # console test statement
    # print(new_letter)
    
    with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as completed_letter:
        completed_letter.write(new_letter)