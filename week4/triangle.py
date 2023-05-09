"""
COMP.CS.100 Programming 1
Calculate triangle angles
"""
def calculate_angle(a, b=90):
    """calculates angles of triangle with given angles"""
    c = 180 - a - b
    return c

def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = calculate_angle(a, b)
    print(c)

if __name__ == "__main__":
    main()