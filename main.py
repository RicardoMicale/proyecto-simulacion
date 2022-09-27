from random import randint

STANDARD_BET: int = 10
NUMBER_OF_RUNS: int = 50
STARTING_MONEY: int = 30
GOAL: int = 50
log: dict = {}

def updateBet(oldBet: int, winStatus: bool) -> int:
  '''
  Actualiza la apuesta
  10 si gana, el doble de la anterior si pierde
  '''
  newBet: int = 10 if winStatus else oldBet*2
  return newBet

def updateWinningMonney(winStatus: bool, currentMoney: int, bet: int) -> int:
  '''
  Actualiza el dinero actual
  Se le resta la apuesta al dinero que tenia al hacerla
  '''
  if winStatus: currentMoney += bet
  else: currentMoney -= bet
  return currentMoney

def setResult(runNumber: str, winStatus: bool, betNumber: int, betData: list, runFinished: bool) -> any:
  '''
  Agrega al diccionario de resultados
  Si no se ha hecho la primera apuesta de la corrida, 
  se agrega al diccionario, de lo contrario, se agrega el resultado de la nueva apuesta
  Si se termina la corrida (gana o pierde), se agrega el resultado general de la corrida
  '''
  if runNumber not in log.keys():
    log[runNumber] = {}
  
  if runFinished:
    runResult: tuple = (runNumber, winStatus)
    log[runNumber][betNumber] = betData
    log[runNumber]['result'] = runResult
  else:
    log[runNumber][betNumber] = betData

def run() -> any:
  '''
  Algoritmo principal de la corrida
  '''
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
  '''Determina las proabilidades de ganar'''
  count: int = 0

  for key in log:
    if log[key]['result'][1]:
      count += 1

  return count/len(log)

def winsExpected() -> float:
  '''Determina el valor esperado de las victorias'''
  winProb = winProbability()
  loseProb = 1 - winProb

  return (20 * winProb) + (30 * loseProb)

def statistics() -> any:
  '''Llama las funciones de estadistica'''
  print(f'Probabilidad de ganar: {winProbability()}')
  print(f'Victorias esperadas: {winsExpected()}')

def buildTable() -> any:
  '''Construye la tabla y la agrega al archivo de texto'''
  tableRow: str = ""

  for primaryKey in log:
    tableRow += f'Corrida numero {int(primaryKey) + 1}:\n'
    for secondaryKey in log[primaryKey]:
      if secondaryKey == 'result':
        tableRow += f'''-------\nresultado: {'Apuesta ganada' if log[primaryKey][secondaryKey][1] else 'Apuesta perdida'}\n\n'''
      else:
        tableRow += f'''{log[primaryKey][secondaryKey][0]} {log[primaryKey][secondaryKey][1]} {'Ganador' if log[primaryKey][secondaryKey][2] else 'Perdedor'}\n'''

  with open('tabla.txt', 'w') as table:
    table.write(tableRow)


def main() -> any:
  run()
  statistics()
  buildTable()

main()