import time
###Linear method
def locate_card_linear(cards,num):
    global time_now
    time_now = time.time()
    for element in range(len(cards)-1):
        if cards[element]==num:
            return element
#print(locate_card_linear([x for x in range(100000000,0,-1)],5))
#end_time=time.time() - time_now
#print(end_time)

#Binary method
def locate_card_binary(cards,num):
    global time_now
    time_now = time.time()
    start,end=0,len(cards)-1
    while start <= end:
        mid = (start + end )// 2
        print(f'start:{start}  end : {end}  mid: {mid}   value: {cards[mid]}')
        if cards[mid] == num:
            return mid
        if cards[mid] > num:
            start = mid+1
        if cards[mid]<num:
            end = mid -1
        # if the provided number is not in list
        if start > len(cards)-1 or end < 0:
            break
       # time.sleep(1)
    return -1
print(locate_card_binary([x for x in range(1000000,0,-1)],5))
print(locate_card_binary([7,5,4,3,2],-64))
print(locate_card_binary([7,5,4,3,2],64))
print(locate_card_binary([],8))
end_time=time.time() - time_now
print(end_time)
