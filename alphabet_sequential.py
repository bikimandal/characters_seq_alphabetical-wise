import string
user_input = input("Enter a word: ")
# print(user_input)

# digits_mapping = {
#    "a" : "1 ",
#    "b" : "2 ",
#    "c" : "3 ",
#    "d" : "4 ",
#    "e" : "5 ",
#    "f" : "6 ",
#    "g" : "7 ",
#    "h" : "8 ",
#    "i" : "9 ",
#    "j" : "10 ",
#    "k" : "11 ",
#    "l" : "12 ",
#    "m" : "13 ",
#    "n" : "14 ",
#    "o" : "15 ",
#    "p" : "16 ",
#    "q" : "17 ",
#    "r" : "18 ",
#    "s" : "19 ",
#    "t" : "20 ",
#    "u" : "21 ",
#    "v" : "22 ",
#    "w" : "23 ",
#    "x" : "24 ",
#    "y" : "25 ",
#    "z" : "26 "
# }
# output = ""
# for ch in user_input:
#    output += digits_mapping.get(ch, "!")
# print(output)


for each_char in user_input:
   if each_char == " ":
      print(" ")
   else:             
         i=0
         j=0
         for letter in string.ascii_lowercase:
            i += 1
            if letter == each_char:
                  print(f"{each_char} = {i} ")
         for letter in string.ascii_uppercase:
            j += 1
            if letter == each_char:
                  print(f"{each_char} = {j} ")

