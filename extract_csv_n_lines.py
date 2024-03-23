import pandas as pd
import sys

"""
在读取 CSV 文件的过程中，Pandas 会尝试根据数据的内容来推断每列的数据类型，并可能根据这些推断进行一些格式化。这可能导致读取后的数据与原始 CSV 文件中的数据在格式上有所差异。
可使用dtype_dict来将数据完整的设置为对应的格式。
import pandas as pd  
dtype_dict = {'column1': str, 'column2': str, 'column3': str}  
df = pd.read_csv('your_file.csv', dtype=dtype_dict)
"""

if __name__=="__main__":
        if len(sys.argv)!=3:
                print("usage:python extract_csv_n_lines.py target.csv number/num1-num2")
                exit(0)
        filename=sys.argv[1]
        if "-" in str(sys.argv[2]):
        # 提取num1-num2行(除去表头，包含num1和num2）
            start_num,end_num=sys.argv[2].split("-")
            start_num=int(start_num)
            end_num=int(end_num)
            df = pd.read_csv(filename,skiprows=range(1,start_num),nrows=end_num-start_num+1)
            new_filename=filename.split(".")[0]+"_"+str(start_num)+"-"+str(end_num)+".csv"
        else:
        # 提取前number行
            extract_lines_number=int(sys.argv[2])
            df = pd.read_csv(filename, nrows=extract_lines_number)
            new_filename=filename.split(".")[0]+"_"+str(extract_lines_number)+".csv"
        df.to_csv(new_filename)
