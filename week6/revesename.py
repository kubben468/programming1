"""
COMP.CS.100 Programming 1
Reverse names
"""

def reverse_name(name):
    """gets name as a input"""
    
    if "," not in name:
        return name
    else:
        fields = name.split(",")
        firstName = fields[1].strip()
        lastName = fields[0].strip()
        
        fullName = firstName + " " + lastName
        
        if (len(firstName) == 0) or (len(lastName) == 0):
            return firstName + lastName
        
        return fullName
    

def main():
    
    print(reverse_name("Techie, Teddy"))
    
if __name__ == "__main__":
    main()