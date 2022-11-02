import time

err_log_path = "D:/TereBin/TtTB/data/err_log.txt"

def err_logging(err):
    with open(err_log_path, 'a') as f:
        err_code = "[" + str(time.strftime('%m/%d %H:%M', time.localtime(time.time()))) + "] " + "req error : \n" + str(err) + "\n\n"
        f.write(err_code)
