import ui


def save_entry(data):
    with open('pb.db', 'a') as pbdb:
        pbdb.write(data)


def show_entryes():
    with open("pb.db", 'r') as pbdb:
        for line in pbdb:
            print(line)
