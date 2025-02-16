import time
import pytz
import datetime as dt
import traceback
from abc import ABC, abstractmethod


class BaseNotification(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def send_message(self, message: str, **kwargs):
        pass

    def noti_job(self, noti_job_name: str):
        def decorator(func):
            def wrapper(*args, **kwargs):
                bkk_now = dt.datetime.now(pytz.timezone("Asia/Bangkok"))
                bkk_now_str = bkk_now.strftime("%Y-%m-%d %H:%M:%S")

                start_time = time.time()
                try:
                    result = func(*args, **kwargs)
                    time_total = time.strftime("%H:%M:%S", time.gmtime(int(time.time() - start_time)))
                    message = f"Job: {noti_job_name} DONE\nStart: {bkk_now_str}\nTime Total: {time_total}"
                    self.send_message(message=message)
                    return result
                except Exception as e:
                    message = f"Job: {noti_job_name} FAILED: {e}\n{traceback.format_exc()}"
                    self.send_message(message=message)
                    raise

            return wrapper

        return decorator
