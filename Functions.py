
import bcrypt
def password_hash(password):
    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    # print("Bytes ", bytes)
    # print("Salt ", salt)
    # print("Hash ", hash.decode())
    return hash.decode()

#password_hash('nairobi1234')

# $2b$12$N9YW9QGplCLKjkcjk0hExqOO0wNMLeJ1hnS8/nMoOfJh/cb3dwBmKGK
def password_verify(input_password, hash):
    userBytes = input_password.encode()
    result = bcrypt.checkpw(userBytes, hash.encode())
    print("Status ", result)
    return result

#password_verify('nairobi1234', "$2b$12$ilIuoxMgYFmhJeSOAqm7ve1Xk1jLnCqGwWkedetEEFLOxFutubLDe")
# send sms
#username: joe2022
import africastalking
def send_sms(phone, message):
    africastalking.initialize(
        username="joe2022",
        api_key="aab3047eb9ccfb3973f928d4ebdead9e60beb936b4d2838f7725c9cc165f0c8a" 
        # justpaste.it/1nua8
    )
    sms = africastalking.SMS
    recipient = [phone]
    sender = "AFRICASTKNG"
    try:
        response = sms.send(message, recipient)
        print(response)
    except Exception as error:
        print("Execption is ", error)


#send_sms("+254729225710", "Hello Kenya, I Love SMS")
def send_email(receiver_address, mail_content, subject):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    sender_address = 'modcomlearning2@gmail.com'
    sender_pass = '!@#$Mwas@@#2'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

#send_email("modcomlearning@gmail.com","I Love this email", "GREETINGS")
def generate_random():
    # initializing size of string
    import string    
    import random # define the random module  
    S = 10  # number of characters in the string.  
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, 
    k = S))    
    # print("The randomly generated string is : " + str(ran)) # print the random data  
    return str(ran)


#generate_random()
from cryptography.fernet import  Fernet
def write_key():
    key = Fernet.generate_key()
    with open('key.key', "wb") as key_file:
        key_file.write(key)

#write_key()
def load_key():
    return open("key.key", "rb").read()

def encrypt(data):
    key = load_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    print("Before Encr", data)
    print("After Encr ", encrypted_data.decode())
    return encrypted_data.decode()

#encrypt("+254729225710")
#b'gAAAAABjIYV6HGcxidgjeXrvAgmOGFQvGWtOyI-xMW9i1RICxTkahv1G5ABpy352ODFzpd-Y-CsTmOL4GStDDBCesTelea7PPQ=='
def decrypt(data):
    key = load_key()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)
    print("Decrypted ", decrypted_data.decode())
    return decrypted_data.decode()

#decrypt("gAAAAABjIY3vZqXEHBV9DIvizYUfsA6uPxx1pT16_OyopLYIAg4x52wUMwVWhRS2_IgVcQfKKZbWPRWmrcfJ15Nu3zj7rMdwWw==")


import re
def validate_email(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   return False


def passwordValidity(password):
    # define a function to check password strength
    if (len(password) < 8):
        print("inValid Password less than 8")
        return "inValid Password less than 8"

    elif not re.search("[a-z]", password):
        print("inValid Password no small letter")
        return "inValid Password no small letter"

    elif not re.search("[A-Z]", password):
        print("inValid Password no caps")
        return "inValid Password no caps"

    elif not re.search("[0-9]", password):
        print("inValid Password no numbers")
        return "inValid Password no numbers"

    elif not re.search("[_@$]", password):
        print("inValid Password no symbol")
        return "inValid Password no symbol"
    else:
        return True

#print(passwordValidity("jNjkbj334kffdghfdh"))
def check_phone(phone):
    regex = "^\+254\d{9}"
    if not re.match(regex, phone)  or len(phone) !=13:
        return False
    else:
        return True


#print(check_phone("+254729225700"))

