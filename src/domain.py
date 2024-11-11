from enum import StrEnum
from dataclasses import dataclass
from typing import BinaryIO
from pathlib import Path


@dataclass
class File:
    name: str
    content: BinaryIO

    def extension(self, with_dot: bool = True) -> str:
        extension = Path(self.name).suffix
        if not with_dot:
            extension = extension[1:]
        return extension

    def is_image(self) -> bool:
        return self.extension() in {".png", ".jpeg", ".jpg"}


class FileType(StrEnum):
    """The type of document the file contains.

    This is regardless of the file format like pdf/docx/jpg etc.
    """

    DRIVERS_LICENSE = "DRIVERS_LICENSE"
    BANK_STATEMENT = "BANK_STATEMENT"
    INVOICE = "INVOICE"

    PASSPORT = "PASSPORT"
    INSURANCE_POLICY = "INSURANCE_POLICY"
    RECEIPT = "RECEIPT"
    UTILITY_BILL = "UTILITY_BILL"
    CREDIT_REPORT = "CREDIT_REPORT"

    UNKNOWN = "UNKNOWN"
