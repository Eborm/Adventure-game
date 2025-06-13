from Varibles import ThingsFromStart as TFS
import random

class Stores:
    # Function for supermarket
    @staticmethod
    def Supermarket():
        # Start loop
        while True:
            BoughtItem = False
            # Ask item
            Item = input("\nWhat do you want to buy?(Type Items to see all items)\n")
            if Item == 'Exit' or Item == 'exit':
                break
            if Item == 'Items' or Item == 'items':
                print(
                    "\nAll items are\nFood for 1 week(40 dollars)\nFood for 2 weeks(70 dollars)\nFood for 4 weeks(120 dollars)\nLottery ticket\nExit")
            if Item == 'Food for 1 week' or Item == 'food for 1 week' or Item == 'FF1W' or Item == 'ff1w' and TFS.Money > 39:
                TFS.Food += 1
                TFS.Money -= 40
                BoughtItem = True
            if Item == 'Food for 2 weeks' or Item == 'food for 2 weeks' or Item == 'FF2W' or Item == 'ff2w' and TFS.Money > 69:
                TFS.Food += 2
                TFS.Money -= 70
                BoughtItem = True
            if Item == 'Food for 4 weeks' or Item == 'food for 4 weeks' or Item == 'FF2W' or Item == 'ff2w' and TFS.Money > 119:
                TFS.Food += 4
                TFS.Money -= 120
                BoughtItem = True
            if Item == 'Lottery ticket' and TFS.Money > 99 or Item == 'lottery ticket' and TFS.Money > 99 or Item == 'LT' and TFS.Money > 99 or Item == 'lt' and TFS.Money > 99:
                TFS.LotteryTickets += 10
                TFS.Money -= 100
                BoughtItem = True
            if BoughtItem:
                print("successfully bought the item")
            if not BoughtItem:
                print("You didn't have enough money")

    # Function for Electronics store
    @staticmethod
    def Electronic():
        while True:
            BoughtItem = False
            Item = input("\nWhat do you want to buy?(Type Items to see all items)\n")
            if Item == 'Exit' or Item == 'exit':
                break
            if Item == 'Items' or Item == 'items':
                print(
                    "\nAll items are\nRefrigerator(800 dollars)\nFreezer(500 dollars)\nStove(550 dollars)\nColor TV(500 dollars)\nVRC(300 dollars)\nStereo(400 dollars)\nMicrowave(300 dollars)\nHot tub(1200 dollars)\nComputer(1600 dollars)\nExit")
            if Item == 'Refrigerator' or Item == 'refrigerator' and TFS.Money > 799 and 'RF' not in TFS.Items:
                TFS.Items.append('RF')
                TFS.Money -= 800
                BoughtItem = True
            if Item == 'Freezer' or 'freezer' and TFS.Money > 499 and 'FR' not in TFS.Items:
                TFS.Items.append('FR')
                TFS.Money -= 500
                BoughtItem = True
            if Item == 'Stove' and TFS.Money > 549 and 'S' not in TFS.Items or Item == 'stove' and TFS.Money > 549 and 'S' not in TFS.Items:
                TFS.Items.append('S')
                TFS.Money -= 550
                BoughtItem = True
            if Item == 'Color TV' or Item == 'color tv' and TFS.Money > 499 and 'CTV' not in TFS.Items:
                TFS.Items.append('CTV')
                TFS.Money -= 500
                BoughtItem = True
            if Item == 'VRC' or Item == 'vrc' and TFS.Money > 299 and 'VRC' not in TFS.Items:
                TFS.Items.append('VRC')
                TFS.Money -= 300
                BoughtItem = True
            if Item == 'Stereo' or Item == 'stereo' and TFS.Money > 399 and 'ST' not in TFS.Items:
                TFS.Items.append('ST')
                TFS.Money -= 399
                BoughtItem = True
            if Item == 'Microwave' or Item == 'microwave' and TFS.Money > 299 and 'MW' not in TFS.Items:
                TFS.Items.append('MW')
                TFS.Money -= 300
                BoughtItem = True
            if Item == 'Hot tub' or Item == 'hot tub' and TFS.Money > 1199 and 'HT' not in TFS.Items:
                TFS.Items.append('HT')
                TFS.Money -= 1200
                BoughtItem = True
            if Item == 'Computer' or Item == 'computer' and TFS.Money > 1599 and 'PC' not in TFS.Items:
                TFS.Items.append('PC')
                TFS.Money -= 1600
                BoughtItem = True
            if BoughtItem:
                print("successfully bought the item")
            if not BoughtItem:
                print("You didn't have enough money")

    # Function for the clothing store
    @staticmethod
    def Clothing():
        while True:
            BoughtItem = False
            Item = input("\nWhat do you want to buy?(Type Items to see all items)\n")
            if Item == 'Exit' or Item == 'exit':
                break
            if Item == 'Items' or Item == 'items':
                print(
                    "All items are:\nCasual clothes(75 dollars)\nDress clothes(125 dollars)\nBusiness suit(290 dollars)\n")
            if Item == 'Casual clothes' or 'casual clothes' and TFS.Money > 74:
                TFS.ClothingLevel = 1
                TFS.Money -= 75
                BoughtItem = True
            if Item == 'Dress clothes' or Item == 'dress clothes' and TFS.Money > 124:
                TFS.ClothingLevel = 2
                TFS.Money -= 125
                BoughtItem = True
            if Item == 'Business suit' or 'business suit' and TFS.Money > 289:
                TFS.ClothingLevel = 3
                TFS.Money -= 290
                BoughtItem = True
            if BoughtItem:
                print("successfully bought the item")
            if not BoughtItem:
                print("You didn't have enough money")


