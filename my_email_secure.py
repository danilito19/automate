import smtplib
from email.mime.text import MIMEText
import weather
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

forecast = weather.get_weather_forecast()

msg = MIMEMultipart()
my_email = "MY EMAIL"
pwd = "PWD"

msg['Subject'] = 'BUENOS DIAS'
body = """
CLASSES TODAY
http://chaturangafitness.com/apps/mindbody/list-schedule

""" + forecast

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP("smtp.live.com",587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(my_email, pwd)

server.sendmail(my_email, my_email, msg.as_string())
server.quit()

