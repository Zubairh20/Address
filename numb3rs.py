import re


# Initial message
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Sets up format for the addresses
    if re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip):
        total_range = ip.split(".")
        
        # Sets up range for the addresses
        for number in total_range:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()