class Study:
    @staticmethod
    # Making a class for the studies
    def DoStudy():
        # Making variables
        import Varibles
        studies = Varibles.ThingsFromStart.Studies
        Money = Varibles.ThingsFromStart.Money
        Varibles.ThingsFromStart.Enroll = Varibles.ThingsFromStart.Enroll
        while True:
            # Making sure the player has enough money to get enrolled and is enrolled before continuing
            if Varibles.ThingsFromStart.HasStudied:
                print("\nYou have already done this today")
                break
            if Varibles.ThingsFromStart.Enroll == 0:
                print("\nYou currently are not enrolled")
                Buy_enroll = input("Do you want to enroll?: ")
                if Buy_enroll == "Y" or Buy_enroll == 'yes' or Buy_enroll == 'y' or Buy_enroll == 'Yes':
                    if Money == 40 or Money > 40:
                        Money = Money - 40
                        Varibles.ThingsFromStart.Enroll += 1
                        print("")
                    else:
                        print("\nYou don't have any money")
                        print("Find a job")
                        break
                elif Buy_enroll == "N":
                    break
            # Making sure the player can't do a study that requires a study he hasn't done
            else:
                if 'TS' in studies:
                    if 'ET' not in studies:
                        print("Electronics/ET")
                    if 'PE' not in studies:
                        print("Pre-Engineering/PE")
                if 'PE' in studies:
                    if 'E' not in studies:
                        print("Engineering/E")
                if 'JC' in studies:
                    if 'BA' not in studies:
                        print("Business Administration/BA")
                    if 'A' not in studies:
                        print("Academic/A")
                if 'A' in studies:
                    if 'GS' not in studies:
                        print("Graduate School/GS")
                if 'GS' in studies:
                    if 'PD' not in studies:
                        print("Post Doctoral/PD")
                if 'PD' in studies:
                    if 'PD' not in studies:
                        print("Research/R")
                if 'R' in studies:
                    if 'P' not in studies:
                        print("Publishing/P")
                if 'TS' not in studies:
                    print("Trade School/TS")
                if 'JC' not in studies:
                    print("Junior College/JC")
                ele = input("\nWhich study do you want to do?: ")
                # Making sure it is a valid study before adding it
                if ele == 'JC' and 'JC' not in studies:
                    studies.append(ele)
                    Varibles.ThingsFromStart.Enroll = Varibles.ThingsFromStart.Enroll = 1
                    Varibles.ThingsFromStart.Money = Money
                    print("You did the study successfully\n")
                    break
                if ele == 'TS' and 'TS' not in studies:
                    studies.append(ele)
                    Varibles.ThingsFromStart.Enroll = Varibles.ThingsFromStart.Enroll = 1
                    Varibles.ThingsFromStart.Money = Money
                    print("You did the study successfully\n")
                    break
                if ele == 'P' and 'R' in studies and 'P' not in studies:
                    studies.append(ele)
                    Varibles.ThingsFromStart.Enroll = Varibles.ThingsFromStart.Enroll = 1
                    Varibles.ThingsFromStart.Money = Money
                    print('You did the study successful')
                    break
                if ele == 'PD' and 'GS' in studies and 'GS' not in studies:
                    studies.append(ele)
                    Varibles.ThingsFromStart.Enroll = Varibles.ThingsFromStart.Enroll = 1
                    Varibles.ThingsFromStart.Money = Money
                    print("You did the study successfully\n")
                    break
                if ele == 'R' and 'PD' in studies and 'R' not in studies:
                    studies.append(ele)
                    Varibles.ThingsFromStart.Enroll = Varibles.ThingsFromStart.Enroll = 1
                    Varibles.ThingsFromStart.Money = Money
                    print("You did the study successfully\n")
                    break
                if ele == 'GS' and 'A' in studies and 'GS' not in studies:
                    studies.append(ele)
                    Varibles.ThingsFromStart.Enroll = Varibles.ThingsFromStart.Enroll = 1
                    Varibles.ThingsFromStart.Money = Money
                    print("You did the study successfully\n")
                    break
                if ele == 'A' and 'JC' in studies and 'A' not in studies:
                    studies.append(ele)
                    Varibles.ThingsFromStart.Enroll = Varibles.ThingsFromStart.Enroll = 1
                    Varibles.ThingsFromStart.Money = Money
                    print("You did the study successfully\n")
                    break
                if ele == 'BA' and 'JC' in studies and 'BA' not in studies:
                    studies.append(ele)
                    Varibles.ThingsFromStart.Enroll = Varibles.ThingsFromStart.Enroll = 1
                    Varibles.ThingsFromStart.Money = Money
                    print("You did the study successfully\n")
                    break
                if ele == 'E' and 'E' not in studies and 'PE' in studies:
                    studies.append(ele)
                    Varibles.ThingsFromStart.Enroll = Varibles.ThingsFromStart.Enroll = 1
                    Varibles.ThingsFromStart.Money = Money
                    print("You did the study successfully\n")
                    break
                if ele == 'PE' and 'PE' not in studies and 'TS' in studies:
                    studies.append(ele)
                    Varibles.ThingsFromStart.Enroll = Varibles.ThingsFromStart.Enroll = 1
                    Varibles.ThingsFromStart.Money = Money
                    print("You did the study successfully\n")
                    break
                if ele == 'ET' and 'TS' in studies and 'ET' not in studies:
                    studies.append(ele)
                    Varibles.ThingsFromStart.Enroll = Varibles.ThingsFromStart.Enroll = 1
                    Varibles.ThingsFromStart.Money = Money
                    print("You did the study successfully\n")
                    break
                # Telling the player it is not a valid study and restarting this program
                else:
                    print('\nThis is not a valid study')


