def from_xml():
    with open("phonebook.xml", 'r') as data:
        export_data = data.read()
    export_data = export_data.replace(";"," ")
    export_data += '\n'
    with open("pb.db", 'w') as f:
        f.write(export_data)