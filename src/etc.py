import csv

# convert to csv
with open('/home/elad_ch/security_prj/security_project/10-million-password-list-top-1000000.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('10-million-password-list-top-1000000.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)