from sacred import Experiment

ex = Experiment('hello world experiment') # experiment name

@ex.config
def my_config():
    recipient = "world"
    message = "Hello %s!" % recipient
    my_cfg1 = 123
    my_cfg2 = 456

@ex.capture
def foo(my_cfg1):
    print('foo %s' %my_cfg1)
    # print(my_cfg2) # does not work

@ex.automain
def my_main(message):
    print(message)
    foo() # no parameter here
    foo(789) # can do overriding
