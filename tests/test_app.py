import pytest

from src.domain import FileType


class TestExtractAPI:
    @pytest.mark.parametrize(
        "filename",
        [
            "drivers_license_1.jpg",
            "drivers_licence_2.jpg",
            "drivers_license_3.jpg",
        ],
    )
    def test_drivers_licenses(self, client, filename):
        with open(f"files/{filename}", "rb") as f:
            files = {"file": f}
            resp = client.post("/classify_file", files=files)

        assert resp.json() == {"file_type": FileType.DRIVERS_LICENSE.name}

    @pytest.mark.parametrize(
        "filename",
        [
            "bank_statement_1.pdf",
            "bank_statement_2.pdf",
            "bank_statement_3.pdf",
        ],
    )
    def test_bank_statements(self, client, filename):
        with open(f"files/{filename}", "rb") as f:
            files = {"file": f}
            resp = client.post("/classify_file", files=files)

        assert resp.json() == {"file_type": FileType.BANK_STATEMENT.name}

    @pytest.mark.parametrize(
        "filename",
        [
            "invoice_1.pdf",
            "invoice_2.pdf",
            "invoice_3.pdf",
        ],
    )
    def test_invoices(self, client, filename):
        with open(f"files/{filename}", "rb") as f:
            files = {"file": f}
            resp = client.post("/classify_file", files=files)

        assert resp.json() == {"file_type": FileType.INVOICE.name}

    @pytest.mark.parametrize(
        "filename",
        [
            "passport_1.jpeg",
            "passport_2.png",
            "passport_3.png",
        ],
    )
    def test_passports(self, client, filename):
        with open(f"files/{filename}", "rb") as f:
            files = {"file": f}
            resp = client.post("/classify_file", files=files)

        assert resp.json() == {"file_type": FileType.PASSPORT.name}

    @pytest.mark.parametrize(
        "filename",
        [
            "insurance_policy_1.jpg",
            "insurance_policy_2.png",
            "insurance_policy_3.jpg",
        ],
    )
    def test_insurance_policies(self, client, filename):
        with open(f"files/{filename}", "rb") as f:
            files = {"file": f}
            resp = client.post("/classify_file", files=files)

        assert resp.json() == {"file_type": FileType.INSURANCE_POLICY.name}

    @pytest.mark.parametrize(
        "filename",
        [
            "credit_report_1.png",
            "credit_report_2.png",
        ],
    )
    def test_credit_reports(self, client, filename):
        with open(f"files/{filename}", "rb") as f:
            files = {"file": f}
            resp = client.post("/classify_file", files=files)

        assert resp.json() == {"file_type": FileType.CREDIT_REPORT.name}

    @pytest.mark.parametrize(
        "filename",
        [
            "receipt_1.jpg",
            "receipt_2.jpeg",
            "receipt_3.jpg",
        ],
    )
    def test_receipt(self, client, filename):
        with open(f"files/{filename}", "rb") as f:
            files = {"file": f}
            resp = client.post("/classify_file", files=files)

        assert resp.json() == {"file_type": FileType.RECEIPT.name}

    @pytest.mark.parametrize(
        "filename",
        [
            "utility_bill_1.jpg",
            "utility_bill_2.jpg",
            "utility_bill_3.jpg",
        ],
    )
    def test_utility_bill(self, client, filename):
        with open(f"files/{filename}", "rb") as f:
            files = {"file": f}
            resp = client.post("/classify_file", files=files)

        assert resp.json() == {"file_type": FileType.UTILITY_BILL.name}
