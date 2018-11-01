import os
os.chdir("C:\\")
f = os.listdir()
for i in f:
    if i != 'Recovery'and i != 'System Volume Information':
        if os.path.isdir("C:\\"+i):
            os.chdir("C:\\"+i)
            if not os.getcwd():
                os.rmdir(os.getcwd())