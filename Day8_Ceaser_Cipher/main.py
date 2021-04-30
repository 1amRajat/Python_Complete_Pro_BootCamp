from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def list_to_str(list_input):
    op_str = ''
    for item in list_input:
        op_str += item
    return op_str


def action_taken(action, user_input, shift_num):
    output = []
    if action.lower() == 'encode':
        for item in user_input.lower():
            if item in alphabet:
                position = 0
                position = alphabet.index(item)
                position = position + shift_num
                output.append(alphabet[position])
        print(f"Encoded output is: {list_to_str(output)}")
    elif action.lower() == 'decode':
        for item in user_input.lower():
            if item in alphabet:
                position = 26
                position = position + alphabet.index(item)
                position = position - shift_num
                output.append(alphabet[position])
        print(f"Decoded output is: {list_to_str(output)}")
    else:
        print("Please provide a correct input!")


print(logo)

terminate = False

while not terminate:
    action = input("Type 'encode' to encrypt or 'decode' to decrypt: \n")
    user_input = input("Type your message: \n")
    shift_num = int(input("Type the shift number: \n"))
    action_taken(action, user_input, shift_num)

    indicator = input("Print 'Yes' to continue, 'No' to end the program \n")
    if indicator.lower() == 'no':
        terminate = True
        print("Thanks for using, Goodbye!")
