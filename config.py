import json
from addict import Dict
from utils import create_weigth_matrix_from_file

def create_config(path):
    config = EGAConfig.from_json(path)
    config.upload_weight_matrix()
    return config

class EGAConfig(Dict):

    @classmethod
    def from_json(cls, path) -> 'EGAConfig':
        with open(path) as f:
            loaded_json = json.load(f)
        return cls(loaded_json)

    # TODO: implement this
    def upload_weight_matrix(self):
        self.weight_matrix = create_weigth_matrix_from_file(self.weight_matrix)
        pass
