"""This is an IPv4 Subnetting Calculator inspired by the functionality of
the website I use for my Cybersecurity Networking classes:
https://www.calculator.net/ip-subnet-calculator.html.

Author: Savannah Ciak
Class: CSI-160-01
Assignment: Final Project
Due Date: 11 December 2023

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

import ipaddress  # The backbone of this code, the built-in ipaddress module


# Option 1: Network Address
def net_address(ip_address):
    net_add = ipaddress.IPv4Network(ip_address, strict=False)
    # I had to reach out to Champlain College student, Sierra Blume, for advice about
    # the difference between strict=False and strict=True for the ipaddress module.
    return net_add.network_address  # Simple, built-in module function


# Option 2: Usable Host IP Range
def use_host_range(ip_address):
    host = ipaddress.IPv4Network(ip_address, strict=False)  # This conversion is repeated throughout so that the
    # ipaddress module can keep working correctly with proper input/formatting.
    range_start = host.network_address + 1
    range_end = host.broadcast_address - 1
    # The usable host range is simple the available hosts minus the network address and the broadcast address,
    # which is simple to calculate using addition and subtraction (along with the ipaddress module).
    return range_start, range_end


# Option 3: Broadcast Address
def broad_address(ip_address):
    host = ipaddress.IPv4Network(ip_address, strict=False)
    return host.broadcast_address  # Simple, built-in module function


# Option 4: Total Number of Hosts
def total_hosts(ip_address):
    host = ipaddress.IPv4Network(ip_address, strict=False)
    return host.num_addresses  # Simple, built-in module function


# Option 5: Total Number of Usable Hosts
def total_use_hosts(ip_address):
    host = ipaddress.IPv4Network(ip_address, strict=False)
    return host.num_addresses - 2  # Simple, built-in module function
    # The total number of usable hosts is the total hosts excluding the network and broadcast addresses


# Option 6: Subnet Mask in Dotted Decimal
def sub_dec(ip_address):
    host = ipaddress.IPv4Network(ip_address, strict=False)
    return host.netmask  # Simple, built-in module function


# Option 7: Subnet Mask in Binary
def sub_bin(ip_address):
    host = ipaddress.IPv4Network(ip_address, strict=False)
    bin_mask = bin(int(host.netmask))[2:]  # Uses indexing to remove the "0b" prefix
    format_bin = [bin_mask[i:i + 8] for i in range(0, len(bin_mask), 8)]
    # I received advice from Jess Hansard, UVM Student, for line above.
    # The for loop goes through the binary mask's entire length and splits it up into 8 bit chunks.
    fin_bin = ".".join(format_bin)
    # This re-joins the 8 bit chunks from above together, separated by periods.
    return fin_bin
    # This was the most difficult of the functions to solve
    # because I was determined to get the binary formatted correctly.
    # Documentation is included at the bottom of the code.


# Option 8: Potential Subnets
def pot_sub(ip_address):
    subnets = []
    for sub in ip_address.subnets():
        subnet_info = {'subnet': sub, 'range': f"{sub.network_address + 1} - {sub.broadcast_address - 1}"}
        subnets.append(subnet_info)
    return subnets
    # Second most difficult part of this code because dictionaries were
    # a weakness of mine going into this project.


# Main User Dashboard
def main():
    final_data = {}  # Empty dictionary to store data the user chooses to calculate

    try:
        print("\nWelcome to Savannah's Subnetting Calculator!")
        ip_address = input("Enter the IPv4 address in CIDR notation you wish to work with: ")
        ip_verified = ipaddress.ip_network(ip_address, strict=False)
        while True:  # Prints menu for user
            print("\nIPv4 Subnet Calculator Menu:")  # \n for formatting - creates a blank line.
            print("1. Determine the Network Address")
            print("2. Usable Host IP Range")
            print("3. Broadcast Address")
            print("4. Total Number of Hosts")
            print("5. Total Number of Usable Hosts")
            print("6. Subnet Mask in Dotted Decimal")
            print("7. Subnet Mask in Binary")
            print("8. Print Potential Subnets")
            print("9. See Current Data")
            print("10. Quit")
            print("11. Secret Surprise")

            choice = input("\nChoose what you would like to do with your IPv4 address (1-11): ")
            # Choose an option above and assigns it the variable "choice"

            # The if and elif statements 1-8 call upon functions in the above code and print simple statements.
            if choice == "1":
                opt_one = net_address(ip_verified)
                final_data.update({'Network Address': opt_one})  # Throughout all the options,
                # the code will update the working dictionary of user data
                print("The network address of", ip_address, "is:", opt_one)

            elif choice == "2":
                range_start, range_end = use_host_range(ip_verified)
                final_data.update({'Usable Host IP Range': (range_start, range_end)})
                print("The usable host IP range for", ip_address, "is:", range_start, "to", range_end)

            elif choice == "3":
                opt_three = broad_address(ip_verified)
                final_data.update({'Broadcast Address': opt_three})
                print("The broadcast address for the network in which", ip_address, "is used is:", opt_three)

            elif choice == "4":
                opt_four = total_hosts(ip_verified)
                final_data.update({'Total Number of Hosts': opt_four})
                print("The total number of hosts for the network in which", ip_address, "is used is:", opt_four)

            elif choice == "5":
                opt_five = total_use_hosts(ip_verified)
                final_data.update({'Total Number of Usable Hosts': opt_five})
                print("The total number of USABLE hosts for the network in which", ip_address, "is used is:", opt_five)

            elif choice == "6":
                opt_six = sub_dec(ip_verified)
                final_data.update({'Subnet Mask in Dotted Decimal': opt_six})
                print("The dotted decimal version of the subnet mask is:", opt_six)

            elif choice == "7":
                opt_seven = sub_bin(ip_verified)
                final_data.update({'Subnet Mask in Binary': opt_seven})
                print("The binary version of the subnet mask is:", opt_seven)

            elif choice == "8":
                opt_eight = pot_sub(ip_verified)
                final_data.update({'Potential Subnets': opt_eight})
                print("\nThe following are subnets that you can create with you given IP address's network:")
                for subnet_info in opt_eight:
                    print("Subnet:", subnet_info['subnet'], "--> Range", subnet_info['range'])
                    # For loop for better formatting of the potential subnets

            elif choice == "9":
                # Choice 9 is a Dictionary Iteration
                print("\nYour current data is:")
                for key, value in final_data.items():
                    print(key + ":", value)

            elif choice == "10":
                # Choice 10 breaks the while loop
                print("\nQuitting Program, User Choice.")  # Uses break to stop the while loop, which will end the code.
                break

            elif choice == "11":
                print("https://youtu.be/79-AwFZCKpA?feature=shared")

            else:
                print("Invalid choice. Please enter a number between 1 and 11.")
                # If choice is not 1-4, prints this and the while loop continues.

            # After the user picks options 1-9 or 11, they can end the program by stopping the while loop:
            end_choice = input("\nWould you like to see the main menu again? (y/n): ")
            if end_choice != "y":
                print("Exiting Savannah's Subnetting Calculator. Thank you!")
                break
            else:
                continue

    # Error handling, as covered in class
    except ValueError as e:
        print(f"\nYou've encountered the error: {e}")  # Informs the user of the specific error
        print("Please try to restart the program. Exiting program now.")


main()  # Calls the main dashboard

"""
Works Referenced: 
1. https://www.calculator.net/ip-subnet-calculator.html 
   - The subnetting calculator that inspired mine
2. https://www.youtube.com/watch?v=u0yr9B3nH8c&pp=ygUUZGljdGlvbmFyeSBpbiBweXRob24%3D 
   - I used this to brush up on dictionaries, especially in the main function
3. https://www.youtube.com/watch?v=u0yr9B3nH8c&pp=ygUUZGljdGlvbmFyeSBpbiBweXRob24%3D
   - Choice 9 main function
4. https://youtube.com/playlist?list=PLOocymQm7YWaP7_ji5xp4PrzjrWSywhBf&feature=shared
   - How to use the IP Module
5. https://docs.python.org/3/library/ipaddress.html
   - How to use the IP Module
6. https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
   - Using f-strings throughout the code for clearer syntax 
7. https://www.youtube.com/watch?v=_b0qNXBWnlI 
   - Began ideas for sub_bin function
8. https://stackoverflow.com/questions/32930246/python-for-loops-for-i-in-range0-lenlist-vs-for-i-in-list
   - For loops and slicing with indexing, helped with sub_bin function 
"""
