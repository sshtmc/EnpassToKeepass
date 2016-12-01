#!/usr/bin/env python

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

import sys
import csv
enpass_export_txt = glob.glob("Enpass_20*.txt")

if not enpass_export_txt:
    print('No Enpass exported file found')
    sys.exit(1)

keepass_import_file = open(enpass_export_txt[-1], "r")
print("Opened {}".format(enpass_export_txt[-1]))

fout = 'enpass_to_keepass_import.csv'
with open(fout, 'w') as csvfile:
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
                    if lines[i + checker].startswith('UserName : '):
                        username = lines[i + checker][11:].rstrip()
                    elif lines[i + checker].startswith('Password : '):
                        password = lines[i + checker][11:].rstrip()
                    elif lines[i + checker].startswith('URL : '):
                        url = lines[i + checker][6:].rstrip()
                    elif lines[i + checker].startswith('Note : '):
                        note = lines[i + checker][7:].rstrip()
                    else:
                        note += lines[i + checker].rstrip()
                    checker += 1
		writer.writerow([title, username, password, url, note])

    except(IndexError):
        keepass_import_file.close() # todo - might be incorrect

    finally:
        keepass_import_file.close()

print('Saved output as {}'.format(fout))
