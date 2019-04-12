from sacred import Experiment

ex = Experiment('configuration example') # experiment name

@ex.config
def my_config():
    my_cfg1 = 123

@ex.capture
def foo(my_cfg1):
    print('foo %s' %my_cfg1)
    ex.log_scalar('calculated_value', 2*2)

@ex.automain
def my_main():
    foo() # no parameter here

