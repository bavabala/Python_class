word = input("Enter the word: ") #string
output = " " #store the output
i = len(word)-1 #length of word
while i>= 0: #while loop
    output = output+word[i] #take the output with index
    i = i-1 #reverse the string
print(output)

