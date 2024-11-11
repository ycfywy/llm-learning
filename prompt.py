import os
# from openai import OpenAI
os.environ["OPENAI_API_KEY"] = os.environ.get("PAIED_API_KEY")
os.environ["OPENAI_BASE_URL"] = "https://api.chatanywhere.tech/v1"





"""

Prompt using openai api in chat model 


client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

# 获取并打印助手的回复

print(response.choices[0].message.content)



"""


"""

Prompt (Few-Shot) using langchain api in Text model


"""


samples = [
 {
    "flower_type": "玫瑰",
    "occasion": "爱情",
    "ad_copy": "玫瑰，浪漫的象征，是你向心爱的人表达爱意的最佳选择。"
  },
  {
    "flower_type": "康乃馨",
    "occasion": "母亲节",
    "ad_copy": "康乃馨代表着母爱的纯洁与伟大，是母亲节赠送给母亲的完美礼物。"
  },
  {
    "flower_type": "百合",
    "occasion": "庆祝",
    "ad_copy": "百合象征着纯洁与高雅，是你庆祝特殊时刻的理想选择。"
  },
  {
    "flower_type": "向日葵",
    "occasion": "鼓励",
    "ad_copy": "向日葵象征着坚韧和乐观，是你鼓励亲朋好友的最好方式。"
  }

]

from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

template = "鲜花类型:{flower_type}\n场合:{occasion}\n文案:{ad_copy}"

prompt_template = PromptTemplate(template=template,input_variables=["flower_type","occasion","ad_copy"])

print(prompt_template.format(**samples[0]))

from langchain.prompts.few_shot import FewShotPromptTemplate

prompt = FewShotPromptTemplate(

    examples=samples,
    example_prompt=prompt_template,
    suffix="鲜花类型:{flower_type}\n场合:{occasion}",
    input_variables=["flower_type", "occasion"]
)

print(prompt.format(flower_type="野玫瑰", occasion="爱情"))


model = OpenAI(model="gpt-3.5-turbo-instruct")
result = model.invoke(input =  prompt.format(flower_type="野玫瑰", occasion="爱情"))
print(result)

"""
  Q: Roger has 5 tennis balls. He buys 2 more cans of
  tennis balls. Each can has 3 tennis balls. How many
  tennis balls does he have now?

  A: The answer is 11.

  Q: The cafeteria had 23 apples. If they used 20 to
  make lunch and bought 6 more, how many apples
  do they have?


 Q: Roger has 5 tennis balls. He buys 2 more cans of
 tennis balls. Each can has 3 tennis balls. How many
 tennis balls does he have now?

 A: Roger started with 5 balls. 2 cans of 3 tennis balls
 each is 6 tennis balls. 5 + 6 = 11. The answer is 11.

 Q: The cafeteria had 23 apples. If they used 20 to
 make lunch and bought 6 more, how many apples
 do they have?



"""