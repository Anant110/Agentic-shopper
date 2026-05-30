from agent.shopping_agent import agent

print("\nAI Retail Agent Ready!")
print("Type 'exit' to quit.\n")

while True:

    query = input("User: ")

    if query.lower() == "exit":
        break

    response =agent.invoke(
    {'messages':[{'role':'user',
                  'content':query}]}
    )

    print("\nAssistant:")
    print(response['messages'][-1].content[0]['text'])