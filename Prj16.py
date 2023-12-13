import pywhatkit

# Phone number of the recipient (with country code)
# recipient_phone_number = input("Enter phone number: ") # Replace with the recipient's actual phone number
recipient_phone_number = "+918651277913"
# Message content
# message = input("Enter message: ")
message = "hello nalley1.0"

# Specify the time at which the message should be sent (24-hour format)
hour = int(input("hour(24): ")) 
i_minute = int(input("minute(60): "))
times = int(input("No. of times want to send: "))

try:
    # Send the WhatsApp message at the specified time
    for i in range(times):
        if i_minute==60:
            i_minute = i + 1
            minute = i + 1
        else:
            minute = i_minute + i + 1
        pywhatkit.sendwhatmsg(recipient_phone_number, message, hour, minute)
        
    print("Message sent successfully!")

except Exception as e:
    print("An error occurred:", str(e))
