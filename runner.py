import whatsapp
import argparse
whatsapp.sleeptime = 0.001

parser = argparse.ArgumentParser(description='Whatsapp Annoyer Guide')
parser.add_argument('--chrome_driver_path', dest = "chromedriver_path", action='store', type=str, default='./driver/chromedriver.exe', help='chromedriver executable path (MAC and Windows path would be different)')
parser.add_argument('--message', dest = "message",action='store', type=str, default='', help='Enter the msg you want to send')
parser.add_argument('--contact', dest = "contact",action='store', type=str, default='', help='Enter the Contact Name[Exact. Case Sensitive]')
parser.add_argument('--times', dest = "times", action='store', type=int, default=1, help='Enter the no. of time you want to send same message')
args = parser.parse_args()

def ask_questions():
    args.contact = '"' + input("%-50s"%("Enter the contact name [case sensetive] : ")) + '"'
    args.message = input("%-50s"%("Enter the message : "))
    args.times = int(input("%-50s"%("Enter how many time you wanna annoy : ")))
    cpath = input(f"Enter driver path, [default : {args.chromedriver_path}] : ")
    args.chromedriver_path = args.chromedriver_path if cpath == "" else cpath

def send_message(times = 100):
    global message, contact
    whatsapp.send_message(contact, message= message, times= times)

ask_questions()
message = args.message
contact = '"' + (args.contact) + '"' 
chromedriver_path = args.chromedriver_path
whatsapp.chromedriver_path = chromedriver_path
print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
whatsapp.whatsapp_login(chromedriver_path)
send_message(args.times)
input("Press Anything to EXIT")