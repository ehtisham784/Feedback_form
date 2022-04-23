import smtplib
from email.mime.text import MIMEText #helps to send text in mails

def send_mail(customer,dealer,rating,comments):
    port=2525
    smtp_server='smtp.mailtrap.io' #mail service
    login='439d37ef6cffdc'
    password='cc2385187187c1'
    message=f"<h3>New Feedback Submission</h3>" \
            f"<ul><li>Customer:{customer}</li></ul>" \
            f"<ul><li>Customer:{dealer}</li></ul>" \
            f"<ul><li>Customer:{rating}</li></ul>" \
            f"<ul><li>Customer:{comments}</li></ul>"
    sender_email='ae7166692@gmail.com'
    reciver_email = 'ae7166692@gmail.com'
    msg=MIMEText(message,'html')
    msg['Subject']='Lexus Feedback'
    msg['From']=sender_email
    msg['To'] = reciver_email
    #send email
    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login,password)
        server.sendmail(sender_email,reciver_email,msg.as_string())


