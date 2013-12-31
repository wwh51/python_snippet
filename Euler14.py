import time
def get_seq_len(x, dict_Num_SeqLen):
    seq_len = 1
    dict_Tmp={}
    while(x != 1):
        if x in dict_Num_SeqLen:
            seq_len += dict_Num_SeqLen[x]
            break
        else:
            dict_Tmp[x] = seq_len
        if x%2 == 0:
            x = x//2
        else:
            x = x*3+1
        seq_len += 1
    for k,v in dict_Tmp.items():
        dict_Num_SeqLen[k] = seq_len - v
    return seq_len

longest_len = 0
longest_num = 0
dict_Num_SeqLen = {}
time_begin = time.time()
for num in range(3,1000000):
    seq_len = get_seq_len(num, dict_Num_SeqLen)
    if seq_len > longest_len:
        longest_len = seq_len
        longest_num = num

print('The starting number %d produce the seq length %d' %(longest_num, longest_len) )
print('cost time: %f' % (time.time()-time_begin))
