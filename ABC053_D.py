from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="053"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc068_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = [x]
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  from collections import Counter
  N=int(input())
  A=list(map(int,input().split()))
  r=N-len(set(A))
  if r%2==0:
    c=Counter(A)
    tmp1=[]
    tmp2=list(set(A))
    for key in c:
      if c[key]>1:
        for i in range(c[key]-1):
          tmp1.append(key)
    tmp1.sort()
    ans=len(set(A))
    if r==0: print(ans)
    else:
      if r==2:
        flag=1
        for i in range(len(tmp2)):
          if tmp1[0]<=tmp2[i]<=tmp1[-1]: flag=0
      else:
        for i in range(len(tmp2)):
          if tmp1[0]<=tmp2[i]<=tmp1[-2] or tmp1[1]<=tmp2[i]<=tmp1[-1]: flag=0
      print(ans-flag)
  else:
    print(len(set(A))-1)
  """ここから上にコードを記述"""

  print(test_case[__+1])