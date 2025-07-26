# This is the data and code given to work with. For more info, refer to the notebook data_structures1.ipynb in this repository.

customer_ids = [101, 102, 103, 104, 105, 106, 103, 102]

# Customer Names
customer_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Charlie', 'Bob']

# Customer Locations:
customer_locations = ('New York', 'California', 'Texas', 'Florida', 'New York', 'Texas', 'Florida', 'California')

# Purchases: dictionary of ID: total amount spent
purchases = {
    101: 250.50,
    102: 100.00,
    103: 340.75,
    104: 80.00,
    105: 150.50,
    106: 300.25
}

# Emails (some duplicates, some invalid)
emails = [
    'alice@gmail.com', 
    'bob@yahoo.com', 
    'charlie@gmail.com', 
    'diana@yahoo.com', 
    'eve@gmail.com', 
    'frank@outlook.com',
    'bob@yahoo.com',
    'invalidemail.com',
    'muniaa2gmailcom'
]





"""
================================================================================
**BELOW ARE THE SOLUTIONS TO THE TASKS**
================================================================================
This script processes customer data for a retail scenario, performing the following tasks:
PART A:
    - Removes duplicate customer IDs, names, and emails using sets.
    - Sorts customer names alphabetically.
    - Filters out invalid email addresses (those missing '@' or '.').
PART B:
    - Identifies unique customer locations from a tuple of locations.
    - Extracts unique email domain providers (e.g., gmail, yahoo, outlook) from the list of valid emails.
PART C:
    - Calculates the total revenue from all customer purchases.
    - Computes the average purchase amount.
    - Determines the customer ID of the highest spender.
PART D:
    - Prints a summary including:
        - Total number of unique customers.
        - Total revenue.
        - Average purchase amount.
        - List of unique customer locations.
        - Set of unique email providers.
"""



# --PART A-- ##
#convert IDs to a set to remove duplicates
unique_customer_ids = set(customer_ids)#convert list to set to remove duplicates
customer_ids = list(unique_customer_ids)#convert back to list frm set
customer_ids

unique_customer_names = set(customer_names)  # convert list to set to remove duplicates
customer_names = list(unique_customer_names)  # convert back to list from set
customer_names.sort()  # sort the names alphabetically
customer_names

unique_emails = set(emails)  # convert list to set to remove duplicates
valid_emails = [email for email in unique_emails if '@' in email and '.' in email]  # filter out invalid emails
emails = list(valid_emails)  # convert back to list from set
emails

## --PART B-- ##
# find unique customer locations
unique_customer_locations = set(customer_locations)  # convert tuple to set to remove duplicates
customer_locations = list(unique_customer_locations)  # convert back to list from set
customer_locations

# using sets to find unique domain providers i.e gmail, yahoo, outlook without the .com part
unique_domains = set(email.split('@')[1].split('.')[0] for email in emails if '@' in email)  # extract unique domains
unique_domains

## --PART C-- ##
# total revenue
total_rev = sum(purchases.values())  # calculate total revenue from purchases

# average purchase amount
average_purchase = total_rev / len(purchases) if purchases else 0  # calculate average purchase amount
average_purchase

# ID of the customer who spent the most
max_spender_id = max(purchases, key=purchases.get) if purchases else None  
max_spender_id

## --PART D-- ##
print(f"Total unique customers: {len(unique_customer_ids)}")
print(f"Total revenue: ${total_rev:.2f}")
print(f"Average purchase amount: ${average_purchase:.2f}")
print(f"Unique locations: {customer_locations}")
print(f"Email providers: {unique_domains}")
