
# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Emily Liang
# exliang@uci.edu
# 79453973

def main():
    n = int(input()) #assume n is a positive int & <= 999
    interface(n)

def interface(n):
	symbol1 = "+-+"
	symbol2 = "+-+-+"
	indent_count = 0
	for i in range(n+1): 
		if i == 0:
			print(symbol1 + "\n" + "| |")
			indent_count += 1
		elif i == n:
			print((indent_count-1) * "  " + symbol1) 
		else:
			print((indent_count-1) * "  " + symbol2 + "\n" + indent_count * "  " + "| |")
			indent_count += 1
        
if __name__ == '__main__':
    main()
