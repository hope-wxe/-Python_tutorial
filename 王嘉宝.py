# �ݹ鷽ʽʵ�� ����ǰ20��
lis =[]
for i in range(20):
    if i ==0 or i ==1:#��1,2�� ��Ϊ1
        lis.append(1)
    else:
        lis.append(lis[i-2]+lis[i-1])#�ӵ�3�ʼÿ��ֵΪǰ����ֵ֮��
print(lis)
