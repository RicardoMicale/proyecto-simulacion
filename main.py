from random import randint

STANDARD_BET: int = 10
NUMBER_OF_RUNS: int = 50
STARTING_MONEY: int = 30
GOAL: int = 50
log: dict = {}

def updateBet(oldBet: int, winStatus: bool) -> int:
  newBet: int = 10 if winStatus else oldBet*2
  return newBet

def updateWinningMonney(winStatus: bool, currentMoney: int, bet: int) -> int:
  if winStatus: currentMoney += bet
  else: currentMoney -= bet
  return currentMoney

def setResult(runNumber: str, winStatus: bool, betNumber: int, betData: list, runFinished: bool) -> any:
  if runNumber not in log.keys():
    log[runNumber] = {}
  
  if runFinished:
    runResult: tuple = (runNumber, winStatus)
    log[runNumber][betNumber] = betData
    log[runNumber]['result'] = runResult
  else:
    log[runNumber][betNumber] = betData

def run() -> any:
  #starting variables
  bet: int = STANDARD_BET
  currentMoney: int = STARTING_MONEY
  runNumber: int = 0
  winStatus: bool = False
  betNumber: int = 1

  while runNumber != NUMBER_OF_RUNS:
    #bet update
    winStatus = True if randint(0, 1) >= 0.5 else False

    #values from this bet
    betData: tuple = (currentMoney, bet, winStatus)

    #money update
    currentMoney = updateWinningMonney(winStatus, currentMoney, bet)
    bet = updateBet(bet, winStatus)

    #winning conditions
    if currentMoney <= 0 or currentMoney >= GOAL:
      setResult(str(runNumber), winStatus, betNumber, betData, True)
      runNumber += 1
      bet: int = STANDARD_BET
      currentMoney: int = STARTING_MONEY
      betNumber = 1
    else:
      setResult(str(runNumber), winStatus, betNumber, betData, False)
      betNumber += 1

  # print(log)

def winProbability() -> float:
  count: int = 0

  for key in log:
    if log[key]['result'][1]:
      count += 1

  return count/len(log)

def winsExpected() -> float:
  winProb = winProbability()
  loseProb = 1 - winProb

  return (20 * winProb) + (30 * loseProb)

def statistics() -> any:
  print(winProbability())
  print(winsExpected())

def buildTable() -> any:
  tableRow: str = 'Corrida Numero    Dinero total     Apuesta     Resultado\n'
  for primaryKey in log:
    tableRow += f'{primaryKey}:\n'
    for secondaryKey in log[primaryKey]:
      if secondaryKey == 'result':
        tableRow += f'''        -------\n        Corrida numero: {log[primaryKey][secondaryKey][0]}, resultado: {'Apuesta ganada' if log[primaryKey][secondaryKey][1] else 'Apuesta perdida'}\n\n'''
      else:
        tableRow += f'''        {log[primaryKey][secondaryKey][0]} {log[primaryKey][secondaryKey][1]} {'Ganador' if log[primaryKey][secondaryKey][2] else 'Perdedor'}\n'''

  print(tableRow)

  with open('tabla.txt', 'w') as table:
    table.write(tableRow)

run()
statistics()
buildTable()