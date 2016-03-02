import urllib2
from bs4 import BeautifulSoup
import codecs
import re
def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo() # optional, called by login()
        server_ssl.login(gmail_user, gmail_pwd)  
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
        server_ssl.sendmail(FROM, TO, message)
        #server_ssl.quit()
        server_ssl.close()

        # server = smtplib.SMTP("smtp.gmail.com", 587)
        # server.ehlo()
        # server.starttls()
        # server.login(gmail_user, gmail_pwd)
        # server.sendmail(FROM, TO, message)
        # server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"
        
out_put_file = 'c:\\temp\\modem.txt'
tid_array=[]
try:
    links_file2 = codecs.open(out_put_file, "r", "utf-8")
    content = links_file2.readlines()
    for line in content:
        line=line.encode("ascii","ignore")
        g=re.search(r'&tid=([0-9]+)',line)
        if g:
            tid_array.append(g.group(1))            
    links_file2.close()
except IOError:
    print ""    

mailbody=""
newline="\r\n"
newline=newline.encode('utf-8')

response = urllib2.urlopen("http://www.yeeyi.com/bbs/forum.php?mod=forumdisplay&fid=642&filter=typeid&typeid=758")
soup = BeautifulSoup(response.read(), "html.parser")
aa3 = soup.find_all("a", class_="s xst")
links_file2 = codecs.open(out_put_file, "a", "utf-8")
for alink in aa3:
  s=alink.contents[0]     
  if (s.find(u'\u8def\u7531') >= 0) or (s.find(u'\u732b') >= 0) or (s.find(u'\u006d\u006f\u0064\u0065\u006d') >= 0): 
      tid = alink["href"]
      g=re.search(r'&tid=([0-9]+)',tid)
      if g:
          newtid=g.group(1)
          if newtid not in tid_array:
              tid_array.append(newtid)
              #line = "http://www.yeeyi.com/bbs/forum.php?mod=viewthread&tid=" + newtid + " " + s + "\r\n"
              line = "".join(["http://www.yeeyi.com/bbs/forum.php?mod=viewthread&tid=" + newtid + " ", s, "\r\n"])
              line = line.encode('utf-8') #+ s + newline
              mailbody = mailbody + line
              links_file2.write(line.decode('utf-8'))
                
links_file2.close()

# # consider use important account
if (mailbody != ""):
    send_email('from', 'password', 'to', 'modem', mailbody)




# tables = soup.find_all("table")
# tables = soup.find_all("table", summary="forum_642")
# tbody = soup.find_all("tbody", id="normalthread_3083933")
# all_th = soup.findAll("th", { "class" : "common" })
# at2 = soup.find_all("th", class_="common")
# aa2 = soup.find_all("a", onclick="atarget(this)")
