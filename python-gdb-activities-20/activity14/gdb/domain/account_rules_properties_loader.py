# gdb/domain/account_rules_properties_loader.py
import os

class AccountRulesPropertiesLoader:
    """Utility loading external .properties files."""

    @staticmethod
    def load_rules(account_type: str) -> dict:
        filename = account_type.strip().lower() + ".properties"
        filepath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..", "resources", "config", "rules", filename
        )
        filepath = os.path.normpath(filepath)

        if not os.path.exists(filepath):
            return {}

        rules = {}
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, _, value = line.partition("=")
                    rules[key.strip()] = value.strip()
        return rules
