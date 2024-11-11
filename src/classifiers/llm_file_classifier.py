import base64

from openai import AsyncOpenAI
from pydantic import BaseModel

from src.domain import File, FileType


class ClassifiedFileType(BaseModel):
    explanation: str
    file_type: FileType


class LLMFileClassifier:
    PROMPT = (
        "What kind of document is this an image of? Choose UNKNOWN if it's not on the list of available file_types."
    )

    def __init__(self):
        self.client = AsyncOpenAI()

    def _encode_image(self, file: File) -> str:
        image_data = file.content.read()
        return base64.b64encode(image_data).decode("utf-8")

    async def clasify_file(self, file: File) -> FileType:
        base64_img = self._encode_image(file)
        url = f"data:image/{file.extension(with_dot=False)};base64,{base64_img}"

        response = await self.client.beta.chat.completions.parse(
            model="gpt-4o",
            response_format=ClassifiedFileType,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": self.PROMPT},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": url,
                            },
                        },
                    ],
                }
            ],
        )
        resp = response.choices[0].message.parsed
        return resp.file_type
