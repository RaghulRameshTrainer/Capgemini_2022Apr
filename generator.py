# def remote_control():
#     yield "cnn"
#     yield "espn"
#     yield "startsport"
#
# # chnl=remote_control()
# # print(next(chnl))
# # print(next(chnl))
# # print(next(chnl))
#
# for channel in remote_control():
#     print(channel.upper())

#0,1,1,2,3,5,8,13,21,34,55.....
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for f in fibonacci():
    if f > 100000000:
        break
    print(f,end=' ')
