import datetime as dt

def logdata(result):
    with open('calc.log', 'a') as log:
        log.write(f'{dt.datetime.now()}: {result} \n')