class GetJob:
    @staticmethod
    def Supermarket():
        while True:
            CantNotApply = False
            GotJob = False
            i = random.randint(1, 5)
            Job = input("\nWhat job do you want?(Type jobs to see all jobs)\n")
            if Job == 'Jobs' or Job == 'jobs':
                CantNotApply = True
                print(
                    "\nAll jobs are:\nExit\nJanitor 5 dollars a hour\nCashier 9 dollars a hour\nButcher 14 dollars a hour\nAssistant manager 17 dollars a hour\nManager 20 dollars a hour")
            if i == 2 and not CantNotApply:
                print('There where no openings')
                break
            if Job == 'Exit' or Job == 'exit':
                break
            if Job == 'Janitor' or Job == 'janitor':
                TFS.Wage = 5
                TFS.Job = 'Janitor'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 1
            if Job == 'Cashier' and TFS.WorkExperience > 19 or Job == 'cashier' and TFS.WorkExperience > 19:
                TFS.Wage = 9
                TFS.Job = 'Cashier'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 1
            if Job == 'Cashier' and TFS.WorkExperience < 20 or Job == 'cashier' and TFS.WorkExperience < 20:
                print("You don't have enough work experience")
            if Job == 'Butcher' and TFS.WorkExperience > 39 and 'TS' in TFS.Studies or Job == 'butcher' and TFS.WorkExperience > 39 and 'TS' in TFS.Studies:
                TFS.Wage = 14
                TFS.Job = 'Butcher'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 1
            if Job == 'Butcher' and TFS.WorkExperience < 40 or Job == 'butcher' and TFS.WorkExperience < 40:
                print("You don't have enough work experience")
            if Job == 'Butcher' and 'TS' not in TFS.Studies or Job == 'butcher' and 'TS' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Assistant manager' and 'JC' in TFS.Studies and TFS.WorkExperience > 59 or Job == 'assistant manager' and 'JC' in TFS.Studies and TFS.WorkExperience > 59:
                TFS.Wage = 17
                TFS.Job = 'Assistant manager'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 2
            if Job == 'Assistant manager' and 'JC' not in TFS.Studies or Job == 'assistant manager' and 'JC' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Assistant manager' and TFS.WorkExperience < 60 and Job == 'assistant manager' and TFS.WorkExperience < 60:
                print("You don't have enough work experience")
            if Job == 'Manager' and 'BA' in TFS.Studies and TFS.WorkExperience > 69 or Job == 'manager' and 'BA' in TFS.Studies and TFS.WorkExperience > 69:
                TFS.Wage = 20
                TFS.Job = 'Manager'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 3
            if Job == 'Manager' and 'BA' not in TFS.Studies or Job == 'manager' and 'BA' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Manager' and TFS.WorkExperience < 70 or Job == 'manager' and TFS.WorkExperience < 70:
                print("You don't have enough work experience")
            if GotJob:
                TFS.Store = 'Supermarket'
                print('You have successfully gotten the job')
                break

    @staticmethod
    def Bank():
        while True:
            CantNotApply = False
            GotJob = False
            i = random.randint(1, 5)
            Job = input("\nWhat job do you want?(Type jobs to see all jobs)\n")
            if Job == 'Exit' or Job == 'exit':
                break
            if Job == 'Jobs' or Job == 'jobs':
                CantNotApply = True
                print(
                    "\nAll jobs are:\nExit\nJanitor 6 dollars a hour\nTeller 10 dollars a hour\nAssistant manager 20 dollars a hour\nManager 25 dollars a hour")
            if i == 2 and not CantNotApply:
                print('There where no openings')
                break
            if Job == 'Janitor' or Job == 'janitor':
                TFS.Wage = 6
                TFS.Job = 'Janitor'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 1
            if Job == 'Teller' and 'JC' in TFS.Studies and TFS.WorkExperience > 19 or Job == 'teller' and 'JC' in TFS.Studies and TFS.WorkExperience > 19:
                TFS.Wage = 10
                TFS.Job = 'Teller'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 2
            if Job == 'Teller' and 'JC' not in TFS.Studies or Job == 'teller' and 'JC' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Teller' and TFS.WorkExperience < 20 or Job == 'Teller' and TFS.WorkExperience < 20:
                print("You don't have enough work experience")
            if Job == 'Assistant manager' and 'BA' in TFS.Studies and TFS.WorkExperience > 39 or Job == 'assistant manager' and 'BA' in TFS.Studies and TFS.WorkExperience > 39:
                TFS.Job = 'Assistant manager'
                TFS.Wage = 20
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 3
            if Job == 'Assistant manager' and 'BA' not in TFS.Studies or Job == 'assistant manager' and 'BA' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Assistant manager' and TFS.WorkExperience < 40 or Job == 'assistant manager' and TFS.WorkExperience < 40:
                print("You don't have enough work experience")
            if Job == 'Manager' and 'BA' in TFS.Studies and TFS.WorkExperience > 54 or Job == 'manager' and 'BA' in TFS.Studies and TFS.WorkExperience > 54:
                TFS.Wage = 25
                TFS.Job = 'Manager'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 3
            if Job == 'Manager' and 'BA' not in TFS.Studies or Job == 'manager' and 'BA' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Manager' and TFS.WorkExperience < 55 or Job == 'manager' and TFS.WorkExperience < 55:
                print("You don't have enough work experience")
            if Job == 'Broker' and 'BA' in TFS.Studies and 'A' not in TFS.Studies and TFS.WorkExperience > 69 or Job == 'broker' and 'BA' in TFS.Studies and 'A' not in TFS.Studies and TFS.WorkExperience > 69:
                TFS.Wage = 27
                TFS.Job = 'Broker'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 3
            if Job == 'Broker' and 'BA' not in TFS.Studies or Job == 'Broker' and 'A' not in TFS.Studies or Job == 'broker' and 'BA' not in TFS.Studies or Job == 'broker' and 'A' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Broker' and TFS.WorkExperience < 70 or Job == 'broker' and TFS.WorkExperience < 70:
                print("You don't have enough work experience")
            if GotJob:
                TFS.Store = 'Bank'
                print('You have successfully gotten the job')
                break

    @staticmethod
    def Macdonald():
        while True:
            CantNotApply = False
            GotJob = False
            i = random.randint(1, 5)
            Job = input("\nWhat job do you want?(Type jobs to see all jobs)\n")
            if Job == 'Jobs' or Job == 'jobs':
                CantNotApply = True
                print(
                    "\nAll jobs are:\nExit\nCook 5 dollars a hour\nClerk 6 dollars a hour\nAssistant manager 9 dollars a hour\nManager 12 dollars a hour")
            if i == 2 and not CantNotApply:
                print('There where no openings')
                break
            if Job == 'Exit' or 'exit':
                break
            if Job == 'Cook' or Job == 'cook':
                TFS.Wage = 5
                TFS.Job = 'Cook'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 1
            if Job == 'Clerk' and TFS.WorkExperience > 4 or Job == 'clerk' and TFS.WorkExperience > 4:
                TFS.Wage = 6
                TFS.Job = 'Clerk'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 1
            if Job == 'Clerk' and TFS.WorkExperience < 5 or Job == 'clerk' and TFS.WorkExperience < 5:
                print("You don't have enough work experience")
            if Job == 'Assistant manager' and 'JC' in TFS.Studies and TFS.WorkExperience > 14 or Job == 'assistant manager' and 'JC' in TFS.Studies and TFS.WorkExperience > 14:
                TFS.Wage = 9
                TFS.Job = 'Assistant manager'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 1
            if Job == 'Assistant manager' and 'JC' not in TFS.Studies or Job == 'assistant manager' and 'JC' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Assistant manager' and TFS.WorkExperience < 15 or Job == 'assistant manager' and TFS.WorkExperience < 15:
                print("You don't have enough work experience")
            if Job == 'Manager' and 'JC' in TFS.Studies and TFS.WorkExperience > 24 or Job == 'manager' and 'JC' in TFS.Studies and TFS.WorkExperience > 24:
                TFS.Wage = 12
                TFS.Job = 'Manager'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 2
            if Job == 'Manager' and 'JC' not in TFS.Studies or Job == 'manager' and 'JC' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Manager' and TFS.WorkExperience < 25 or Job == 'manager' and TFS.WorkExperience < 25:
                print("You don't have enough work experience")
            if GotJob:
                TFS.Store = 'Macdonald'
                print('You have successfully gotten the job')
                break

    @staticmethod
    def ElectronicsStore():
        while True:
            CantNotApply = False
            GotJob = False
            i = random.randint(1, 5)
            Job = input("\nWhat job do you want?(Type jobs to see all jobs)\n")
            if Job == 'Jobs' or Job == 'jobs':
                CantNotApply = True
                print(
                    "\nAll jobs are:\nExit\nClerk 6 dollars a hour\nSalesperson 8 dollars a hour\nElectronic repairman 11 dollars a hour\nManager 14 dollars a hour\n")
            if Job == 'Exit' or Job == 'exit':
                break
            if i == 2 and not CantNotApply:
                print('There where no openings')
                break
            if Job == 'Clerk' or Job == 'clerk':
                TFS.Wage = 6
                TFS.Job = 'Clerk'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 1
            if Job == 'Salesperson' and TFS.WorkExperience > 9 or Job == 'salesperson' and TFS.WorkExperience > 9:
                TFS.Wage = 8
                TFS.Job = 'Salesperson'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 2
            if Job == 'Salesperson' and TFS.WorkExperience < 10 or Job == 'salesperson' and TFS.WorkExperience < 10:
                print("You don't have enough work experience")
            if Job == 'Electronic repairman' and 'E' in TFS.Studies and TFS.WorkExperience > 14 or Job == 'electronic repairman' and 'E' in TFS.Studies and TFS.WorkExperience > 14:
                TFS.Wage = 11
                TFS.Job = "Electronic repairman"
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 1
            if Job == 'Electronic repairman' and 'E' not in TFS.Studies or Job == 'electronic repairman' and 'E' not in TFS.Studies:
                print("You haven't don the right studies")
            if Job == 'Electronic repairman' and TFS.WorkExperience < 15 or Job == 'electronic repairman' and TFS.WorkExperience < 15:
                print("You don't have enough work experience")
            if Job == 'Manager' and 'E' in TFS.Studies and 'JC' in TFS.Studies and TFS.WorkExperience > 24 or Job == 'manager' and 'E' in TFS.Studies and 'JC' in TFS.Studies and TFS.WorkExperience > 24:
                TFS.Wage = 14
                TFS.Job = 'Manager'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 3
            if Job == 'Manager' and 'E' not in TFS.Studies or Job == 'Manager' and 'JC' not in TFS.Studies or Job == 'manager' and 'E' not in TFS.Studies or Job == 'manager' and 'JC' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Manager' and TFS.WorkExperience < 25 or Job == 'manager' and TFS.WorkExperience < 25:
                print("You don't have enough work experience")
            if GotJob:
                TFS.Store = 'Electronics store'
                print('You have successfully gotten the job')
                break

    @staticmethod
    def Factory():
        while True:
            CantNotApply = False
            GotJob = False
            i = random.randint(1, 5)
            Job = input("\nWhat job do you want?(Type jobs to see all jobs)\n")
            if Job == 'Jobs' or Job == 'jobs':
                CantNotApply = True
                print(
                    "\nAll jobs are:\nExit\nJanitor 7 dollars a hour\nAssembly worker 10 dollars a hour\nSecretary 11 dollars a hour\nMachinists helper 12 dollars a hour\nExecutive secretary 18 dollars a hour\nMachinist 19 dollars a hour\nDepartment manager 22 dollars a hour\nEngineer 23 dollars a hour\nGeneral manager 25 dollars a hour\n")
            if Job == 'Exit' or Job == 'exit':
                break
            if i == 2 and not CantNotApply:
                print('There where no openings')
                break
            if Job == 'Janitor' or Job == 'janitor':
                TFS.Wage = 7
                TFS.Job = 'Janitor'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 1
            if Job == 'Assembly worker' and 'TS' in TFS.Studies and TFS.WorkExperience > 9 or Job == 'assembly worker' and 'TS' in TFS.Studies and TFS.WorkExperience > 9:
                TFS.Wage = 10
                TFS.Job = 'Assembly worker'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 1
            if Job == 'Assembly worker' and 'TS' not in TFS.Studies or Job == 'assembly worker' and 'TS' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Assembly worker' and TFS.WorkExperience < 10 or Job == 'Assembly worker' and TFS.WorkExperience < 10:
                print("You don't have enough work experience")
            if Job == 'Secretary' and 'JC' in TFS.Studies and TFS.WorkExperience > 14 or Job == 'secretary' and 'JC' in TFS.Studies and TFS.WorkExperience > 14:
                TFS.Wage = 11
                TFS.Job = 'Secretary'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 2
            if Job == 'Secretary' and 'JC' not in TFS.Studies or Job == 'secretary' and 'JC' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Secretary' and TFS.WorkExperience < 15 or Job == 'secretary' and TFS.WorkExperience < 15:
                print("You don't have enough work experience")
            if Job == 'Machinists helper' and 'PE' in TFS.Studies and TFS.WorkExperience > 19 or Job == 'machinists helper' and 'PE' in TFS.Studies and TFS.WorkExperience > 19:
                TFS.Wage = 12
                TFS.Job = 'Machinists helper'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 1
            if Job == 'Machinists helper' and 'PE' not in TFS.Studies or Job == 'machinists helper' and 'PE' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Machinists helper' and TFS.WorkExperience < 20 or Job == 'machinists helper' and TFS.WorkExperience < 20:
                print("You don't have enough work experience")
            if Job == 'Executive secretary' and 'BA' in TFS.Studies and TFS.WorkExperience > 24 or Job == 'executive secretary' and 'BA' in TFS.Studies and TFS.WorkExperience > 24:
                TFS.Wage = 18
                TFS.Job = 'Executive secretary'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 3
            if Job == 'Executive secretary' and 'BA' not in TFS.Studies or Job == 'executive secretary' and 'BA' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Executive secretary' and TFS.WorkExperience < 25 or Job == 'executive secretary' and TFS.WorkExperience < 25:
                print("You don't have enough work experience")
            if Job == 'Machinist' and 'E' in TFS.Studies and TFS.WorkExperience > 29 or Job == 'machinist' and 'E' in TFS.Studies and TFS.WorkExperience > 29:
                TFS.Wage = 19
                TFS.Job = 'Machinist'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 1
            if Job == 'Machinist' and 'E' not in TFS.Studies or Job == 'machinist' and 'E' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Machinist' and TFS.WorkExperience < 30 or Job == 'machinist' and TFS.WorkExperience < 30:
                print("You don't have enough work experience")
            if Job == 'Department manager' and 'BA' in TFS.Studies and TFS.WorkExperience > 29 or Job == 'Department manager' and 'BA' in TFS.Studies and TFS.WorkExperience > 29:
                TFS.Wage = 22
                TFS.Job = 'Department manager'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 3
            if Job == 'Department manager' and 'BA' not in TFS.Studies or Job == 'department manager' and 'BA' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Department manager' and TFS.WorkExperience < 30 or Job == 'department manager' and TFS.WorkExperience < 30:
                print("You don't have enough work experience")
            if Job == 'Engineer' and 'JC' in TFS.Studies and 'E' in TFS.Studies and TFS.WorkExperience > 34 or Job == 'engineer' and 'JC' in TFS.Studies and 'E' in TFS.Studies and TFS.WorkExperience > 34:
                TFS.Wage = 23
                TFS.Job = 'Engineer'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 3
            if Job == 'Engineer' and 'JC' not in TFS.Studies or Job == 'Engineer' and 'E' not in TFS.Studies or Job == 'engineer' and 'JC' not in TFS.Studies or Job == 'engineer' and 'E' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'Engineer' and TFS.WorkExperience < 35 or Job == 'engineer' and TFS.WorkExperience < 35:
                print("You don't have enough work experience")
            if Job == 'General manager' and 'BA' in TFS.Studies and 'E' in TFS.Studies and TFS.WorkExperience > 39 or Job == 'general manager' and 'BA' in TFS.Studies and 'E' in TFS.Studies and TFS.WorkExperience > 39:
                TFS.Wage = 25
                TFS.Job = 'General manager'
                GotJob = True
                TFS.ClothingLevelRequiredForJob = 3
            if Job == 'General manager' and 'BA' not in TFS.Studies or Job == 'General manager' and 'E' not in TFS.Studies or Job == 'general manager' and 'BA' not in TFS.Studies or Job == 'general manager' and 'E' not in TFS.Studies:
                print("You haven't done the right studies")
            if Job == 'General manager' and TFS.WorkExperience < 40 or Job == 'general manager' and TFS.WorkExperience < 40:
                print("You don't have enough work experience")
            if GotJob:
                TFS.Store = 'Factory'
                print('You have successfully gotten the job')
                break


