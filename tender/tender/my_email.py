import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from tender.common.consts import const
from tender.utils import date


class Handle_Send_Email(object):
    def __init__(self):
        # 连接SMTP服务器
        self.client = smtplib.SMTP(const.MAIL_HOST)
        # 开启SSL
        self.client.starttls()
        # 登录邮箱
        self.client.login(user=const.SENDER, password=const.MAIL_PASS)

    # 发送邮件
    def send_email(self, address, file_list):
        # 创建邮件对象
        msg = MIMEMultipart()
        # 邮件的主题
        msg['Subject'] = Header("测试邮件", 'utf-8')
        # 定义发送者
        msg['From'] = Header('通知助手')
        # 定义邮件的内容
        content = MIMEText("{}日招标信息".format(date.get_curdate()), 'plain', 'utf-8')
        msg.attach(content)
        for file in file_list:
            part_attach1 = MIMEApplication(open(file, 'rb').read())  # 打开附件
            part_attach1.add_header('Content-Disposition', 'attachment', filename=file)  # 为附件命名
            msg.attach(part_attach1)  # 添加附件
        # 发送邮件
        self.client.sendmail(const.SENDER, address, msg.as_string())
        # 关闭邮件连接
        self.client.close()


