import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('shreyasdeveloper049@gmail.com','hlru aauq xacv ccmy')
subject = "Test Python"
body="I Love Python"
message = "subject:{}\n\n{}".format(subject, body)
listadd=['shreyaspachpute2002@gmail.com',
         "shreyasdeveloper049@gmail.com"]
ob.sendmail('shreyaspachpute.co20d2@scet.ac.in', listadd, message)
print("send mail")
ob.quit()