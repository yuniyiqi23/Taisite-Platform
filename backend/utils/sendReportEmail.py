#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_report_email(username, password, mail_namelist, title, content, attachment_name='attachment',
                      attachment_content=None):
    try:
        msg = MIMEMultipart()
        msg['from'] = username
        msg['to'] = ";".join(mail_namelist)
        msg['subject'] = title
        txt = MIMEText(content, 'html', 'utf-8')
        msg.attach(txt)

        if attachment_name and attachment_content:
            # 添加附件
            part = MIMEApplication(attachment_content)
            # part = MIMEApplication(open(attachment, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=
                            attachment_name)
            msg.attach(part)

        # 设置服务器、端口
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 登录邮箱
        s.login(username, password)
        # 发送邮件
        s.sendmail(username, mail_namelist, msg.as_string())
        s.quit()
        print("email successfully send")
        return True
    except smtplib.SMTPException as e:
        print("send email failed : %s" % e)
        return False
    except BaseException as e:
        print("BaseException: %s" % e)
        return False


if __name__ == '__main__':
    pass




