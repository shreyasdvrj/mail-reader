# Importing libraries
import imaplib
import email
import csv   
import yaml 

def getMail():
    with open("credentials.yml") as f:
        content = f.read()
        
    my_credentials = yaml.load(content, Loader=yaml.FullLoader)
    user, password = my_credentials["user"], my_credentials["password"]


    imap_url = 'imap.gmail.com'
    my_mail = imaplib.IMAP4_SSL(imap_url)
    my_mail.login(user, password)
    my_mail.select('Inbox')

    key = 'FROM'
    value =  my_credentials["from"]
    # _, data = my_mail.search(None, key, value, '(UNSEEN)')  #Filter out for unread emails 
    _, data = my_mail.search(None, key, value)

    mail_id_list = data[0].split() 

    msgs = [] 
    for num in mail_id_list:
        typ, data = my_mail.fetch(num, '(RFC822)')
        msgs.append(data)

    for msg in msgs[::-1]:
        for response_part in msg:
            if type(response_part) is tuple:
                fields = []
                my_msg=email.message_from_bytes((response_part[1]))
                fields.append(my_msg['subject'])
                for part in my_msg.walk():  
                    if part.get_content_type() == 'text/plain':
                        fields.append(part.get_payload())
                with open(r'mail.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
            





