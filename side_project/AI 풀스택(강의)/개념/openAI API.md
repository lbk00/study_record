> chat 모델을 불러온 후
> 
> 해당 모델에 입력할 template 설정
> 
> 그 후, prompt로 질문을 넘겨준다

chat = ChatOpenAI(
    temperature=0.1 // 창의성 정도
)

template = PromptTemplate.from_template(
    "What is the distance between {country_a} and {country_b}."
)

prompt = template.format(country_a="Mexico",country_b="Thailand")

chat.predict(prompt)
