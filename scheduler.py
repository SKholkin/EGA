class PlateauScheduler:
    def __init__(self, ega_state, patience=50, threshold=0):
        self.ega_state = ega_state
        self.threshold = threshold
        self.patience = patience
        self.max_value = 0
        self.waiting = 0

    def step(self, value):
        if value < self.max_value * (1 + self.threshold):
            self.waiting += 1
        else:
            self.waiting = 0
            self.max_value = value

        if self.waiting > self.patience:
            self.ega_state.gen_overlap = self.ega_state.gen_overlap / 2
            self.waiting = 0


def create_scheduler(ega_state, config):
    return PlateauScheduler(ega_state, patience=config.get('scheduler', {}).get('patience', 50),
                            threshold=config.get('scheduler', {}).get('threshold', 0))
