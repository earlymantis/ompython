#Ask the user their name

name = input("What's your name? ")

#find out how much their food bill was

bill = float(input("Hi %s, how much was your bill? " % (name)))

#calculate the various tip amounts, ensuring to convert to the proper data type

fifteen = float(bill * 0.15)
eighteen = float(bill * 0.18)
twenty = float(bill * 0.20)

#print your results to inform the user of their options

print ("""Well, %s, if you'd like to be cheap, leave $%.2f \n
If you'd like to be fair, leave $%.2f. \n
If you'd like to be generous, leave $%.2f.""" % (name, fifteen, eighteen, twenty))