def Work():
    if TFS.ClothingLevel < TFS.ClothingLevelRequiredForJob:
        print("You don't have the right clothes for this job")
    if TFS.ClothingLevel == TFS.ClothingLevelRequiredForJob and TFS.PayedRent == True or TFS.ClothingLevel > TFS.ClothingLevelRequiredForJob and TFS.PayedRent == True:
        t = random.randint(4, 7)
        print("\nYou have worked for " + str(t) + " hours")
        MoneyMade = TFS.Wage * t
        print("\nYou have made " + str(MoneyMade) + " dollars")
        TFS.Money += MoneyMade
        TFS.WorkExperience += 1 * t
    if TFS.ClothingLevel == TFS.ClothingLevelRequiredForJob and TFS.PayedRent == False or TFS.ClothingLevel > TFS.ClothingLevelRequiredForJob and TFS.PayedRent == False:
        t = random.randint(4, 7)
        print("\nYou have worked for " + str(t) + " hours")
        MoneyMade = TFS.Wage * t
        TFS.RentNeedToBePaid -= MoneyMade * 0.25
        print("\nYou have made " + str(MoneyMade) + " dollars there will be " + str(MoneyMade * 0.25) + " subtract from you wage to pay rent")
        TFS.Money += (MoneyMade - (MoneyMade * 0.25))
        TFS.WorkExperience += 1 * t


