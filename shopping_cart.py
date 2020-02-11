# shopping_cart.py
# env is shopping-cart-env
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S

import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
# used https://nitratine.net/blog/post/how-to-send-an-email-with-python/

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)

total_price = 0

valid_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "DONE"]
shopping_list_inputs = [] #storing inputs from in list code from https://stackoverflow.com/questions/43141691/storing-user-input-in-a-list-and-writing-a-loop-to-find-a-valid-value-from-that?rq=1
while True:
    # capturing user input and storing in a variable
    user_input = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    # demonstrating ability to recognize what the input was, although you might also want to check its datatype
    #print("YOUR INPUT WAS: " + user_input)
    if user_input not in valid_inputs:
        print("This input is not valid, please try again.")
        user_input = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if user_input == "DONE":
        break
    shopping_list_inputs.append(user_input)

#print("Customer Purchases: ",shopping_list_inputs)

print("--------------------------------")
print("Georgetown Grocery Store")
print("--------------------------------")
print("Web: www.georgetowngrocery.com")
print("Phone: 1.212.387.6890")
print("Checkout Time: ", dt_string) #https://www.programiz.com/python-programming/datetime/current-datetime
print("--------------------------------")
print("Shopping Cart Items:")

for selected_id in shopping_list_inputs:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    print("..." + matching_product["name"] + " " + "${0:.2f}".format(matching_product["price"]))

subtotal_price_usd = "${0:.2f}".format(total_price)

print("--------------------------------")
print("SUBTOTAL: " + str(subtotal_price_usd))
x = float(total_price) #https://stackoverflow.com/questions/379906/how-do-i-parse-a-string-to-a-float-or-int
tax = .06
sales_tax = (x*tax)
print("DC Sales Tax (6%): " + "${0:.2f}".format(sales_tax))
total = x + sales_tax
print("FINAL TOTAL: " + "${0:.2f}".format(total))
print("--------------------------------")
print("Thanks for your business! Please come again!")
print("--------------------------------")

#email option 
valid_inputs1 = ["y", "n"]
user_input1 = input("Would the customer like to be emailed their receipt? [y/n] ")
if user_input1 not in valid_inputs1:
    print("This input is not valid, please try again.")
    user_input1 = input("Would the customer like to be emailed their receipt? [y/n] ")
if user_input1 == "y":
     user_input2 = input("Please enter customer's email address: ")
else: 
    print("No receipt will be emailed.")
    quit()

email = 'georgetowngrocery2@gmail.com' #here are the login credentials for the email that I made for this program
password = 'grocerygtown'
send_to_email = user_input2
subject = "Here is your receipt from Georgetown Grocery!"
message = "Thank you for shopping at Georgetown Grocery. Your total is " + "${0:.2f}".format(total) + " at " + dt_string + "."

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
