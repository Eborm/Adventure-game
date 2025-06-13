from re import T
from Varibles import ThingsFromStart as TFS
import Fuctions as F

# Run all the functions that need to be run when starting a new day


def NewDay():
    F.RandomGetRobbedHome()
    F.PCBitcoinMine()
    F.RandomGetSick()
    F.Lottery()
    F.CheckIfStarving()
    F.CheckifRentPaid()
    if not TFS.PayedRent == False and TFS.PayedRents == False:
        TFS.PayedRents = True
        if TFS.Appartment == 1:
            TFS.RentNeedToBePaid = 325
        if TFS.Appartment == 2:
            TFS.RentNeedToBePaid = 650 
    if not TFS.PayedRent:
        print("You haven't payed rent there will be some money subtracted from your earnings")
    TFS.Day += 1
    TFS.TempDays += 1
    TFS.HasStudied = False
    if TFS.TempDays == 7:
        TFS.Week += 1
        TFS.TempDays = 0
        TFS.TempWeeks += 1
    if TFS.TempWeeks == 1:
        TFS.TempWeeks = 0
        TFS.TempWeeks2 += 1
        TFS.Food -= 1
        F.Intrest()
    if TFS.TempWeeks2 == 4:
        TFS.TempWeeks2 = 0
        TFS.TempMonths = 1
    if TFS.TempMonths == 1:
        F.Rent()
        TFS.Month += 1
        TFS.TempMonths = 0
    print("\nHello " + TFS.Name + " its day " + str(TFS.Day) + ' and its week ' + str(TFS.Week) + ' and its month ' + str(TFS.Month))
