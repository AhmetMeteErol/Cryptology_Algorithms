from math import ceil

original_text = input("Enter the message which is going to encode: ")

# Edit Section
original_text = original_text.replace(' ','')
original_text = original_text.replace(',','')
original_text = original_text.replace('.','')
original_text = original_text.replace('?','')
original_text = original_text.replace('-','')
original_text = original_text.lower()
original_text = list(original_text)


# Encoding Section
N = len(original_text)
indice_of_matrice = ceil(N**.5)

lines = []

encoded_message = ''

for i in range(((indice_of_matrice * indice_of_matrice) - (len(original_text)))):
    original_text.append(' ')

for j in range(indice_of_matrice):
    lines.append(''.join(original_text[(j*indice_of_matrice):(i * indice_of_matrice) + indice_of_matrice]))

for k in range(indice_of_matrice):

    for l in range(len(lines)):
        encoded_message = encoded_message + str(lines[l][k])

print(encoded_message)
