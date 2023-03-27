import smtplib
from email.mime.text import MIMEText

# 第三方SMTP服务
mail_host = "smtp.sina.com"             # 设置服务器（smtp.163.com是网易邮箱服务器,smtp.qq.com是QQ地址）
mail_user = "zhxjlbs@sina.com"         # 用户名
mail_pass = "8c162c310feb65c1"        # 密码(注意，这里的密码指的是邮箱客户端授权码)


# 发送者邮箱
sender = "zhxjlbs@sina.com"

# 接收者邮箱
receivers = ['zhxjlbs@163.com', 'cyckun@aliyun.com']                 # 邮件接受者，可设置多个

# 构造正文
message = MIMEText('This is a email test, set by yongchao', 'plain', 'utf-8')       # 构造正文

# 构造发件人
message["From"] = sender                                                 # 发件人，这个必须构造，也可以使用Header来构造

# 收件人列表，这个不是必须的
message["To"] = ";".join(receivers)

# 定义邮件主题
message["Subject"] = "这是主题：SMTP 邮件测试 From yongchao"

try:
    smtpObj = smtplib.SMTP()                                            # 建立和SMTP邮件服务器的连接
    smtpObj.connect(mail_host, 25)                                      # 25 为端口号
    print(" connnect ok")
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('send mail Successfully')
    smtpObj.quit()                                                       # 结束会话
except smtplib.SMTPException as e:
    print(f"发送失败，错误原因：{e}")

