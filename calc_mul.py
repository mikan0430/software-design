#!/usr/bin/python3

import re
                
def calc(A,B):

        #A,Bが整数ではない場合
        if(type(A) == type(1) and type(B) == type(1)):
                try:
                        ai=str(A)
                        bi=str(B)

                        p = re.compile('\d+$')                 #整数のみ受理可能に
                        if p.match(ai) or p.match(bi):
                                a=int(ai)                       #castの型をfloatからintへ
                                b=int(bi)

                        #条件を0<a<b<1000から，1<=a<=999と1<=b<=999へ変更
                                if (1<=a and a<=999) and (1<=b and b<=999):      
                                        valid=True
                                else:
                                        valid=False
                        else:
                                valid=False
                        
                        if valid:
                                ans=a*b
                                return ans
                        else:
                                return -1        
                except:
                        return -1
        else:
                return -1


#変更前
"""        
        p = re.compile('\d+(\.\d+)?')
        if p.match(ai) or p.match(bi):
                a=float(ai)
                b=float(bi)
                if 0<a and a<b and b<1000:
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
"""


                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
