import math
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

def calculate_pages(total_tickets, tickets_per_page):
    total_pages = math.ceil(total_tickets / tickets_per_page)
    extra_tickets = total_tickets % tickets_per_page  # Calculate leftover tickets on the last page
    return total_pages, extra_tickets

while True:
    # Get user input
    user_input = input(Fore.YELLOW + "Enter the total number of tickets (or type 'jet' to exit): ")
    if user_input.lower() == "jet":
        print(Fore.RED + "\nExiting the program. Goodbye!")
        break

    try:
        total_tickets = int(user_input)
        tickets_per_page = int(input(Fore.YELLOW + "Enter the number of tickets per page: "))

        # Calculate total pages and extra tickets
        total_pages, extra_tickets = calculate_pages(total_tickets, tickets_per_page)
        
        # Display the result with clear formatting and line separation
        print(Fore.CYAN + "\n--- Ticket Page Calculation ---")
        print(f"{Fore.GREEN}Total tickets: {total_tickets}")
        print(f"{Fore.GREEN}Tickets per page: {tickets_per_page}")
        print(f"{Fore.GREEN}Total pages required: {total_pages}")
        
        if extra_tickets > 0:
            blank_slots = tickets_per_page - extra_tickets
            print(f"{Fore.YELLOW}Page {total_pages} has {extra_tickets} ticket(s) with {blank_slots} empty slot(s).")
        else:
            print(Fore.YELLOW + "All pages are fully filled.")
        print(Fore.CYAN + "--------------------------------\n")  # Clear separator line for each output

    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number for tickets and tickets per page.\n")

