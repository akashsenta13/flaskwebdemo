from email.mime.text import MIMEText
import smtplib

def send_email(email,height,avg,count):
    from_email= "php.sprinfot@gail.com"
    from_pwd = "P@sg#90"
    to_email = email
    subject = "Height data"
    message = "Your height is <strong>%s</strong>. Average height of all is %s. That is calculated out of %s people." % (height,avg,count)

    msg = MIMEText(message,'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login(from_email,from_pwd)
    conn.send_message(msg)
    conn.quit()
