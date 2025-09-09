import ftplib
import json
import io

user = "root"
password = ""
buffer = io.BytesIO()
print("App Center Browser by Kilgorezer")
print("Only tested on LeapPad Platinum.")
print("See README.TXT for details")
ftp = ftplib.FTP(input("Enter LeapPad's Local IP: "))
ftp.login(user, password)

def setData(bina):
    print(json.load(bina))

ftp.cwd("/LF/Bulk/")
ftp.retrbinary('RETR endpointurls.json', buffer.write)
buffer.seek(0)
data = json.load(buffer)
target = "https://u.kilgorezer.com/brow.html"
data["AppCenterHomeButton"]["production"] = target
data["AppCenter"]["production"] = target
buffer.seek(0)

ftp.cwd("/Kilgorezer/")
ftp.storbinary('STOR endpointurls.json', io.BytesIO(json.dumps(data, indent="\t").encode('ascii')))
ftp.quit()
input("Done!")
