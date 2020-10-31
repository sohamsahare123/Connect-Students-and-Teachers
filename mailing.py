import email.message as em
import smtplib

def send_mail_password_forgot(TO, EMAIL_ADDRESS, EMAIL_PASSWORD, username, password):

    msgstr = "Username: {} \nTemporary Password: {}".format(username, password)

    msg = em.Message()
    msg['Subject'] = 'Password change request'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(msgstr)

    s = smtplib.SMTP("smtp.outlook.com", 587)
    s.starttls()

    s.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    s.sendmail(EMAIL_ADDRESS, TO, msg.as_string())
    s.quit()

def send_mail_password_changed(TO, EMAIL_ADDRESS, EMAIL_PASSWORD):

    msgstr = "Password Changed"

    msg = em.Message()
    msg['Subject'] = 'Password Changed'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(msgstr)

    s = smtplib.SMTP("smtp.outlook.com", 587)
    s.starttls()

    s.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    s.sendmail(EMAIL_ADDRESS, TO, msg.as_string())
    s.quit()