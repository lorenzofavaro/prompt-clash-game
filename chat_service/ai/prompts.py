system_prompt = """Compose a unique prompt to generate an image based on the description messages.
Do not invent anything, use ONLY the descriptions.
**IMPORTANT**: Return the generation prompt in English.

<description_messages>
{user_history}

{image_desc}
</description_messages>

Examples:
    <description_messages>Generate an image of a horse</description_messages>
    Response: Generate an image of a horse

    <description_messages>Generate an image of a horse\n\nThe horse must have blue eyes</description_messages>
    Response: Generate an image of a horse with blue eyes.

    <description_messages>a dog running\n\nthe dog must be black\n\nI changed my mind, generate a red horse\n\nI want to see it in full</description_messages>
    Response: Generate an image of a full red horse.

Response:
"""
