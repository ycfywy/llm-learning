import os
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

import pandas as pd


os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")
os.environ["OPENAI_API_BASE"] = "https://api.chatanywhere.tech/v1"



template = """您是一位专业的鲜花店文案撰写员。
对于售价为 {price} 元的 {flower} ，您能提供一个吸引人的简短描述吗？
{format_instructions}"""

response_schemas = [

    ResponseSchema(name="description",description="描述的结果"),
    ResponseSchema(name="reason",description="为什么文案是这样的")
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

format_instructions = output_parser.get_format_instructions(only_json=False)

prompt = PromptTemplate.from_template(template,
                                      partial_variables={"format_instructions": format_instructions})

# print(prompt)
print(format_instructions)

flowers = ["玫瑰", "百合", "康乃馨"]
prices = ["50", "30", "20"]


model = OpenAI(model='gpt-3.5-turbo-instruct' )



df = pd.DataFrame(columns=['flower','price','description','reason'])

for flower,price in zip(flowers,prices):
    input = prompt.format(price=price,flower=flower)
    output = model.invoke(input=input)
    print(output)
    parsed_output = output_parser.parse(output)
    parsed_output['flower'] = flower
    parsed_output['price'] = price
    print(parsed_output)
    df.loc[len(df)] = parsed_output

print(df)
df.to_csv('output.csv',index=False)




