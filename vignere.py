def vignere(txt, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ""
    j = 0
    txt = txt.upper()
    key = key.upper()

    for i in range(len(txt)):
        if txt[i] == " ":
            encrypted += " "    
        else :
            indice1 = alphabet.find(txt[i])
            #if indice1 == -1:  # Si le caractère n'est pas dans l'alphabet
                #encrypted += txt[i]
                #continue

            indice2 = alphabet.find(key[j])
            sum_indices = indice1 + indice2
            
            if sum_indices >=26:
                sum_indices -= 26

            encrypted += alphabet[sum_indices]
            
            #check j manually for key rotation
            j += 1 
            if j>= len(key):
                j = 0
#j = (j + 1) % len(key)  # Avance dans la clé et la réinitialise si nécessaire

    return encrypted

print('Using : \"la rencontre est prevue 6 la cafeteria as a text for testing."')
print("And 'Poule' as a Key!")
print(vignere("larencontreestprevuealacafeteria","poule"))
