"""Singleton config."""
import json, os

class ConfigManager:
    _instance = None
    CONFIG_PATH = os.path.expanduser('~/.signbridge/config.json')

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load()
        return cls._instance

    def _load(self):
        os.makedirs(os.path.dirname(self.CONFIG_PATH), exist_ok=True)
        if os.path.exists(self.CONFIG_PATH):
            with open(self.CONFIG_PATH) as f:
                self._data = json.load(f)
        else:
            self._data = {"theme":"flatly","user":"","progress":{}}
            self._save()

    def _save(self):
        with open(self.CONFIG_PATH, 'w') as f:
            json.dump(self._data, f, indent=2)

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value
        self._save()

ConfigManager._instance = None
