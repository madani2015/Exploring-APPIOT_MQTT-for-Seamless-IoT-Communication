import threading
import subprocess


def run_device():
    subprocess.call(["python", "device.py"])

def run_multiple(num_threads):
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=run_device)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

run_multiple(10)