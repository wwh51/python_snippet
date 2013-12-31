
import time
def get_seq_len(x, dict_Num_SeqLen):
    l = 1
    dict_Tmp={}
    while(x != 1):
        if x in dict_Num_SeqLen:
            l += dict_Num_SeqLen[x]
            break
        else:
            dict_Tmp[x] = l
        if x%2 == 0:
            x = x//2
        else:
            x = x*3+1
        l += 1
    for k,v in dict_Tmp.items():
        dict_Num_SeqLen[k] = l - v
    return l

longest_len = 0
longest_num = 0
dict_Num_SeqLen = {}
time_begin = time.time()
for num in range(3,1000000):
    l = get_seq_len(num, dict_Num_SeqLen)
    if l > longest_len:
        longest_len = l
        longest_num = num

print('The starting number %d produce the seq length %d' %(longest_num, longest_len) )
print('cost time: %f' % (time.time()-time_begin))
