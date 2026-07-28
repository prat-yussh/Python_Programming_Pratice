# Q15: Clear Completed Notifications

# Do exactly this:

# Create an independent backup named notification_backup using copy().
# Remove every item from notifications using clear().
# Print both lists.

# Expected output:

# Notifications: []
# Backup: ['Payment received', 'Order shipped', 'Login detected']

# Do not write a loop or create another list manually.

notifications = ["Payment received", "Order shipped", "Login detected"]

notification_backup = notifications.copy()

notifications.clear()

print(notifications)
print(notification_backup)