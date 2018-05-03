from apscheduler.schedulers.blocking import BlockingScheduler
from gmail import GMail, Message

sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=10)
def timed_job():
    gmail = GMail(username="20166635@student.hust.edu.vn",password="quy.dc20166635")
    msg = Message("hello Hoa", to="duchoapc99@gmail.com", text = "Hello world")
    gmail.send(msg)
    print("Sent")
    # print('This job is run every three minutes.')


sched.start()
