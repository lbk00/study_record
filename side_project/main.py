import streamlit as st
import food_type


main_food = st.container()



with main_food:


   st.write("### 음식추천 ver 1.00")

   option1 = st.selectbox(
   '고기를 좋아하시나요?',
   ('네', '아니요'))

   option2 = st.selectbox(
   '한식을 좋아하시나요?',
   ('네', '아니요'))
   option3 = st.selectbox(
   '자극적인 맛을 선호하시나요?',
   ('네', '아니요'))

   option4 = st.selectbox(
   '지난 일주일간 배달음식을 시켜먹은적이 있나요?',
   ('네', '아니요'))

   option5 = st.selectbox(
   '지금 배고프신가요?',
   ('네', '아니요'))

   submit = st.button("제출")


if submit == True:
   f1,f2,f3,f4,f5 = food_type.cohice_food(option1,option2,option3,option4,option5)
   result = food_type.select_index(f1,f2,f3,f4,f5)

   st.write(result+"!!!!")
