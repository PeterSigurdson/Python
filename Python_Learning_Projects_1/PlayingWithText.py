# palindrome
import os

class PlayingWithTextStrings:
    
    def palindrome(word_IN, output):
        
        print("input is ", word_IN)
        inputCharacters = []
        outputCharacters = []

        i = 0
        for letter in word_IN:
            inputCharacters.append(letter.rstrip())
            # print(letter)
            i+=1
            
        # print("We now have the input string stored letter by letter in a LIST")
        # print("Now print out the letters in Reverse order.")
        
        for j in range(len(inputCharacters)-1,-1,-1):
            # print(inputCharacters[j])
            outputCharacters.append(inputCharacters[j])
            
        output = ''.join(outputCharacters)
        # print("output string is ", output)
            
        if word_IN.rstrip() == output:
            print("YOU WON! You found a Palindrome!")
        else:
            print("Sorry! You did NOT WIN")
        
        return output

if __name__ == "__main__":
    
    output = ""
    objectA = PlayingWithTextStrings
    f= open("input_word_list.txt", 'r')
    lines = f.readlines()
    
    for line in lines:
        output = objectA.palindrome(line.upper(), output)
        print("Output is: ", output)
    