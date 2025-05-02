import pollinations

"""
(method) def __init__(
    self: Self@Text,
    model: Model | None = "openai",
    system: System | None = "You are a helpful AI assistant.",
    contextual: Contextual | None = False,
    messages: Messages | None = [],
    private: Private | None = False,
    seed: Seed | None = "random",
    reasoning_effort: ReasoningEffort | None = "medium",
    tools: Tools | None = [],
    tool_choices: ToolChoice | None = [],
    voice: Voice | None = None,
    json_mode: JsonMode | None = False,
    referrer: Referrer | None = "pollinations.py",
    openai_endpoint: UseOpenAIEndpoint | None = False,
    *any_kwargs_will_be_passed_in_request: Args,
    **kwargs: Kwargs,
) -> None
"""

model = pollinations.Text()

"""
(method) def __call__(
    self: Self@Text,
    prompt: Prompt | None = None,
    *any_kwargs_will_be_passed_in_request: Args,
    stream: Stream | None = False,
    **kwargs: Kwargs
) -> Output
"""

print(model("Напиши змейку на пайтон"))
# Alternatively:
# print(model.Generate("Hello, what is 1 + 1?"))


# Streaming
for token in model("Напиши змейку на пайтон", stream=True):
    print(token, end="", flush=True)

# Alternatively:
# for token in model.Generate("Hello, what is 1 + 1?", stream=True):
#     print(token, end="", flush=True)