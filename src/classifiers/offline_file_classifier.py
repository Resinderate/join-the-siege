from src.domain import File, FileType


class OfflineFileClassifier:
    def classify_file(self, file: File) -> FileType:
        filename = file.name.lower()

        if "drivers_license" in filename:
            return FileType.DRIVERS_LICENSE

        if "bank_statement" in filename:
            return FileType.BANK_STATEMENT
            return "bank_statement"

        if "invoice" in filename:
            return FileType.INVOICE

        return FileType.UNKNOWN
