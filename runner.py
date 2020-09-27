import whatsapp

whatsapp.sleeptime = 0.001


message = "100 messages incoming !. This will be very long mesasage\n"
contact = '"Ganesh Kadam"' 
chromedriver_path = "./chromedriver.exe"
whatsapp.chromedriver_path = chromedriver_path
print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
whatsapp.whatsapp_login(chromedriver_path)

def send_message(times = 100):
    global message, contact
    whatsapp.send_message(contact, message= message, times= times)

send_message()