from datetime import datetime
import subprocess
from imports import insert

today = datetime.today().strftime('%Y-%m-%d')

with open('the_pusher.txt', 'w') as update:
    update.write(f'{today}')

subprocess.run(
    [
        'cd workspace',
        'cd the_pusher',
        'git add .',
        'git commit -m "minor changes"',
        'git push origin master',
        f'{insert}'
    ], stdout=subprocess.PIPE,
       stderr=subprocess.STDOUT,
       shell=True
)