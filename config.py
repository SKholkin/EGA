import json
from addict import Dict


class EGAConfig(Dict):

    @classmethod
    def from_json(cls, path) -> 'EGAConfig':
        with open(path) as f:
            loaded_json = json.load(f)
        return cls(loaded_json)
