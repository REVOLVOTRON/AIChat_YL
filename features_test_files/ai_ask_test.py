import openai

client = openai.OpenAI(
    api_key="io-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJvd25lciI6IjQ1ZTYwYWE3LTIxMGItNGI5Ny1hZDkwLWYzMDFkMTZiNDdiYyIsImV4cCI6NDg5ODk0MDE1NH0.cdTvLXPqopUM324g-pObyzhDQPDISpEfdS94qL0QjVKyVsnXqyogaDhFSImQd_kgWb01juOQFT3jo-iEpSeSRw",
    base_url="https://api.intelligence.io.solutions/api/v1/",
)

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-Coder-32B-Instruct",
    messages=[
        {"role": "system", "content": """
You are a calculator. Output ONLY valid Python mathematical expressions. Without 'math.'
Examples:
- "Calculate 2+2" → "2 + 2"
- "What is 5 multiplied by 3?" → "5 * 3"
- "7 divided by 2" → "7 / 2"
"""},
        {"role": "user", "content": "Натуральный логарифм из десяти деленый на 12 и это все умножено на 15"},
    ],
    temperature=0.7,
    stream=False,
    max_completion_tokens=1000
)

print(response.choices[0].message.content)


"https://ai.io.net/ai/models"


"""
LLM Model Name	Daily Chat quote	Daily API quote	Daily Embeddings quote	Context Length
deepseek-ai/DeepSeek-R1	1,000,000 tk	500,000 tk	N/A	128,000 tk
deepseek-ai/DeepSeek-R1-Distill-Llama-70B	1,000,000 tk	500,000 tk	N/A	128,000 tk
meta-llama/Llama-3.3-70B-Instruct	1,000,000 tk	500,000 tk	N/A	128,000 tk
deepseek-ai/DeepSeek-R1-Distill-Qwen-32B	1,000,000 tk	500,000 tk	N/A	128,000 tk
Qwen/QwQ-32B-Preview	1,000,000 tk	500,000 tk	N/A	32,000 tk
databricks/dbrx-instruct	1,000,000 tk	500,000 tk	N/A	32,000 tk
deepseek-ai/DeepSeek-R1-Distill-Llama-8B	1,000,000 tk	500,000 tk	N/A	128,000 tk
deepseek-ai/DeepSeek-R1-Distill-Qwen-14B	1,000,000 tk	500,000 tk	N/A	128,000 tk
deepseek-ai/DeepSeek-R1-Distill-Qwen-7B	1,000,000 tk	500,000 tk	N/A	128,000 tk
deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B	1,000,000 tk	500,000 tk	N/A	128,000 tk
microsoft/phi-4	1,000,000 tk	500,000 tk	N/A	16,000 tk
mistralai/Mistral-Large-Instruct-2411	1,000,000 tk	500,000 tk	N/A	128,000 tk
neuralmagic/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-dynamic	1,000,000 tk	500,000 tk	N/A	128,000 tk
google/gemma-2-9b-it	1,000,000 tk	500,000 tk	N/A	8,000 tk
nvidia/AceMath-7B-Instruct	1,000,000 tk	500,000 tk	N/A	4,000 tk
CohereForAI/aya-expanse-32b	1,000,000 tk	500,000 tk	N/A	8,000 tk
Qwen/Qwen2.5-Coder-32B-Instruct	1,000,000 tk	500,000 tk	N/A	32,000 tk
THUDM/glm-4-9b-chat	1,000,000 tk	500,000 tk	N/A	128,000 tk
CohereForAI/c4ai-command-r-plus-08-2024	1,000,000 tk	500,000 tk	N/A	128,000 tk
tiiuae/Falcon3-10B-Instruct	1,000,000 tk	500,000 tk	N/A	32,000 tk
NovaSky-AI/Sky-T1-32B-Preview	1,000,000 tk	500,000 tk	N/A	32,000 tk
bespokelabs/Bespoke-Stratos-32B	1,000,000 tk	500,000 tk	N/A	32,000 tk
netease-youdao/Confucius-o1-14B	1,000,000 tk	500,000 tk	N/A	32,000 tk
Qwen/Qwen2.5-1.5B-Instruct	1,000,000 tk	500,000 tk	N/A	32,000 tk
mistralai/Ministral-8B-Instruct-2410	1,000,000 tk	500,000 tk	N/A	32,000 tk
openbmb/MiniCPM3-4B	1,000,000 tk	500,000 tk	N/A	32,000 tk
jinaai/ReaderLM-v2	1,000,000 tk	500,000 tk	N/A	512,000 tk
ibm-granite/granite-3.1-8b-instruct	1,000,000 tk	500,000 tk	N/A	128,000 tk
microsoft/Phi-3.5-mini-instruct	1,000,000 tk	500,000 tk	N/A	128,000 tk
ozone-ai/0x-lite	1,000,000 tk	500,000 tk	N/A	32,000 tk
mixedbread-ai/mxbai-embed-large-v1	N/A	N/A	500,000 tk	512 tk
meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8	1,000,000 tk	500,000 tk	N/A	430,000 tk
"""