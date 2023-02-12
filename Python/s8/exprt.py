def to_xml():
    with open("pb.db", 'r') as data:
        export_data = data.read()
    export_data = export_data.replace(" ", ";")
    with open("phonebook.xml", 'w') as f_xml:
        f_xml.write(export_data)


def to_html():
    with open("pb.db", 'r') as data:
        export_data = data.read()     
        export_data = export_data.replace("\n","<br>")
    with open("html1.pattern", 'r') as h1:
        temp1 = h1.read()
    with open("html2.pattern", 'r') as h2:
        temp2 = h2.read()         
    with open("phoonebook.html", 'a') as e_data:
         e_data.write(temp1)
         e_data.write(export_data)
         e_data.write(temp2)