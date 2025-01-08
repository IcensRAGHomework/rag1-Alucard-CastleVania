import json
import traceback

from model_configurations import get_model_configuration

from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

gpt_chat_version = 'gpt-4o'
gpt_config = get_model_configuration(gpt_chat_version)
#OctQuestion = "2024年台灣10月紀念日有哪些?"
#knowledge_base = [
#        {"input": OctQuestion, "output": "國慶日"},
#        {"input": "Hello world!", "output":  "YOLO!"}
#        ]

#example_prompt = ChatPromptTemplate.from_messages(
#        [
#            ("human", "{input}"),
#            ("ai", "{output}")
#            ]
#        )
#few_shot_prompt = FewShotChatMessagePromptTemplate(
#        example_prompt = example_prompt,
#        examples = knowledge_base
#        )

#print(few_shot_prompt.invoke({}).to_messages())
base_model = AzureChatOpenAI(
        model=gpt_config['model_name'],
        deployment_name=gpt_config['deployment_name'],
        openai_api_key=gpt_config['api_key'],
        openai_api_version=gpt_config['api_version'],
        azure_endpoint=gpt_config['api_base'],
        temperature=gpt_config['temperature']
)

def generate_hw01(question):
    holiday_schema1 = {
            "title": "holiday",
            "description": "Give me some memorial day in taiwan",
            "type":"object",
            "properties": {
                "result":{
                    "type" : "object",
                    "description" : "Query result of question",
                    "properties": {
                        "date" : {
                            "type" : "string",
                            "description" : "holiday date"
                            },
                        "name" : {
                            "type" : "string",
                            "description" : "holiday name"
                            }
                        },
                    "requires": ["date", "name"]
                    }
                },
            "required" : ["result"]
            }
    formated_llm = base_model.with_structured_output(holiday_schema1)
    res = formated_llm.invoke(question)

    
def generate_hw02(question):
    pass
    
def generate_hw03(question2, question3):
    pass
    
def generate_hw04(question):
    pass
    
def demo(question):
    print(question + ", from demo")
    llm = AzureChatOpenAI(
            model=gpt_config['model_name'],
            deployment_name=gpt_config['deployment_name'],
            openai_api_key=gpt_config['api_key'],
            openai_api_version=gpt_config['api_version'],
            azure_endpoint=gpt_config['api_base'],
            temperature=gpt_config['temperature']
    )
    message = HumanMessage(
            content=[
                {"type": "text", "text": question},
            ]
    )
    response = llm.invoke([message])
    
    return response
