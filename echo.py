import os
import subprocess
import shlex
from pathlib import Path

class GithubEnv:
    def __init__(self):
        self.file = Path(os.environ.get('GITHUB_ENV','env.txt'))
    def __setitem__(self, name, value):
        with self.file.open('a') as f:
            f.write(f'{name}={value}\n')

github_env = GithubEnv()
for i in range(3):
    github_env[f"name{i}"] = f'value{i}'