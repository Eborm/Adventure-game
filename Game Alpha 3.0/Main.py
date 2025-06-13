#Lines of total code 1044

# Import files
import StartNewDay
from Varibles import ThingsFromStart
import Fuctions as F

# Introduce the player to the game
print("Game Alpha 3.0")
print("Welcome to my game \n")
# Ask for name

ThingsFromStart.Name = input("Hello what is your name? \n")

# Start main loop
while True:
    StartNewDay.NewDay()
    while True:
        if ThingsFromStart.Inheratence > 0:
            print("Your dad died and left you " + str(ThingsFromStart.Inheratence) + " dollars")
            ThingsFromStart.Money += ThingsFromStart.Inheratence
            ThingsFromStart.Inheratence = 0
        # Ask what they want to do
        Menu = input("\nWhat do you want to do?(Type Options to see all options)\n")
        # show options
        if Menu == 'Options' or Menu == 'options':
            print("\nAll options are\nSkip day\nGo to store\nDo a study\nLook for a job\nGo work\nVisit the bank\nPay the rent\nInventory\n")
        if Menu == 'Go to store' or Menu == 'go to store':
            # Start loop
            while True:
                # Ask what store
                Store = input("\nwhat store do you want to go to?(Type Stores for all the stores)\n")
                # show stores
                if Store == 'Stores' or Store == 'stores':
                    print("\nSupermarket\nElectronic Store\nClothing store\nExit")
                if Store == 'Exit' or Store == 'exit':
                    print(" ")
                    break
                if Store == 'Supermarket' or Store == 'supermarket':
                    F.Stores.Supermarket()
                if Store == 'Electronic store' or Store == 'electronic store':
                    F.Stores.Electronic()
                if Store == 'Clothing store' or Store == 'clothing store':
                    F.Stores.Clothing()
        if Menu == 'Do a study' and not ThingsFromStart.HasStudied or Menu == 'do a study' and not ThingsFromStart.HasStudied:
            F.Study.DoStudy()
            ThingsFromStart.HasStudied = True
        if Menu == 'Look for a job' or Menu == 'look for a job':
            # Start look
            while True:
                place = input('\nWhat place do you want to work?(Type places for all the places)\n')
                if place == 'Exit' or place == 'exit':
                    break
                if place == 'Places' or place == 'places':
                    print("\nAll places u can work at are:\nExit\nSupermarket\nBank\nMacdonald\nFactory")
                if place == 'supermarket' or place == 'Supermarket':
                    F.GetJob.Supermarket()
                    break
                if place == 'Bank' or place == 'bank':
                    F.GetJob.Bank()
                    break
                if place == 'Macdonald' or place == 'MacDonald':
                    F.GetJob.Macdonald()
                    break 
                if place == 'Factory' or place == 'factory':
                    F.GetJob.Factory()
                    break
        if Menu == 'Go work' or Menu == 'go work':
            F.Work()
            break
        if Menu == 'Skip day' or Menu == 'skip day':
            print("The day will now be skipped")
            break
        if Menu == 'Visit the bank' or Menu == 'visit the bank':
            F.VisitBank()
        if Menu == 'Pay the rent' or Menu == 'pay the rent':
            F.PayRent()
        if Menu == 'Inventory' or Menu == 'inventory':
            F.Inventory()
