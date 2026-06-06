from backend.app.llm.factory import LLMFactory

llm = LLMFactory.get_llm()

response = llm.invoke(
    "What is root cause analysis?"
)

print(response.content)