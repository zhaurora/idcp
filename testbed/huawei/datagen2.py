import os
import os.path 
import time


while True:
    sample  = ["0001,20171202081202,20171202081203,true,23.1234532,35.3321232,91.23,east,200,20321",
        "0001,20171202081203,20171202081204,true,23.1234535,35.3321231,95.43,east,201,20321",
        "0001,20171202081205,20171202081206,true,23.1234537,35.3321236,102.01,east,200,20321",
        "0002,20171202081206,20171202081207,true,23.1234533,35.3321231,105.04,north,232,12342"
       ]


    fileHandle = open('D:\\car_data\\test.log','a')
    
    print (sample)
    
    for i  in range(0,300):
        for r in sample: 
            fileHandle.write(r)
            fileHandle.write('\n')
            print(r)
            
        time.sleep(1)

    fileHandle.close()

        
