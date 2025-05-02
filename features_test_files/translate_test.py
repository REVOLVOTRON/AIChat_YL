from iointel import (
    Agent,
    Workflow
)

import os

os.environ["OPENAI_API_KEY"] = "io-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJvd25lciI6IjQ1ZTYwYWE3LTIxMGItNGI5Ny1hZDkwLWYzMDFkMTZiNDdiYyIsImV4cCI6NDg5ODk0MDE1NH0.cdTvLXPqopUM324g-pObyzhDQPDISpEfdS94qL0QjVKyVsnXqyogaDhFSImQd_kgWb01juOQFT3jo-iEpSeSRw"  # Replace with your actual IO.net API key

text = """The future of artificial intelligence is rapidly evolving. With advancements in deep learning and neural networks, AI is transforming industries such as healthcare, finance, and transportation. As technology continues to improve, AI will play an even greater role in solving complex problems and enhancing human capabilities."""


agent = Agent(
    name="Translate Agent",
    instructions="You are an assistant specialized in translation.",
    model="meta-llama/Llama-3.3-70B-Instruct",
    api_key="io-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJvd25lciI6IjQ1ZTYwYWE3LTIxMGItNGI5Ny1hZDkwLWYzMDFkMTZiNDdiYyIsImV4cCI6NDg5ODk0MDE1NH0.cdTvLXPqopUM324g-pObyzhDQPDISpEfdS94qL0QjVKyVsnXqyogaDhFSImQd_kgWb01juOQFT3jo-iEpSeSRw",
    base_url="https://api.intelligence.io.solutions/api/v1"
)

workflow = Workflow(text=text, client_mode=False)
results = workflow.translate_text(target_language="russian",agents=[agent]).run_tasks()
print(results)




"https://ai.io.net/ai/agents"