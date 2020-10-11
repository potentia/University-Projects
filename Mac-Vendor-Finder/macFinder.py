macAddressDic = {}  # Creating an empty dictionary
with open("mac.txt", "r", encoding="utf8") as macAddressFile:  # Using the with statement to open the file.
    # Using readonly("r") with the encoding set to utf8 as this is what the mac address file was written in.
    # We are assigning the file to macAddressFile
    for line in macAddressFile:  # This iterates through every line in macAddressFile setting its value to line
        if line[0:8] in macAddressDic: # Checks current line to see if the first 8 chars are in macAddressDic
            macAddressDic[line[0:8]] = macAddressDic[line[0:8]] + line # Add line to the current value in the dictionary
        else:
            macAddressDic[line[0:8]] = line   # Creates new key with the value line[0:8] and sets the value to line

macSearch = input("What is the first 6 digits of the MAC address(Including :) you would like to search : ")
try:    # Tries to execute code below but if it gets a KeyError it will not print an error but instead our own message
    if macAddressDic[macSearch].count("\n") > 2: # Checking if there are multiple mac addresses
        print("There are multiple results for the first 6 digits of the mac address you entered \nThey are going to "
              "be printed below \n")
        print(macAddressDic[macSearch])  # Prints the value from the key given
    else:
        print("Here is the result: ")
        print(macAddressDic[macSearch])

except KeyError:
    print("That address is not valid!!!")
