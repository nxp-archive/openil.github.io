n [1]: from email import encoders

In [2]: from email.header import Header

In [3]: from email.mime.text import MIMEText

In [4]: from email.utils import parseaddr, formataddr

In [5]: import smtplib

In [6]: def _format_addr(s):
   ...:      name, addr = parseaddr(s)
   ...:      return formataddr(( \
   ...:          Header(name, 'utf-8').encode(), \
   ...:          addr.encode('utf-8') if isinstance(addr, unicode) else addr))
   ...: 

In [7]: from_addr = '1329199881@qq.com'

In [8]: password = 'zntnccubswfvijfd'

In [9]: to_addr = 'jinpeng8@staff.sina.com.cn'

In [10]: smtp_server = 'smtp.qq.com'

In [11]: msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

In [12]: msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)

In [13]: msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)

In [14]: msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

In [15]: server = smtplib.SMTP(smtp_server, 465)


^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-15-95b88ea2ff75> in <module>()
----> 1 server = smtplib.SMTP(smtp_server, 465)

/usr/lib/python2.7/smtplib.py in __init__(self, host, port, local_hostname, timeout)
    254         self.esmtp_features = {}
    255         if host:
--> 256             (code, msg) = self.connect(host, port)
    257             if code != 220:
    258                 raise SMTPConnectError(code, msg)

/usr/lib/python2.7/smtplib.py in connect(self, host, port)
    315             print>>stderr, 'connect:', (host, port)
    316         self.sock = self._get_socket(host, port, self.timeout)
--> 317         (code, msg) = self.getreply()
    318         if self.debuglevel > 0:
    319             print>>stderr, "connect:", msg

/usr/lib/python2.7/smtplib.py in getreply(self)
    359         while 1:
    360             try:
--> 361                 line = self.file.readline(_MAXLINE + 1)
    362             except socket.error as e:
    363                 self.close()

/usr/lib/python2.7/socket.pyc in readline(self, size)
    478             while True:
    479                 try:
--> 480                     data = self._sock.recv(self._rbufsize)
    481                 except error, e:
    482                     if e.args[0] == EINTR:

KeyboardInterrupt: 

In [16]: server = smtplib.SMTP(smtp_server, 465, timeout=2)
---------------------------------------------------------------------------
SMTPServerDisconnected                    Traceback (most recent call last)
<ipython-input-16-956b0c772563> in <module>()
----> 1 server = smtplib.SMTP(smtp_server, 465, timeout=2)

/usr/lib/python2.7/smtplib.py in __init__(self, host, port, local_hostname, timeout)
    254         self.esmtp_features = {}
    255         if host:
--> 256             (code, msg) = self.connect(host, port)
    257             if code != 220:
    258                 raise SMTPConnectError(code, msg)

/usr/lib/python2.7/smtplib.py in connect(self, host, port)
    315             print>>stderr, 'connect:', (host, port)
    316         self.sock = self._get_socket(host, port, self.timeout)
--> 317         (code, msg) = self.getreply()
    318         if self.debuglevel > 0:
    319             print>>stderr, "connect:", msg

/usr/lib/python2.7/smtplib.py in getreply(self)
    363                 self.close()
    364                 raise SMTPServerDisconnected("Connection unexpectedly closed: "
--> 365                                              + str(e))
    366             if line == '':
    367                 self.close()

SMTPServerDisconnected: Connection unexpectedly closed: timed out


In [17]: server = smtplib.SMTP(smtp_server, 587, timeout=2)

In [18]: server.set_debuglevel(1)

