import os
import subprocess
import shlex

# cmd = 'echo "commit-message-tw=blablabla" >> $GITHUB_ENV'
# print(shlex.split(cmd))
print(os.environ['GITHUB_ENV'])
# subprocess.run(cmd,shell=True,env=os.environ)