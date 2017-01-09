import logging, sys
from smtplib import SMTP

def contact_email(email_dict):
    logging.info("Initializing contact email script")
    logging.info(email_dict)
    logging.info(email_dict['email'])
    sender = 'khannegan@gmail.com'
    receivers = ['kevin@kevinhannegan.net', email_dict['email']]

    message = email_dict['message']
    subject = "Message from " + email_dict['name'] + "to Kevin Hannegan"
    msg = 'Subject: %s\nTo: kevin@kevinhannegan.net\nCC: %s\n\n%s\n\n--\nSent from kevinhannegan.net' % (subject,
    email_dict['email'],message)
    try:
        smtpObj = SMTP('localhost')
        smtpObj.sendmail(sender, receivers, msg)         
        logging.info("Email successful")
        return True
    except:
        logging.info("Error: unable to send email")
        return False

