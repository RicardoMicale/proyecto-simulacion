from random import randint

STANDARD_BET: int = 10
NUMBER_OF_RUNS: int = 5
STARTING_MONEY: int = 30
GOAL: int = 50

def updateBet(oldBet: int, winStatus: bool) -> int:
  newBet: int = oldBet if winStatus else oldBet*2
  return newBet

def updateWinningMonney(winStatus: bool, currentMoney: int, bet: int) -> int:
  if winStatus: currentMoney += bet
  else: currentMoney -= bet
  return currentMoney

def run() -> any:
  #starting variables
  bet: int = STANDARD_BET
  currentMoney: int = STARTING_MONEY
  runNumber: int = 0
  winStatus: bool = False
  log: list = []

  while runNumber != NUMBER_OF_RUNS:
    #bet update
    if randint(0, 1) >= 0.5:
      winStatus = True
      bet = updateBet(bet, winStatus)
    else:
      winStatus = False
      bet = updateBet(bet, winStatus)
    
    #money update
    currentMoney = updateWinningMonney(winStatus, currentMoney, bet)
    print(currentMoney)
    #winning conditions
    if currentMoney <= 0:
      runNumber += 1
      runResult = (runNumber, winStatus)
      log.append(runResult)
      bet: int = STANDARD_BET
      currentMoney: int = STARTING_MONEY
    elif currentMoney >= GOAL:
      runNumber += 1
      runResult = (runNumber, winStatus)
      log.append(runResult)
      bet: int = STANDARD_BET
      currentMoney: int = STARTING_MONEY

  print(log)

run()