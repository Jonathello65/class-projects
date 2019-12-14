import requests
import plotly
from plotly.graph_objs import *
import csv
import json
import smtplib
import getpass
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

file = input("Enter path of student list file: ")
table = open(file, "r")
tableReader = csv.reader(table)
tableReader = list(tableReader)
nameI = tableReader[0].index("Name")
addressI = tableReader[0].index("Address")
emailI = tableReader[0].index("Email")

smtpObj = smtplib.SMTP('smtp.dtcc.edu', 587)
smtpObj.ehlo()
smtpObj.starttls()
print("Login to DTCC to send emails.")
username = input("Enter your username: ")
pw = getpass.getpass("Enter your password: ")
smtpObj.login(username + "@dtcc.edu", pw)

fileToSend = "campaignLetter.docx"
districts = []

for i in range(1, len(tableReader)):
    name = tableReader[i][nameI]
    address = tableReader[i][addressI]
    email = tableReader[i][emailI]
    location = requests.get(
        "https://maps.googleapis.com/maps/api/geocode/json?address=" + address
        + "&key=AIzaSyDiBlwdAq7oKKBF3p2QbQT-5JLspbJlXHU")

    locFile = open("location.json", 'wb')
    for chunk in location.iter_content(100000):
        locFile.write(chunk)
    locFile.close()

    locFile = open("location.json", 'r')
    location = locFile.read()
    locFile.close()
    locData = json.loads(location)
    lat = str(locData['results'][0]['geometry']['location']['lat'])
    lng = str(locData['results'][0]['geometry']['location']['lng'])

    legislators = requests.get(
        "https://openstates.org/api/v1/legislators/geo/?lat=" + lat + "&long="
        + lng + "&apikey=dc9da7e7-7b26-4eae-89ec-2aba318eeccb")
    legFile = open("legislator.json", 'wb')
    for chunk in legislators.iter_content(100000):
        legFile.write(chunk)
    legFile.close()

    legFile = open("legislator.json", 'r')
    legislators = legFile.read()
    legFile.close()
    legData = json.loads(legislators)

    msg = MIMEMultipart()
    msg["From"] = username + "@dtcc.edu"
    msg["To"] = email
    msg["Subject"] = "Help fight for Net Neutrality!"

    body = """\
    <html>
        <body>
            <p>Dear """ + name + """,<br>You are receiving this letter
            because Deltech needs your help to fight for Net Neutrality!
            You can help us by contacting your local representatives and
            telling them your stance on the matter. We've attached a letter
            that you can print out, sign, and mail to your representatives.<br><br>
            Please confirm that the address we have for you
            <a href=\"https://www.google.com/maps/place/""" + address + """\">here</a> is correct.
            <br><br>If this is correct, your local representative information is below:<br></p>
    """
    for rep in legData:
        body += ("Name: " + rep['full_name'] + "<br>")
        if rep['email'] != '':
            body += ("Email: " + rep['email'] + "<br>")
        body += ("District: " + rep['district'] + "<br>")
        for dist in districts:
            if dist[0] == rep['district']:
                dist[1] += 1
                break
        else:
            districts.append([rep['district'], 1])
        body += "<br>Offices:<br>"
        for office in rep['offices']:
            if office['name'] != '':
                body += (office['name'] + "<br>")
                body += ("Address: " + str(office['address']) + "<br>")
                body += ("Phone: " + str(office['phone']) + "<br>")
        body += "<br><br>"
    body += """\
            Please help us keep the internet equal for all! Contact your representatives today.
            <br>DTCC
        </body>
    </html>
    """
    body = MIMEText(body, 'html')

    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text":
        fp = open(fileToSend)
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "image":
        fp = open(fileToSend, "rb")
        attachment = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "audio":
        fp = open(fileToSend, "rb")
        attachment = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()

    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)

    msg.attach(body)
    msg.attach(attachment)

    smtpObj.sendmail(msg["From"], msg["To"], msg.as_string())
smtpObj.quit()

districts.sort()

district = []
student = []

for dist in districts:
    district.append(str(dist[0]))
    student.append(dist[1])

district = ["District " + x for x in district]

firstLine = Pie(
    labels=district,
    values=student,
)

data = Data([firstLine])

graphLayout = Layout(
    title='Students per District',
)

fig = Figure(data=data, layout=graphLayout)

plotly.offline.plot(fig, filename='districts.html')
