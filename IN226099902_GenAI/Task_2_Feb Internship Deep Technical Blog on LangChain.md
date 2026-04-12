LangChain Deep Technical Blog: Building LLM Applications the Right Way
Link of medium: https://medium.com/@ashishsaval2002/langchain-deep-technical-blog-building-llm-applications-the-right-way-fa3ce60510cf


When people first hear LangChain, they often assume it is “just a wrapper around an LLM.” That is too small a view. In the current LangChain Python stack, the framework is built around composable building blocks for models, messages, prompts, tools, memory, and agents, and create_agent is the standard way to build agents on top of a graph-based runtime. LangChain also gives you a very broad integration layer across providers, vector stores, document loaders, and toolkits, so you can swap components without rewriting the whole application.

A useful way to think about this assignment is: you are not writing a chatbot; you are designing a system. A prompt alone is fragile. A well-designed LangChain app separates concerns: one component formats input, another calls the model, another retrieves context, another uses tools, and memory keeps the conversation coherent over time. That modularity is exactly why LangChain matters in modern LLM development.

Step 1: Introduction to LangChain
   LangChain is an open-source framework for building LLM-powered applications and agents. Its value is not that it “talks to models.” Its value is that it gives you a structured way to connect the model to context, tools, memory, and external systems. In practice, that means you can build assistants that answer questions, search documents, call APIs, query databases, and handle multi-step workflows with a consistent interface.

But why is this crucial? Because real-world LLM apps are not single-prompt demos. They need orchestration. They need retrieval. They need tool use. They need conversation state. LangChain exists to make those pieces composable instead of hard-coded.

Press enter or click to view image in full size

Step 2: Core Components of LangChain
   Press enter or click to view image in full size

Step 2.1: LLMs and Chat Models
Models are the reasoning engine of the system. In LangChain, standard model interfaces let you connect to different providers through a consistent API, which makes provider switching much easier. Messages are the basic unit of context, and chat models operate on message objects like system, human, AI, and tool messages.

Why it exists:
To decouple your application logic from any single model provider.

# Step 1: Import libraries
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Step 2: Initialize the model
llm = ChatOpenAI(
model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
temperature=0
)

# Step 3: Invoke with a message
response = llm.invoke([
HumanMessage(content="Explain LangChain in one sentence.")
])

# Step 4: Print result
print(response.content)
Step 2.2: Prompts and Prompt Templates
Prompts are not just text; they are structured instructions. ChatPromptTemplate helps you define reusable message patterns with variables, which reduces prompt bugs and keeps your app maintainable. LangChain documentation also emphasizes using message-based prompts for system instructions and multi-turn interaction.

Why it exists:
To separate prompt design from business logic.

# Step 1: Import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate

# Step 2: Create the prompt template
prompt = ChatPromptTemplate.from_messages([
("system", "You are a senior data science mentor."),
("human", "Explain {topic} in simple but technical terms.")
])

# Step 3: Format the prompt
formatted = prompt.invoke({"topic": "LangChain"})

# Step 4: Print the result
print(formatted)
Step 2.3: Chains
Chains are predefined sequences of steps. In the simplest case, a chain connects prompt → model → parser. This is still one of the cleanest ways to build predictable LLM flows. The LangChain philosophy explicitly talks about chains as predetermined steps of computation, such as retrieval followed by generation.

Why it exists:
To make repeated workflows deterministic and easy to reuse.

# Step 1: Import output parser
from langchain_core.output_parsers import StrOutputParser

# Step 2: Create the chain
chain = prompt | llm | StrOutputParser()

# Step 3: Invoke the chain
answer = chain.invoke({"topic": "prompt engineering"})

# Step 4: Print the answer
print(answer)
This pipe-based style is one of the biggest practical wins in modern LangChain. It is readable, modular, and easy to test.

Press enter or click to view image in full size

Step 2.4: Memory
Memory is what makes a system feel continuous instead of stateless. LangChain’s short-term memory stores conversation history inside the agent state, usually under a messages key, and persistence is handled through a checkpointer. That matters because long conversations can exceed the model context window, increase latency, and raise cost.

Why it exists:
To preserve conversation context across turns without forcing the model to reread everything every time.

# Step 1: Import create_agent and memory
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

# Step 2: Create agent with memory
memory_agent = create_agent(
model=llm,
tools=[],
checkpointer=InMemorySaver()
)

# Step 3: First interaction
result1 = memory_agent.invoke(
{"messages": [{"role": "user", "content": "My name is Ashish."}]},
{"configurable": {"thread_id": "demo-1"}}
)

# Step 4: Second interaction to test memory
result2 = memory_agent.invoke(
{"messages": [{"role": "user", "content": "What is my name?"}]},
{"configurable": {"thread_id": "demo-1"}}
)

