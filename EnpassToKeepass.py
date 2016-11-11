'''
This script converts the Enpass txt Export to a Keepass CSV file.
It was tested with Enpass 5.3.0 and Keepass 2.34
At this stage, it only converts the fields "Title", "Username", "Password", "URL"
and the first row of "Notes". In the future, this might be enhanced.

Only one parameter has to be set for the folder of the Enpass txt file.
The script will then create a csv file for Keepass in the same directory as the
script was started.

Please make sure that you only have the keywords ("Title", "Username", "Password", "URL"
"Notes") in English.

Use the Keepass Generic CSV Importer for the import.
'''

import csv

''''
PLEASE CHANGE THIS TXT VALUE TO YOUR TXT FILE
Below an example file name
'''
enpass_export_txt = r"Enpass_2016-11-07_21-31-58.txt"


class KeepassRow:
    ''''
    Returns the Keepass Row for the CSV file.

    '''

    def __init__(self, title, username, password, url, notes):
        self.title = title
        self.username = username
        self.password = password
        self.url = url
        self.notes = notes

    def write_row(self):
        row = ",".join([self.title, self.username, self.password, self.url, self.notes])
        row = row.split(",")
        return row


keepass_import_file = open(enpass_export_txt, "r")

with open('Keepass_Import.csv', 'w') as csvfile:
    try:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["Account", "Login Name", "Password", "Web Site", "Comments"])

        lines = keepass_import_file.read().splitlines()
        for i in range((len(lines))):
            if "Title" in lines[i]:
                title = lines[i][8:].rstrip()
                checker = 1
                username = ""
                password = ""
                url = ""
                note = ""
                while "Title" not in lines[i + checker]:
                    if "username" in lines[i + checker].lower():
                        username = lines[i + checker][11:].rstrip()
                    elif "password" in lines[i + checker].lower():
                        password = lines[i + checker][11:].rstrip()
                    elif "url" in lines[i + checker].lower():
                        url = lines[i + checker][6:].rstrip()
                    elif "Note" in lines[i + checker].lower():
                        note = lines[i + checker][7:].rstrip()
                    checker += 1
                row = KeepassRow(title, username, password, url, note)
                writer.writerow(row.write_row())

    except(IndexError):
        keepass_import_file.close()

    finally:
        keepass_import_file.close()
