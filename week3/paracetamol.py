"""
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
"""

def calculate_dose(w, t, d):
    """functin calculates paracetamol dosage patient can consume"""
    while t < 6:
        return 0
    while (d + w * 15) > 4000:
        return 4000 - d
    return w * 15
    
def main():
    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total_doze_24 = int(input("The total dose for the last 24 hours (mg): "))
    print(f"The amount of Parasetamol to give to the patient: {calculate_dose(weight, time, total_doze_24)}")

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()
