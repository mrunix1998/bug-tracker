import schedule
import time
import os


def send_notify_email():
    os.system('python manage.py f24_create_invoices')
    print("Notify Email Sent.")


if __name__ == '__main__':
    print("Started Scheduled Service ... ")

    # jobs
    schedule.every(1).minute.do(send_notify_email)

    while True:
        schedule.run_pending()
        time.sleep(1)
