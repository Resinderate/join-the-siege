from io import BytesIO

from pdf2image import convert_from_bytes

from src.domain import File


class FileConverter:
    """Take a file and convert it to an image.

    Currently only supports pdfs, but gives us a place to extend for other file types.

    The general idea would probably to go from docx/pages/etc -> pdf -> jpeg.
    """

    def convert_file(self, file: File) -> File:
        if file.extension() != ".pdf":
            # Here we would delegate to some targetted pipeline to convert arbitrary files to PDF.
            # Probably easier to cover more files this way, than going directly from files to images.
            raise ValueError("We only support PDFs for now.")

        # This is only taking the first page for now, but could take _all_ and combine or classify different pages.
        image = convert_from_bytes(file.content.read(), fmt="jpeg", single_file=True)[0]

        image_content = BytesIO()
        image.save(image_content, format="JPEG")
        image_content.seek(0)

        new_name = file.name.replace(file.extension(), ".jpeg")
        return File(name=new_name, content=image_content)
