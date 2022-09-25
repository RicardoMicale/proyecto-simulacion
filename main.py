from random import randint

STANDARD_BET: int = 10
NUMBER_OF_RUNS: int = 50
STARTING_MONEY: int = 30
GOAL: int = 50
log: list = []

def updateBet(oldBet: int, winStatus: bool) -> int:
  newBet: int = 10 if winStatus else oldBet*2
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

  while runNumber != NUMBER_OF_RUNS:
    #bet update
    winStatus = True if randint(0, 1) >= 0.5 else False
    
    #money update
    currentMoney = updateWinningMonney(winStatus, currentMoney, bet)
    bet = updateBet(bet, winStatus)
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