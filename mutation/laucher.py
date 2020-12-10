def launch_mutation(descendants, config):
    not_chosen_desc = []
    chosen_descendants = []
    mutated = []
    if config.mutation.is_additional:
        return not_chosen_desc + chosen_descendants + mutated
    else:
        return not_chosen_desc + mutated