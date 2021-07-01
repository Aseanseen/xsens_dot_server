import sys, json
import pandas as pd

#Read data from stdin, output dataframe
def read_in():
	rows = sys.stdin.readlines()
	arr = []
	for i in range(len(rows)):
		arr.append(rows[i].split())
	df = pd.DataFrame(arr)
	return df

def main():
    #get our data as an array from read_in()
    df = read_in()
    print(df)

# Start process
if __name__ == '__main__':
    main()
