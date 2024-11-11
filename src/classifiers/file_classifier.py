from openai import OpenAIError

from src.domain import File, FileType
from src.classifiers.llm_file_classifier import LLMFileClassifier
from src.classifiers.offline_file_classifier import OfflineFileClassifier
from src.classifiers.file_converter import FileConverter


class FileClassifier:
    """Take a file and classify what kind of file it is.

    Broadly taking the strategy:
    - Convert the file to an image (if needed).
    - Use a multimodal input LLM model to examine the file, and classify it.
    """

    async def classify_file(self, file: File) -> FileType:
        if not file.is_image():
            file = FileConverter().convert_file(file)

        try:
            file_type = await LLMFileClassifier().clasify_file(file)
        except OpenAIError:
            # Use a tiered archetechture, so that we can fall back to cheaper
            # more reliable (but less capable) classifiers in the face of issues.
            file_type = OfflineFileClassifier().classify_file(file)

        return file_type
