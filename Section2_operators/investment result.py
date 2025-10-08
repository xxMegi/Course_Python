capital = 5000
rateOfInterest = 0.08
inflationRate = 0.15

earnedMoney = capital * rateOfInterest
print("Zarobiona kwota: " + str(earnedMoney))

lostMoney = capital * inflationRate
print("Utracona kwota: " + str(lostMoney))

newCapital = capital + earnedMoney - lostMoney
print("Kwota końcowa: " + str(newCapital))