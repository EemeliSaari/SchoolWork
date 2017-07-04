# Purpose: learn more about functions


def calculate_dose(weight, previous_dose, whole_dose):
    """
    Calculates Parasetamol medication dose
    :param weight: Patients weight (kg)
    :param previous_dose: how many hours from previous dose (full hours)
    :param whole_dose: dose from the past 24 hours (mg)
    :return: the amount of Parasetamol given to patient
    """

    every_six_hour = int(weight * 15)
    daily = int(every_six_hour * 4)
    maximum = int(4000)

    possible = int(maximum - whole_dose)

    if weight <= 0:
        A = 0
        print("The amount of Parasetamol to give to the patient:",A)

    if previous_dose < 6:
        A = 0
        print("The amount of Parasetamol to give to the patient:",A)

    if whole_dose >= maximum:
        A = 0
        print("The amount of Parasetamol to give to the patient:",A)

    if weight > 0:
        if previous_dose >= 6:
            if whole_dose + every_six_hour > maximum:

                print("The amount of Parasetamol to give to the patient:",
                      possible)

            elif whole_dose < daily:

                print("The amount of Parasetamol to give to the patient:",
                      every_six_hour)


def main():

    input1 = float(input("Patient's weight (kg): "))
    input2 = float(input("How much time has passed from the previous dose (full hours): "))
    input3 = float(input("The total dose for the last 24 hours (mg): "))

    calculate_dose(input1, input2, input3)

main()



