
import yagmail

try:
    yag = yagmail.SMTP('prathmesh.soni112@gmail.com', 'cobykuwsrpnjbzqw')
    print("SMTP connection successful!")
    yag.send(to='prathmesh.soni51@gmail.com', subject='Test Email', contents='Hello from yagmail!')
    yag.close()
except Exception as e:
    print(f"SMTP Error: {e}")