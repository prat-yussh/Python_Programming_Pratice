# Final Practice: Online Store Checkout
product_price = 2400
quantity = 3
stock_available = 5
coupon_code = "SAVE10"
valid_coupons = ["SAVE10", "WELCOME"]
premium_member = True
tax_percent = 5
delivery_charge = 100
wallet_balance = 7000

# Build a checkout program with these exact requirements.

# 1. Calculate subtotal
subtotal = product_price * quantity

# 2. Check stock
# Store True in stock_available_for_order when the available stock is greater than or equal to the requested quantity.

stock_available_for_order = stock_available >= quantity

# 3. Check coupon
# Store True in coupon_valid when coupon_code is present in valid_coupons.

coupon_valid = coupon_code in valid_coupons

# 4. Decide discount percentage
# Premium member with a valid coupon → 15%
# Non-premium member with a valid coupon → 10%
# Invalid coupon → 0%
# Store the result in approved_discount_percent.
# Use ternary expressions.

approved_discount_percent = 15 if (premium_member and coupon_valid) else 10 if (premium_member == False and coupon_valid) else 0

# 5. Calculate discount amount

discount_amount = subtotal * approved_discount_percent / 100

# 6. Calculate price after discount

discounted_price = subtotal - discount_amount

# 7. Decide delivery charge
# Discounted price is at least 5000 → delivery charge is 0
# Otherwise → delivery charge is 100
# Store it in approved_delivery_charge.

approved_delivery_charge = 0 if discounted_price >=5000 else 100

# 8. Calculate tax

tax_amount = discounted_price * tax_percent / 100

# 9. Calculate final bill

final_bill = discounted_price + approved_delivery_charge + tax_amount

# 10. Check whether the order can be completed
# The order can be completed only when:
# Enough stock AND Wallet balance is greater than or equal to final bill
# Store the Boolean result in order_approved.

order_approved = stock_available_for_order and wallet_balance >= final_bill

# 11. Create order status
# Store:
# "Order Successful"
# when approved, otherwise:
# "Order Failed"
# Use a ternary expression.

order_status = "Order Successful" if order_approved else "Order Failed"

# 12. Update wallet and stock
# When the order is approved:

remaining_wallet = wallet_balance - final_bill if order_approved else wallet_balance
remaining_stock = stock_available - quantity if order_approved else stock_available

# When the order fails, both values must remain unchanged.

# Print these labeled outputs
print("Subtotal:",subtotal)
print("Stock available:",stock_available)
print("Coupon valid:",coupon_valid)
print("Approved discount percent:",approved_discount_percent)
print("Discount amount:",discount_amount)
print("Discounted price:",discounted_price)
print("Delivery charge:",delivery_charge)
print("Tax amount:",tax_amount)
print("Final bill:",final_bill)
print("Order approved:",order_approved)
print("Order status:",order_status)
print("Remaining wallet:",remaining_wallet)
print("Remaining stock:",remaining_stock)