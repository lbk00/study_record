Meat = ['보쌈','양념갈비','곱창','삼겹살',           #안자극
        '쭈꾸미볶음','제육','김치찜','찜닭', # 16 #   자극  한식 

        '후라이드 치킨','돈까스','스테이크' ,'부타동',#안자극
        '탕수육','양념치킨','마라탕','햄버거'] #  자극   한식 X


NoMeat = ['부대찌개', '떡볶이&튀김','해물찜', '라면', #안자극
          '된장찌개','김밥','국밥','고등어구이', # 한식
          
            '짬뽕','짜장면','피자', '파스타',     #안자극
            '쌀국수', '토스트','초밥','샐러드']     #한식x

# 1 2 3 4 절반 / 절반  짝수번째 가벼운음식



def cohice_food(op1,op2,op3,op4,op5):
    flag1 =0
    flag2 =0
    flag3 =0
    flag4 =0
    flag5 =0
    if op1 =='네': flag1 = 0
    else: flag1 = 1
    if op2 =="네": flag2 = 0
    else: flag2 = 1
    if op3 =="네": flag3 = 0
    else: flag3 = 1
    if op4 =="네": flag4 = 0
    else: flag4 = 1
    if op5 =="네": flag5 = 0
    else: flag5 = 1

    return flag1 , flag2 , flag3, flag4, flag5


def select_index(f1,f2,f3,f4,f5):
    if f1 == 0: # Meat
        if f2 == 0 and f3 == 1 and f4 == 1 and f5 == 0 : return Meat[0] 
        elif f2 == 0 and f3 == 1 and f4 == 1 and f5 == 1 :return Meat[1]
        elif f2 == 0 and f3 == 1 and f4 == 0 and f5 == 0 :return Meat[2] 
        elif f2 == 0 and f3 == 1 and f4 == 0 and f5 == 1 :return Meat[3] 
        elif f2 == 0 and f3 == 0 and f4 == 1 and f5 == 0 :return Meat[4] 
        elif f2 == 0 and f3 == 0 and f4 == 1 and f5 == 1 :return Meat[5] 
        elif f2 == 0 and f3 == 0 and f4 == 0 and f5 == 0 :return Meat[6] 
        elif f2 == 0 and f3 == 0 and f4 == 0 and f5 == 1 :return Meat[7]

        elif f2 == 1 and f3 == 1 and f4 == 1 and f5 == 0 :return Meat[8] 
        elif f2 == 1 and f3 == 1 and f4 == 1 and f5 == 1 :return Meat[9] 
        elif f2 == 1 and f3 == 1 and f4 == 0 and f5 == 0 :return Meat[10] 
        elif f2 == 1 and f3 == 1 and f4 == 0 and f5 == 1 :return Meat[11] 
        elif f2 == 1 and f3 == 0 and f4 == 1 and f5 == 0 :return Meat[12] 
        elif f2 == 1 and f3 == 0 and f4 == 1 and f5 == 1 :return Meat[13] 
        elif f2 == 1 and f3 == 0 and f4 == 0 and f5 == 0 : return Meat[14] 
        elif f2 == 1 and f3 == 0 and f4 == 0 and f5 == 1 : return Meat[15]  


    else :
        if f2 == 0 and f3 == 1 and f4 == 1 and f5 == 0 :return NoMeat[0] 
        elif f2 == 0 and f3 == 1 and f4 == 1 and f5 == 1 :return NoMeat[1]
        elif f2 == 0 and f3 == 1 and f4 == 0 and f5 == 0 :return NoMeat[2] 
        elif f2 == 0 and f3 == 1 and f4 == 0 and f5 == 1 :return NoMeat[3] 
        elif f2 == 0 and f3 == 0 and f4 == 1 and f5 == 0 :return NoMeat[4] 
        elif f2 == 0 and f3 == 0 and f4 == 1 and f5 == 1 :return NoMeat[5] 
        elif f2 == 0 and f3 == 0 and f4 == 0 and f5 == 0 :return NoMeat[6] 
        elif f2 == 0 and f3 == 0 and f4 == 0 and f5 == 1 : return NoMeat[7]

        elif f2 == 1 and f3 == 1 and f4 == 1 and f5 == 0 :return NoMeat[8] 
        elif f2 == 1 and f3 == 1 and f4 == 1 and f5 == 1 :return NoMeat[9] 
        elif f2 == 1 and f3 == 1 and f4 == 0 and f5 == 0 :return NoMeat[10] 
        elif f2 == 1 and f3 == 1 and f4 == 0 and f5 == 1 :return NoMeat[11] 
        elif f2 == 1 and f3 == 0 and f4 == 1 and f5 == 0 :return NoMeat[12] 
        elif f2 == 1 and f3 == 0 and f4 == 1 and f5 == 1 :return NoMeat[13] 
        elif f2 == 1 and f3 == 0 and f4 == 0 and f5 == 0 : return NoMeat[14] 
        elif f2 == 1 and f3 == 0 and f4 == 0 and f5 == 1 :return NoMeat[15] 
