# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"H572.00","system":"readv2"},{"code":"N001000","system":"readv2"},{"code":"N001200","system":"readv2"},{"code":"Nyu4500","system":"readv2"},{"code":"105976.0","system":"med"},{"code":"107382.0","system":"med"},{"code":"110174.0","system":"med"},{"code":"17675.0","system":"med"},{"code":"28417.0","system":"med"},{"code":"3670.0","system":"med"},{"code":"44141.0","system":"med"},{"code":"55601.0","system":"med"},{"code":"68277.0","system":"med"},{"code":"71763.0","system":"med"},{"code":"94996.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('systemic-sclerosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["systemic-sclerosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["systemic-sclerosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["systemic-sclerosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
