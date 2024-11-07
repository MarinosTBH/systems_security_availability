def kasiski_examination(ciphertext):
    """
    Identify repeating sequences in the ciphertext and estimate key length.
    """
    min_sequence_length = 3
    distances = []
    sequences = {}

    # Find repeating sequences
    for i in range(len(ciphertext) - min_sequence_length + 1):
        seq = ciphertext[i:i + min_sequence_length]
        if seq in sequences:
            sequences[seq].append(i)
        else:
            sequences[seq] = [i]

    # Calculate distances between repeats
    for seq, indices in sequences.items():
        if len(indices) > 1:
            for i in range(1, len(indices)):
                distances.append(indices[i] - indices[i - 1])

    # Estimate key length using the GCD of distances
    if distances:
        from math import gcd
        from functools import reduce
        estimated_key_length = reduce(gcd, distances)
        return estimated_key_length
    return None

def frequency_analysis(text):
    """
    Perform basic frequency analysis to determine the most common character.
    """
    # Initialize letter counts
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counts = {char: 0 for char in alphabet}

    for char in text:
        if char in counts:
            counts[char] += 1

    # Find the character with the maximum count
    max_char = max(counts, key=counts.get)
    return max_char

def decrypt_vigenere(ciphertext, key):
    """
    Decrypt the ciphertext using the given key.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted = ""
    j = 0
    key = key.upper()

    for i in range(len(ciphertext)):
        if ciphertext[i] not in alphabet:
            decrypted += ciphertext[i]
        else:
            ci = alphabet.find(ciphertext[i])
            ki = alphabet.find(key[j])
            decrypted += alphabet[(ci - ki + 26) % 26]
            j = (j + 1) % len(key)

    return decrypted

def cryptanalysis_vigenere(ciphertext):
    """
    Perform Vigenère cryptanalysis.
    """
    ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))  # Normalize text by removing non-alphabets and converting to uppercase
    key_length = kasiski_examination(ciphertext)

    if key_length:
        print(f"Estimated Key Length: {key_length}")

        # Divide text into segments based on estimated key length
        segments = ['' for _ in range(key_length)]
        for i in range(len(ciphertext)):
            segments[i % key_length] += ciphertext[i]

        # Guess each key character using frequency analysis
        guessed_key = ''
        for segment in segments:
            most_common_letter = frequency_analysis(segment)
            # Assume 'E' (most common letter) is encrypted with this character
            shift = (ord(most_common_letter) - ord('E')) % 26
            guessed_key += chr(ord('A') + shift)

        print(f"Guessed Key: {guessed_key}")
        return decrypt_vigenere(ciphertext, guessed_key)

    print("Key length estimation failed.")
    return None

# Example Ciphertext
ciphertext = "ZICVTWQNGRZGVTWAVZHCQYGLMGJ" # Working example
#ciphertext = "AOLPRRCHEVTSMETGSPFIPZUNEUSNPVXO" Example with spaces or without or sequences dosent work  
plaintext = cryptanalysis_vigenere(ciphertext)
print(f"Decrypted Text: {plaintext}")

