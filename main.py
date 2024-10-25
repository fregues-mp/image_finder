import base

def run():
    c = 0
    while True:

        if base.VI('reset'):
            break

        if not base.EI_Click(r'data\test.png', name='test', move_func=center, value=c):
            c += 1

if __name__ == "__main__":
    try:  
        run()
    finally:
        base.log_file.close()