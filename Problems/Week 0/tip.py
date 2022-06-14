def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Change dollar amount to float
    without_sign = d.replace("$", "")
    d_converted = float(without_sign)
    return d_converted


def percent_to_float(p):
    #remove percent
    without_percent = p.replace("%", "")
    p_converted = float(without_percent) / 100
    return p_converted


main()