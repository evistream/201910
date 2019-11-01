import subprocess

def add():
    subprocess.call(['git', 'reset'])
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'status'])


def commit(text=None):
    if text is None:
        text='.'

    subprocess.call(['git', 'commit', '-m', text])