# Step 5: Print the response
print(result2["messages"][-1].content)
Step 2.5: Agents
Agents combine models with tools so the system can decide what action to take next. In LangChain v1, create_agent builds a graph-based agent runtime on top of LangGraph. The agent moves through nodes such as model calls and tool execution until it reaches a stop condition.

Why it exists:
To let the LLM reason, act, inspect results, and continue iterating.

# Step 1: Import modules
from langchain.agents import create_agent
from langchain.tools import tool

# Step 2: Define a tool
@tool
def calculator(expression: str) -> str:
"""Evaluate a basic arithmetic expression."""
try:
return str(eval(expression, {"**builtins**": {}}))
except Exception as e:
return f"Error: {e}"

# Step 3: Create the agent
agent = create_agent(
model=llm,
tools=[calculator],
system_prompt="You are a careful assistant. Use tools when needed."
)

# Step 4: Invoke the agent
result = agent.invoke({
"messages": [{"role": "user", "content": "What is (25 * 4) + 12?"}]
})

# Step 5: Print the result
print(result["messages"][-1].content)
Press enter or click to view image in full size

Agents use LLMs to decide which tool or chain to call in real time.

Standard Agents: Simple tool orchestration.
Deep Agents: Multi-step planning, sub-agents, file system access, structured reasoning.
Analogy: The orchestra conductor directing the right instrument (tool) at the right time, adjusting dynamically.
⚠️ Leadership Watch-Out: Agents are powerful but unpredictable. Always sandbox, monitor, and add guardrails before enterprise deployment.

Step 2.6: Tools
Tools are callable functions with clear inputs and outputs. LangChain passes them to the model, and the model decides when to invoke them based on the conversation. This is how agents fetch real-time data, query databases, run calculations, or trigger external actions. The docs also recommend clear names and informative docstrings so the model can use tools correctly.

Why it exists:
To connect language reasoning with real actions.

Tools are APIs or functions the LLM can call.

Examples: Search APIs, Python calculators, Salesforce connectors, SQL query runners.
Analogy: Tools are the power drills and hammers in an AI engineer’s toolbox without them, the LLM is limited to reasoning over its input.
Delivery Note: Tool governance is essential. Uncontrolled tools increase risk, latency, and compliance issues.
# Step 1: Define a tool using the @tool decorator
@tool
def get_status(ticket_id: str) -> str:
"""Check the status of a support ticket."""
mock_db = {"T-101": "Open", "T-102": "Resolved"}
return mock_db.get(ticket_id, "Ticket not found")
Step 2.7: Document Loaders
Document loaders bring data from files, web pages, Slack, Notion, Google Drive, and more into LangChain’s standard Document format. That uniform format is what makes downstream retrieval and indexing possible.

Write on Medium
Why it exists:
To normalize messy external data into a common structure.

# Step 1: Import the document loader
from langchain_community.document_loaders import PyPDFLoader

# Step 2: Create a loader instance
loader = PyPDFLoader("company_policy.pdf")

# Step 3: Load the documents
docs = loader.load()

# Step 4: Print the number of documents
print(len(docs))
Press enter or click to view image in full size

Step 2.8: Indexes / Vector Stores
Vector stores keep embeddings and make semantic search possible. LangChain provides a unified interface for vector stores, so you can add documents, delete documents, and run similarity search without changing your app logic. That abstraction is central to RAG systems.

Why it exists:
To let the model retrieve the right context before generating an answer.

# Step 1: Import necessary modules
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# Step 2: Create a text splitter
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)

# Step 3: Split the documents into chunks
chunks = splitter.split_documents(docs)

# Step 4: Create embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Step 5: Create vector store from documents
vectorstore = Chroma.from_documents(chunks, embeddings)

# Step 6: Create a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 4}) Step 3: Architecture Explanation

A LangChain application usually follows this flow:

The key idea is simple: the user asks something, the prompt shapes the request, the model interprets it, and the chain or agent decides whether more context or a tool is needed before producing the final response. In agentic systems, the loop continues until the model has enough information to stop. LangChain’s agent docs describe this as a graph-based runtime, while the tools docs explain that tools are called when the model decides they are needed.

Press enter or click to view image in full size

Step 4: Conversational AI Agent Flow
   Press enter or click to view image in full size

