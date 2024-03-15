import pandas as pd
import sys
if __name__=="__main__":
        if len(sys.argv)!=3:
                print("usage:python extract_csv_n_lines.py target.csv number")
                exit(0)
        filename=sys.argv[1]
        extract_lines_number=int(sys.argv[2])
        df = pd.read_csv(filename, nrows=extract_lines_number)
        new_filename=filename.split(".")[0]+"_"+str(extract_lines_number)+".csv"
        df.to_csv(new_filename)
