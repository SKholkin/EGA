from mutation.algo import saltation
from utils import prob_bool_choice


def launch_mutation(descendants, config):
    if config.get('mutation', {}).get('algoritm', None) == 'saltation':
        for i in range(len(descendants)):
            if prob_bool_choice(prob=float(config.get('mutation', {}).get('prob', 0.05))):
                descendants[i] = saltation(descendants[i], config.get('mutation', {}).get('to_mutate', 1))
    else:
        for i in range(len(descendants)):
            if prob_bool_choice(prob=0.05):
                descendants[i] = saltation(descendants[i], 1)
    return descendants