Step 5: Hands-on Code Examples
   Example 1: Basic LLM Call
   # Step 1: Import the required libraries
   import os
   from langchain_openai import ChatOpenAI
   from langchain_core.messages import HumanMessage
   
   # Step 2: Initialize the ChatOpenAI model
   llm = ChatOpenAI(
   model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
   temperature=0
   )
   
   # Step 3: Invoke the model with a human message
   response = llm.invoke([HumanMessage(content="What is LangChain?")])
   
   # Step 4: Print the response
   print(response.content)
   Example 2: PromptTemplate Usage
   # Step 1: Import the ChatPromptTemplate
   from langchain_core.prompts import ChatPromptTemplate
   
   # Step 2: Create a prompt template with system and human messages
   prompt = ChatPromptTemplate.from_messages([
   ("system", "You are a concise technical writer."),
   ("human", "Write a short explanation of {concept}.")
   ])
   
   # Step 3: Invoke the prompt with a specific concept
   result = prompt.invoke({"concept": "vector stores"})
   
   # Step 4: Print the formatted prompt
   print(result)
   Example 3: Simple Chain
   # Step 1: Import the output parser
   from langchain_core.output_parsers import StrOutputParser
   
   # Step 2: Create a chain by piping prompt, llm, and parser
   chain = prompt | llm | StrOutputParser()
   
   # Step 3: Invoke the chain with input data
   print(chain.invoke({"concept": "LangChain agents"}))
   Example 4: Agent with Tool
   # Step 1: Import necessary modules
   from langchain.agents import create_agent
   from langchain.tools import tool
   
   # Step 2: Define a tool function
   @tool
   def check_inventory(product_id: str) -> str:
   """Check product inventory."""
   stock = {"P100": 12, "P200": 0}
   return f"Stock for {product_id}: {stock.get(product_id, 'unknown')}"
   
   # Step 3: Create an agent with the tool
   agent = create_agent(
   model=llm,
   tools=[check_inventory],
   system_prompt="You are a helpful operations assistant."
   )
   
   # Step 4: Invoke the agent with a user message
   result = agent.invoke({
   "messages": [{"role": "user", "content": "Check inventory for P100"}]
   })
   
   # Step 5: Print the final response
   print(result["messages"][-1].content)
   Example 5: Memory Example
   # Step 1: Import the memory saver
   from langgraph.checkpoint.memory import InMemorySaver
   
   # Step 2: Create an agent with memory checkpointer
   agent_with_memory = create_agent(
   model=llm,
   tools=[],
   checkpointer=InMemorySaver()
   )
   
   # Step 3: Set up configuration for thread
   config = {"configurable": {"thread_id": "user-42"}}
   
   # Step 4: Invoke the agent with initial message
   agent_with_memory.invoke(
   {"messages": [{"role": "user", "content": "My favorite language is Python."}]},
   config
   )
   
   # Step 5: Invoke again to test memory
   final_state = agent_with_memory.invoke(
   {"messages": [{"role": "user", "content": "What is my favorite language?"}]},
   config
   )
   
   # Step 6: Print the response
   print(final_state["messages"][-1].content)
Step 6: Real-World Use Cases

1) Customer Support Assistant
   Problem: Support teams spend time answering the same questions again and again.
   LangChain solution: Use an agent with tools for ticket lookup, policy search, and escalation.
   Components used: Chat model, prompt template, agent, tools, memory.

2) PDF Q&A Bot for Internal Knowledge
   Problem: Employees need answers hidden inside manuals, SOPs, and policy PDFs.
   LangChain solution: Load PDFs, split them into chunks, embed them, store them in a vector store, and retrieve relevant passages before generation.
   Components used: Document loaders, text splitters, embeddings, vector stores, retriever, chain.

3) Research Assistant with Conversation Memory
   Problem: Users ask follow-up questions and expect the system to remember earlier context.
   LangChain solution: Use short-term memory with a checkpointer so the system retains prior turns per thread.
   Components used: Messages, memory, agent state, checkpointer.

Step 7: Advantages and Limitations
   LangChain’s biggest strengths are modularity, fast prototyping, and integrations. It gives you a standard interface across providers and components, which means you can move from a demo to a real system without rewriting everything. It is also strong in retrieval and agent orchestration, which is why it fits modern GenAI applications so well.

Its limitations are just as important. Agent loops can add latency and cost because the system may call the model and tools multiple times. Long context can become expensive and harder to manage, which is why memory strategies like trimming or summarizing matter. Debugging also becomes more complex once you introduce multiple steps, middleware, and tool calls; LangSmith is recommended for tracing and evaluation.

So when should you not use LangChain? If your workflow is a single prompt and a single response, adding an agent is unnecessary complexity. LangGraph’s own documentation distinguishes workflows with predetermined paths from agents with dynamic behavior; if your use case is fixed and simple, a plain script or a minimal chain is cleaner.

Step 8: Conclusion
   LangChain is not valuable because it hides LLMs. It is valuable because it helps you design reliable LLM systems: prompts for structure, chains for predictable flows, tools for action, memory for continuity, and agents for decision-making. In the current ecosystem, the real shift is from “prompting a model” to “orchestrating a system,” and LangChain v1 is built around that idea.
