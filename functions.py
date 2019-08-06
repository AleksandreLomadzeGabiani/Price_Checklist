# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 09:01:32 2019

@author: A_Normal_PC
"""

import smtplib, ssl


def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ul (upper left)
    ur = rectangle.getP2()  # assume p2 is lr (lower right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()


def send_email(msg):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "iotagroupmail@gmail.com"  # Enter your address
    receiver_email = "iotagroupmail@gmail.com"  # Enter receiver address
    password = "Aaa"+str(20576*2*3) #NOTE TO EVERYONE this is not secure. DO NOT use an email that you care about being compromised when using this part of the project.  <#input("Type your password and press enter: ")>
    message = msg
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


# =============================================================================
# send_email("""\
# Subject: Hi there
# 
# This message is sent from Python.""")
# =============================================================================
