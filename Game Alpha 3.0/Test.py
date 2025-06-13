import random
import sys
import time
startTime = time.time()

AvarageStolenMoney = 0
TimesRobbed = 0

def RandomGetRobbed():
    import Test
    Money = 400
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    if a == b:
        StolenMoney = random.randint(30, 500)
        while StolenMoney > Money:
            StolenMoney -= 1
        # print("You got robbed and the robber stole " + str(StolenMoney) + " dollars from you")
        Money -= StolenMoney
        Test.AvarageStolenMoney += StolenMoney
        Test.TimesRobbed += 1


for i in range(100000):
    RandomGetRobbed()

print("The average stolen money is " + str(AvarageStolenMoney/TimesRobbed))
print("You got robbed " + str(TimesRobbed) + " times")
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
sys.exit()