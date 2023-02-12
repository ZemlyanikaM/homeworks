import ui
import core
def find_entry(surename):
    with open('pb.db','r') as pbdb:
        data = pbdb
        enty_consist = False
        for line in data:
            if line.split()[0] == surename:
                enty_consist = True
                return line
        if enty_consist == False:
            return  f'There are no any entry about {surename}'