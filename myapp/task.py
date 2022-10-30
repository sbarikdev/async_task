from __future__ import absolute_import,unicode_literals
from celery import shared_task
from time import sleep
import os

# @shared_task
# def sleepy(duration):
#     sleep(duration)
#     return None
 
@shared_task
def async_task(save_path, name_of_file):
    sleep(30)
    print('its here')
    completeName = os.path.join(save_path, name_of_file+".html")         
    file1 = open(completeName, "w")
    toFile = 'test data'
    file1.write(toFile)
    file1.close()
    return 'task complete'