"""
COMP.CS.100 Programming 1
Reverse names
"""

def create_an_acronym(str):
    """funciton to split input and making acronym"""
    fields = str.split(" ")
    
    acronym = ""
    
    for i in range(len(fields)):
        acronym += fields[i][0]
        i += 1
    
    return acronym.upper()
        

def main():
    
    print(create_an_acronym("central intelligence agency"))
    
if __name__ == "__main__":
    main()