In [19]: server.login(from_addr, password)
send: 'ehlo [127.0.1.1]\r\n'
reply: '250-smtp.qq.com\r\n'
reply: '250-PIPELINING\r\n'
reply: '250-SIZE 73400320\r\n'
reply: '250-STARTTLS\r\n'
reply: '250-AUTH LOGIN PLAIN\r\n'
reply: '250-AUTH=LOGIN\r\n'
reply: '250-MAILCOMPRESS\r\n'
reply: '250 8BITMIME\r\n'
reply: retcode (250); Msg: smtp.qq.com
PIPELINING
SIZE 73400320
STARTTLS
AUTH LOGIN PLAIN
AUTH=LOGIN
MAILCOMPRESS
8BITMIME
send: 'AUTH PLAIN ADEzMjkxOTk4ODFAcXEuY29tAHpudG5jY3Vic3dmdmlqZmQ=\r\n'
reply: '530 Must issue a STARTTLS command first.\r\n'
reply: retcode (530); Msg: Must issue a STARTTLS command first.
---------------------------------------------------------------------------
SMTPAuthenticationError                   Traceback (most recent call last)
<ipython-input-19-22f2d9e81137> in <module>()
----> 1 server.login(from_addr, password)

/usr/lib/python2.7/smtplib.py in login(self, user, password)
    620             # 235 == 'Authentication successful'
    621             # 503 == 'Error: already authenticated'
--> 622             raise SMTPAuthenticationError(code, resp)
    623         return (code, resp)
    624 

SMTPAuthenticationError: (530, 'Must issue a STARTTLS command first.')






















In [20]: password = 'vwpubzxsmkungfii'



























































In [21]: server.login(from_addr, password)
send: 'AUTH PLAIN ADEzMjkxOTk4ODFAcXEuY29tAHZ3cHVienhzbWt1bmdmaWk=\r\n'
reply: '530 Must issue a STARTTLS command first.\r\n'
reply: retcode (530); Msg: Must issue a STARTTLS command first.
---------------------------------------------------------------------------
SMTPAuthenticationError                   Traceback (most recent call last)
<ipython-input-21-22f2d9e81137> in <module>()
----> 1 server.login(from_addr, password)

/usr/lib/python2.7/smtplib.py in login(self, user, password)
    620             # 235 == 'Authentication successful'
    621             # 503 == 'Error: already authenticated'
--> 622             raise SMTPAuthenticationError(code, resp)
    623         return (code, resp)
    624 

SMTPAuthenticationError: (530, 'Must issue a STARTTLS command first.')

In [22]: server = smtplib.SMTP(smtp_server, 587, timeout=2)

In [23]: server.set_debuglevel(1)

In [24]: server.login(from_addr, password)
send: 'ehlo [127.0.1.1]\r\n'
reply: '250-smtp.qq.com\r\n'
reply: '250-PIPELINING\r\n'
reply: '250-SIZE 73400320\r\n'
reply: '250-STARTTLS\r\n'
reply: '250-AUTH LOGIN PLAIN\r\n'
reply: '250-AUTH=LOGIN\r\n'
reply: '250-MAILCOMPRESS\r\n'
reply: '250 8BITMIME\r\n'
reply: retcode (250); Msg: smtp.qq.com
PIPELINING
SIZE 73400320
STARTTLS
AUTH LOGIN PLAIN
AUTH=LOGIN
MAILCOMPRESS
8BITMIME
send: 'AUTH PLAIN ADEzMjkxOTk4ODFAcXEuY29tAHZ3cHVienhzbWt1bmdmaWk=\r\n'
reply: '530 Must issue a STARTTLS command first.\r\n'
reply: retcode (530); Msg: Must issue a STARTTLS command first.
---------------------------------------------------------------------------
SMTPAuthenticationError                   Traceback (most recent call last)
<ipython-input-24-22f2d9e81137> in <module>()
----> 1 server.login(from_addr, password)

/usr/lib/python2.7/smtplib.py in login(self, user, password)
    620             # 235 == 'Authentication successful'
    621             # 503 == 'Error: already authenticated'
--> 622             raise SMTPAuthenticationError(code, resp)
    623         return (code, resp)
    624 

SMTPAuthenticationError: (530, 'Must issue a STARTTLS command first.')




In [25]: server = smtplib.SMTP_SSL(smtp_server, 465, timeout=2)

In [26]: server.login(from_addr, password)
Out[26]: (235, 'Authentication successful')

In [27]: server.sendmail(from_addr, [to_addr], msg.as_string())
Out[27]: {}

In [28]: server.quit()
Out[28]: (221, 'Bye')

In [29]:   
