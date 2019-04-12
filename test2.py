from sacred import Experiment

ex = Experiment('configuration example') # experiment name

@ex.config
def my_config():
    my_cfg1 = 123

@ex.automain
def my_main():
    pass

