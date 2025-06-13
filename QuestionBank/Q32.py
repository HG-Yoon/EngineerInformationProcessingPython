str = "Sinagong"
n = len(str)  # 8
st = list()
for k in range(n):
    st.append(str[k])   # ["S","i","n","a","g","o","n","g"]
for k in range(n-1, -1, -1):
    print(st[k], end='')  # gnoganiS
