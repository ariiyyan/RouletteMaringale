import random
totalNumGame = 100
MONEY_INITIAL = 1000
INITIAL_BET = 10
money = MONEY_INITIAL

count = totalNumGame
initialBet = INITIAL_BET
won_count = 0
while money > 0 and count > 0:
    count -= 1
    num = random.randint(0, 36)

    bet_on_odd = random.choice([True, False])

    if (num % 2 == 0 and num != 0 and num != 36 and bet_on_odd is False) or (num % 2 == 0 and num != 0 and num != 36 and bet_on_odd is True):

        money += initialBet
        initialBet = INITIAL_BET
        won_count += 1
    else:
        money -= initialBet
        initialBet *= 2




    print(f" number of roulette is = {num} and total money is = {money} and the bet = {initialBet}")


print(f" {count} many time played happen")
print(f"Number of times won: {won_count}")
print(f" total money left is  =  {money}")