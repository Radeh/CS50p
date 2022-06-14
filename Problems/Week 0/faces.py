def main():
    # Get user input
    toconvert = input("Input? ")

    # Print result
    print(convert(toconvert))

def convert(string):
    # Replace emoticons for emojis
    return string.replace(":)", "🙂").replace(":(", "🙁")

main()