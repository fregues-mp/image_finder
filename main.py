import base

def run():
    c = 0
    while True:

        if base.VI('reset'):
            break

        if not base.PN(r'data\test.png', name='test', value=c):
            c += 1

if __name__ == "__main__":
    try:  
        run()
    finally:
        base.log_file.close()