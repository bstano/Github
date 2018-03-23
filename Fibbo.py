#Python Version 3.6
#This program takes a user's input and prints out a portion of the Fibbonacci Sequence
#up to the user's specified length

#Reads the user's input for the Sequence length
#User is given 3 tries to enter valid length
def user_length():
    n = 0
    while True:
		print( "You have {} more chance(s) to enter a valid integer.".format(3-n))
		user_length = input("What length should the sequence be?\n")#make sure the user has entered a positive integer greater than or equal to 2
		try: 
            length = int(user_length)
            if length >= 2:
                return length
            else:
                print('The length must be a positive integer of 2 or more.')
                n += 1
        except:
            print('The length should be a positive integer.')
            n += 1
	    #increment counter 'n' and check to see if user has any remaining guesses
        if n == 3:
            print("You're having trouble, let's set the length to 20")
            return 20
    
#Generates a Fibbonacci Sequence of a specified length   
def create_seq(length):
    result = []
    for n in range(length):
        if n == 0:
            result.append(0)
        elif n == 1:
            result.append(1)
        else:
            result.append(result[n-1]+result[n-2])
    return result
    
#Main function of the program
def main():
	length = user_length()
	sequence = create_seq(length)
	print("You're Fibbonacci Sequence is: /n")
	rint(sequence)

main()