def VisitBank():
    while True:
        DO = input('\nWhat do you want to do in the bank?(Type options to see all options)\n')
        if DO == 'Exit' or DO == 'exit':
            break
        if DO == 'Options' or DO == 'options':
            print("\nAll options are\nExit\nLend money\nDeposit money\nPay off loans\nPick up money\n")
        if DO == 'Lend money' or DO == 'lend money':
            Money = input("\nHow much money do you want to lend?\n")
            print("\nwe will add the amount to your account")
            TFS.Money += int(Money)
            TFS.LendedMoney += int(Money)
        if DO == 'Deposit money' or DO == 'deposit money':
            Money = input("\nHow much money do you want to deposit\n")
            if int(Money) < TFS.Money or Money == TFS.Money:
                print("\nWe will add the money to your savings account")
                TFS.DepositedMoney += int(Money)
                TFS.Money -= int(Money)
            if int(Money) > TFS.Money:
                print("\nYou don't have that amount of money")
        if DO == 'Pick up money' or DO == 'pick up money':
            Money = input("\nYou currently have " + str(TFS.DepositedMoney) + " money in your savings account\nHow much would you like to pick up?\n")
            if int(Money) > TFS.DepositedMoney:
                print("\nYou don't have that amount of money")
            if int(Money) < TFS.Money or Money == TFS.Money:
                print("\nWe will add the money to your account")
                TFS.Money += int(Money)
                TFS.DepositedMoney -= int(Money)
        if DO == 'Pay off loans' or DO == 'pay off loans':
            Money = input("\nYou currently ow the bank " + str(TFS.LendedMoney) + " dollars\nHow much would you like to pay off\n")
            if int(Money) > TFS.LendedMoney:
                print("\nYou don't ow the bank that much money")
            if int(Money) == TFS.LendedMoney or Money > TFS.LendedMoney:
                print("\nWe will now remove the money from your account")
                TFS.Money -= int(Money)
                TFS.LendedMoney -= int(Money)


