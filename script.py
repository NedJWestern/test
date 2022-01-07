from datetime import datetime
import time

print('foo')
print('bar')


for i in range(60):

    now = str(datetime.now())
    print(now)
    f = open('write_test.txt', 'a')
    f.write(now + '\n')
    f.close()
    time.sleep(1)

    if i==10:
        import pdb; pdb.set_trace()
        print('ilfbags')
        print(1/0)


print('baz')
print('fuz')

# print(1/0)

