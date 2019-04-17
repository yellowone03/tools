#coding: utf-8    
  
import smtplib    
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage 
from email.header import Header   

def send_warning_email():
    smtpserver = ''
    username = ''
    password=''
    sender=''
    receiver=['', '']
    
    subject = 'SSO连续访问故障！'
    
    msg = MIMEMultipart('mixed') 
    msg['Subject'] = subject
    msg['From'] = 'huangyi03 <yellowoneyellow@163.com>'
    #收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
    msg['To'] = ";".join(receiver) 
    
    text = "sso节点连续5次出现访问错误！\n\n近1小时ldap服务器访问情况见附件。\n"
    text_plain = MIMEText(text,'plain', 'utf-8')    
    msg.attach(text_plain)    
    
    sendfile=open(r'/home/web_server/huangyi/es_ssoAndldap_status.txt','rb').read()
    text_att = MIMEText(sendfile, 'base64', 'utf-8') 
    text_att["Content-Type"] = 'application/octet-stream'  
    text_att.add_header('Content-Disposition', 'attachment', filename='ldap_status_1hour.txt')
    msg.attach(text_att)
       
    #发送邮件
    smtp = smtplib.SMTP()    
    smtp.connect('smtp.163.com')
    #smtp.set_debuglevel(1)  
    smtp.login(username, password)    
    smtp.sendmail(sender, receiver, msg.as_string())    
    smtp.quit()


if __name__ == '__main__':
    send_warning_email()
