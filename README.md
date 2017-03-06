# EnpassToKeepass

## Idea
Enpass is nice, however the export format in txt is poorly designed
and makes it hard to export into other tools.
The current structure is similar like:
```
Title : 1st title
username : hello
password: 123456
Title : 2nd title
...
```
## Conversion
This script converts the Enpass Export (txt file) to a Keepass CSV file.
It was tested with Enpass 5.3.0 and Keepass 2.34
At this stage, it only converts the fields "Title", "Username", "Password", "URL"
and the first row of "Notes". Should be easy to enhance this for other fields as well.

Only one parameter has to be set for the folder of the Enpass txt file.
The script will then create a csv file for Keepass in the same directory as the
script was started.

Please make sure that you only have the keywords ("Title", "Username", "Password", "URL"
"Notes") in English.

Use the Keepass Generic CSV Importer for the import.

## Versions
Keepass 2.34
Enpass 5.30
Python 3
