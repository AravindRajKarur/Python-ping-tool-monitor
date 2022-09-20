import os
import csv
import smtplib as smtp

smtp_server = "smtp.gmail.com"
port = 465  
sender_email = "Your E-Mail Address"
receiver_email = "Your E-Mail Address"
password = "Your E-Mail Password"   #If it is gmail app passsword recommended

with open('ip.csv', 'r') as ip:
    reader = csv.reader(ip)
    for row in reader:
        response = os.system("ping -c 1 " + row[1])
        print(response)
        if response == 0:
            print(row[0], 'is up!')
        else:
            message = row[0]+" is down!"
            print(row[0], 'is down!')
            
            connection = smtp.SMTP_SSL(smtp_server, port)
            connection.login(sender_email, password)
            connection.sendmail(sender_email, receiver_email, message)
            connection.close()