def Intrest():
    TFS.LendedMoney = TFS.LendedMoney * 1.5
    TFS.DepositedMoney = TFS.DepositedMoney * 1.4


def Rent():
    print("\nRent is due")
    TFS.PayedRent = False


def PayRent():
    if TFS.Appartment == 1 and not TFS.PayedRent:
        print("\nYou currently live in the low security apartment\nYou have to pay 325 dollars for rent")
        PayorUpgrade = input("Dou you want to upgrade to the high security apartment(650) or pay rent?\n")
        if PayorUpgrade == 'Pay' and TFS.Money > 324 or PayorUpgrade == 'pay' and TFS.Money > 324:
            print("We will subtract the money from your account")
            TFS.Money -= 325
            TFS.PayedRent = True
        if PayorUpgrade == 'Pay' and TFS.Money < 325 or PayorUpgrade == 'pay' and TFS.Money < 325:
            print("You don't have enough money")
        if PayorUpgrade == 'Upgrade' and TFS.Money > 649 or PayorUpgrade == 'upgrade' and TFS.Money > 649:
            print("We will subtract the money from your account")
            TFS.Money -= 650
            TFS.PayedRent = True
            TFS.Appartment = 2
        if PayorUpgrade == 'Upgrade' and TFS.Money < 650 or PayorUpgrade == 'upgrade' and TFS.Money < 650:
            print("You don't have enough money to upgrade")
    if TFS.Appartment == 2 and not TFS.PayedRent:
        print("\nYou currently live in the high security apartment\nYou have to pay 650 dollars for rent")
        PayorUpgrade = input("Dou you want to downgrade to the low security apartment(325) or pay rent?\n")
        if PayorUpgrade == 'Pay' and TFS.Money > 649 or PayorUpgrade == 'pay' and TFS.Money > 649:
            print("We will subtract the money from your account")
            TFS.Money -= 650
            TFS.PayedRent = True
        if PayorUpgrade == 'Pay' and TFS.Money < 649 or PayorUpgrade == 'pay' and TFS.Money < 649:
            print("You don't have enough money")
        if PayorUpgrade == 'Downgrade' and TFS.Money > 324 or PayorUpgrade == 'downgrade' and TFS.Money > 324:
            print("We will downgrade you to the low security apartment")
            TFS.Appartment = 1
            TFS.PayedRent = True
        if PayorUpgrade == 'Downgrade' and TFS.Money < 325 or PayorUpgrade == 'downgrade' and TFS.Money < 325:
            print("You don't have enough money to downgrade")


