#ask the user to enter the names of three products
product_1 = input("write the product ")
product_2 = input("write the product ")
product_3 = input("write the product ")

#Now ask for the price of each product.
#Each product must have two decimal values
product_price_1 = int(input("price number 1 "))
product_price_2 = int(input("price number 2 "))
product_price_3 = int(input("price number 3 "))
print(product_price_1 + product_price_2 + product_price_3)

#Calculate the average price of the three products. 
# (Hint: you may want to look up round() )
total_price = (product_price_1 + product_price_2 + product_price_3)
print(round(total_price))
average_price = (product_price_1 + product_price_2 + product_price_3) / 3
print(f"The Total of {product_1}, {product_2}, {product_3} is {total_price} and the average price of the items is {average_price}.")
