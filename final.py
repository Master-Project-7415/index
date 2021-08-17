import imaplib
import email
import os

import re
punc='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});') 
  """ cleanr = re.compile('<.*?>') """
  cleantext = re.sub(cleanr, '', raw_html)
  cleantext=cleantext.lower()
  for ele in cleantext:
      if ele in punc:
          cleantext=cleantext.replace(ele,"")
          
  return cleantext
host='smtp.gmail.com'
username='testshrestha78@gmail.com'
password='asmita@123'
mail=imaplib.IMAP4_SSL(host)
mail.login(username,password)
mail.select("inbox")
_,search_data=mail.search(None,'ALL')
my_message=[]
for num in search_data[0].split():
        _,data=mail.fetch(num,'(RFC822)')
        _,b=data[0]
        email_message=email.message_from_bytes(b)
        email_data={}
        for header in ['subject', 'to','from','date']:
            print("{}: {}".format(header,email_message[header]))
            email_data[header]=email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body=part.get_payload(decode=True)
                email_data['body']=body.decode()
            elif part.get_content_type()=="text/html":
                html_body=part.get_payload(decode=True)
                email_data['html_body']=html_body.decode()
                bodyonly = cleanhtml(html_body.decode())
                print(bodyonly.split())
            '''elif part.get_content_type() =="multipart":
              continue
            if part.get('content-disposition') is None:
              continue
            attachment_body=part.get_filename()
            if bool(attachment_body):
              filepath= os.path.join('/Users/fedunibrisbane/Desktop/text/',attachment_body)
              if not os.path.isfile(filepath):
                fp=open(filepath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()'''
        my_message.append(email_data)


                                                    