def CheckifRentPaid():
    if TFS.RentNeedToBePaid < 0:
        print("You have paid off your dept from the rent department")
        TFS.PayedRent = True


def Inventory():
    Studies = TFS.Studies
    print("\nYou currently have " + str(TFS.Money) + " dollars\nYou have food for " + str(TFS.Food) + " weeks\nYou have " + str(TFS.LotteryTickets) + ' Lottery tickets')
    if 'RF' in TFS.Items:
        print("You have a refrigerator")
    if 'F' in TFS.Items:
        print("You have a freezer")
    if 'S' in TFS.Items:
        print("You have a stove ")
    if 'CTV' in TFS.Items:
        print("You have a color TV")
    if 'VRC' in TFS.Items:
        print("You have a VRC")
    if 'ST' in TFS.Items:
        print("You have a Stereo")
    if 'MW' in TFS.Items:
        print("You have a microwave")
    if 'HT' in TFS.Items:
        print("You have a hot tub")
    if 'PC' in TFS.Items:
        print("You have a computer")
    print("You are working at the " + str(TFS.Store) + " and you are the " + str(TFS.Job) + " and you " + str(TFS.Wage) + " dollars a hour")
    if 'JC' in Studies or 'TS' in Studies:
        print("You have done the studies: ")
    if 'ET' in Studies:
        print("Electronics")
    if 'PE' in Studies:
        print("Pre-Engineering")
    if 'E' in Studies:
        print("Engineering")
    if 'BA' in Studies:
        print("Business administration")
    if 'A' in Studies:
        print("Academic")
    if 'GS' in Studies:
        print("Graduate school")
    if 'PD' in Studies:
        print("Post doctoral")
    if 'R' in Studies:
        print("Research")
    if 'P' in Studies:
        print("Publishing")
    if 'TS' in Studies:
        print("Trade school")
    if 'JC' in Studies:
        print("Junior college")
    if 'JC' not in Studies and 'TS' not in Studies:
        print("You haven't done any studies")
    if TFS.Appartment == 1:
        print("You are currently living in the low security apartment")
    if TFS.Appartment == 2:
        print("You are currently living in the high security apartment")


