import csv
import sys

csv_file = open("TB_burden_countries_2014-09-29.csv")
total_rows = 0
total_e_prev_num_low_rows = 0
total_e_prev_num_low = 0
total_1990_rows = 0
total_1990 = 0
total_2011 = 0
total_2011_rows = 0
for k in csv.reader(csv_file):
    total_rows+=1
    if(total_rows>1):
        try:
            total_e_prev_num_low+=float(k[11])
            total_e_prev_num_low_rows+=1
        except Exception as e:
            pass
    if(str(k[5])=="1990"):
        try:
            total_1990+=float(k[11])
            total_1990_rows+=1
        except Exception as e:
            pass
    if(str(k[5])=="2011"):
        try:
            total_2011+=float(k[11])
            total_2011_rows+=1
        except Exception as e:
            pass
print("Total Rows - "+str(total_rows))
total_rows_without_index = total_rows-1
print("Estimated prevalence of TB (all forms), low bound with null rows - "+str(total_e_prev_num_low/total_rows))
print("Estimated prevalence of TB (all forms), low bound without null rows - "+str(total_e_prev_num_low/total_e_prev_num_low_rows))
print("Estimated prevalence of TB (all forms), low bound for 1990 - "+str(total_1990/total_1990_rows))
print("Estimated prevalence of TB (all forms), low bound for 2011 - "+str(total_2011/total_2011_rows))

