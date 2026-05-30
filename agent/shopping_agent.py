from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import StructuredTool
from langchain.agents import create_agent
import os

import sys

print("cwd =", os.getcwd())
print("file =", __file__)
print("sys.path =")
for p in sys.path:
    print(p)


load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.product_tools import (
    search_products,
    get_product,
    SearchProductsInput,
    productInput
)

from tools.order_tools import (
    get_order,
    OrderIdInput
)

from tools.return_tools import (
    evaluate_return,
    GetOrderId
)

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

tools = [

    StructuredTool.from_function(
        func=search_products,
        args_schema=SearchProductsInput
    ),

    StructuredTool.from_function(
        func=get_product,
        args_schema=productInput
    ),

    StructuredTool.from_function(
        func=get_order,
        args_schema=OrderIdInput
    ),

    StructuredTool.from_function(
        func=evaluate_return,
        args_schema=GetOrderId
    )
]

agent = create_agent(
    model=llm,
    tools=tools,
)

# user_query=input("What is your query today?")

# # response=llm.invoke("How is the whether in Rome")
# response=agent.invoke(
#     {'messages':[{'role':'user',
#                   'content':user_query}]}
# )

# print(response['messages'][-1].content)