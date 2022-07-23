# 1 Coding and decoding messages via Caesar Cipher
# Step 1.1. Decoding of messages & printing the results. This message has an offset of 10.
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "

message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

translated_message = ""
for letter in message:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated_message += alphabet[(letter_value + 10) % 26]
    else:
        translated_message += letter
print(translated_message)

# # Step 1.2 Encoding of messages & printing the results. This message also has an offset of 10.
#
encoded_message = "Hey, this is really cool. Can you read my message?"
decoded_message = ""
for letter in encoded_message.lower():
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        decoded_message += alphabet[(letter_value - 10) % 26]
    else:
        decoded_message += letter
print(decoded_message)
#
# # 2 Functions for decoding and coding.
# # Step 2.1 Decoding.
#
first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

def decoder(message,offset):
    decoded_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            decoded_message += alphabet[(letter_value + offset) % 26]
        else:
            decoded_message += letter
    return decoded_message

print(decoder(first_message, 10))
print(decoder(second_message, 14))
#
# # Step 2.2 Solving a Caesar Cipher without knowing the shift value.
#
coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(1,26):
    print("Offset: ", str(i))
    print("\t", decoder(coded_message,i).title() ,"\n")

# 5. The Vigenère Cipher.
# Step 5.1 Decoding of messages using function, without knowing the offset but keyword.

message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

def vigenere_decoder(message,keyword):
    letter_pointer = 0
    keyword_final = ""
    for letter in message:
        if not letter in punctuation:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer + 1) % len(keyword)
        else:
            keyword_final += letter
    translated_message = ""
    for i in range(0, len(message)):
        if not message[i] in punctuation:
            ln = alphabet.find(message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message

print(vigenere_decoder(message, keyword))

# Step 5.2 Cooding of messages using function with keyword but without the offset.

message_three = "thanks for teaching me all these cool ciphers! you really are the best!"
keyword = "besties"

def vigenere_coder(message, keyword):
    letter_pointer = 0
    keyword_final = ""
    for i in range(0, len(message)):
        if not message[i] in punctuation:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer + 1) % len(keyword)
        else:
            keyword_final += message[i]
    coded_message = ""
    for i in range(0, len(message)):
        if not message[i] in punctuation:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            coded_message += alphabet[ln % 26]
        else:
            coded_message += message[i]
    return coded_message

print(vigenere_coder(message_three, keyword))

# Step 5.3 Decoding of in step 5.2 coded message.

print(vigenere_decoder(vigenere_coder(message_three, keyword), keyword))



