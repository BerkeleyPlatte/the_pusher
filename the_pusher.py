from datetime import datetime
import subprocess

today = datetime.today().strftime('%Y-%m-%d')

with open("the_pusher.txt", "w") as update:
    update.write(f'{today}')

subprocess.run("echo 'hello world'", check=True, shell=True)