def Lottery():
    for i in range(TFS.LotteryTickets):
        Temp_LotteryTicketslevel = 0
        x = 0
        y = 0
        while x == y:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            if x == y:
                Temp_LotteryTicketslevel += 1
            elif x != y:
                break
        if Temp_LotteryTicketslevel == 0:
            print("You won nothing")
        if Temp_LotteryTicketslevel == 1:
            print("You won 200 dollars")
            TFS.Money += 200
        if Temp_LotteryTicketslevel == 2:
            print("You won 500 dollars")
            TFS.Money += 500
        if Temp_LotteryTicketslevel == 3:
            print("You won 700 dollars")
            TFS.Money += 700
        if Temp_LotteryTicketslevel == 4:
            print("You won 1000 dollars")
            TFS.Money += 1000
        if Temp_LotteryTicketslevel == 5:
            print("You won 2000 dollars")
            TFS.Money += 2000
        if Temp_LotteryTicketslevel == 6:
            print("You won 5000 dollars")
            TFS.Money += 5000
    TFS.LotteryTickets = 0


def RandomGetSick():
    CantGetSick = False
    if TFS.StarvingForDays > 3:
        TFS.Sick = True
    if 'S' in TFS.Items:
        CantGetSick = True
    if CantGetSick:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        if a == b:
            TFS.Sick = True
    if not CantGetSick:
        a = random.randint(1, 4)
        b = random.randint(1, 4)
        if a == b:
            TFS.Sick = True
    if TFS.Sick:
        Cost = random.randint(30, 150)
        while Cost > TFS.Money:
            Cost -= 1
        print("You got sick and went to the hospital")
        print("It cost you ", Cost)
        TFS.Money -= Cost
        TFS.Sick = False


def PCBitcoinMine():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if a == b and 'PC' in TFS.Items:
        cash = random.randint(50, 200)
        print("You made " + str(cash) + " dollars with your pc")
        TFS.Money += cash


def RandomGetRobbed():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    if a == b:
        StolenMoney = random.randint(30, 500)
        while StolenMoney > TFS.Money:
            StolenMoney -= 1
        print("You got robbed and the robber stole " + str(StolenMoney) + " dollars from you")
        TFS.Money -= StolenMoney


def RandomGetRobbedHome():
    if len(TFS.Items) > 1 and TFS.Appartment == 1:
        a = random.randint(1, 25)
        b = random.randint(1, 25)
        if a == b:
            StolenItem = random.choice(TFS.Items)
            TFS.Items.remove(StolenItem)
            if StolenItem == 'RF':
                print("Your refrigerator got stolen")
            if StolenItem == 'F':
                print("Your freezer got stolen")
            if StolenItem == 'S':
                print("Your stove got stolen")
            if StolenItem == 'CTV':
                print("Your color TV got stolen")
            if StolenItem == 'VRC':
                print("Your VRC got stolen")
            if StolenItem == 'ST':
                print("Your Stereo got stolen")
            if StolenItem == 'MW':
                print("Your microwave got stolen")
            if StolenItem == 'HT':
                print("Your hot tub got stolen")
            if StolenItem == 'PC':
                print("Your computer got stolen")


def CheckIfStarving():
    if TFS.Food > 0:
        TFS.StarvingForDays = 0
    if TFS.Food < 1:
        print("You are starving you should buy food")
        TFS.StarvingForDays += 1
    if TFS.StarvingForDays == 28:
        print("You have been starving for a month")
        print("You will die soon")
    if TFS.StarvingForDays > 28 + random.randint(1, 3):
        print("You died")
        RestartProgram()


def RestartProgram():
    TFS.Inheratence = random.randint(0, int(TFS.Money))
    TFS.Day = 0
    TFS.Money = 400
    TFS.Food = 1
    TFS.Week = 0
    TFS.TempDays = 0
    TFS.TempWeeks = 0
    TFS.LotteryTickets = 0
    TFS.Enroll = 0
    TFS.Studies = []
    TFS.Items = []
    TFS.ClothingLevel = 1
    TFS.HasStudied = False
    TFS.Wage = 0
    TFS.Job = None
    TFS.Store = None
    TFS.WorkExperience = 0
    TFS.ClothingLevelRequiredForJob = 0
    TFS.DepositedMoney = 0
    TFS.LendedMoney = 0
    TFS.TempWeeks2 = 0
    TFS.Month = 0
    TFS.TempMonths = 0
    TFS.Appartment = 1
    TFS.PayedRent = True
    TFS.RentNeedToBePaid = 0
    TFS.StarvingForDays = 0
    TFS.Sick = False
    TFS.StarvingForDays = 0
