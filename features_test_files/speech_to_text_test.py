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
(method) def Transcribe(
    self: Self@Text,
    file: Filename,
    *any_kwargs_will_be_passed_in_request: Args,
    **kwargs: Kwargs
) -> Output
"""

print(model.Transcribe("my_audio.mp3"))