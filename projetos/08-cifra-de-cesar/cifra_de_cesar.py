import arte

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Imprimir a arte
print(arte.arte)

# Criptografar ou descriptografar o texto recebido
def caesar(original_text, shift_amount, action):
    output_text = ""
    
    # Ajustar as variáveis de acordo com a ação a ser realizada
    if action == "encode":
        index_limit = -26
    if action == "decode":
        index_limit = 26
        shift_amount *= -1
    
    for letter in original_text:
        try:
            if letter not in alphabet:
                output_text += letter
            else:
                output_text += alphabet[alphabet.index(letter) + shift_amount]
        except IndexError:
            output_text += alphabet[alphabet.index(letter) + shift_amount + index_limit]
        
    print(f"Here is the {action}d result: {output_text}")

while True:
    # Receber a entrada do usuário
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, action=direction)
    
    restart = input('Type "yes" if you want to go again. Otherwise type "no".\n').lower()
    
    if restart == "no":
        print("Thank you for using the Caeser Cypher. Goodbye.")
        break
