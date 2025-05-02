import pollinations

model = pollinations.Image()
"""
(method) def __init__(
    self: Self@Image,
    model: ImageModel | None = "flux",
    width: Width | None = 1024,
    height: Height | None = 1024,
    seed: Seed | None = "random",
    nologo: NoLogo | None = False,
    private: Private | None = False,
    enhance: Enhance | None = False,
    safe: Safe | None = False,
    referrer: Referrer | None = "pollinations.py",
    *any_kwargs_will_be_passed_in_request: Args,
    **kwargs: Kwargs,
) -> None
"""

"""
(method) def __call__(
    self: Self@Image,
    prompt: Prompt,
    negative: Negative | None = "",
    *args: Args,
    file: Filename | None = "pollinations-image.jpeg",
    save: Save = False,
    *kwargs: Kwargs
) -> PILImage
"""
image = model("girly girl")
image.save("my_image.jpeg")
# Alternatively:
# image = model.Generate("A dog and cat.", file="my_image.jpeg", save=True)