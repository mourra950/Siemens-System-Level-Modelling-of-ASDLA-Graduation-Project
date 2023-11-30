from TemplateRenderer import convert_jinja_to_code

# This is just a test file to demonistrate the template rendering
# and is to be later deleted
convert_jinja_to_code('templates/train.py.jinja', 'output/train.py', {
    'learning_rate': 0.01,
    'batch_size': 256,
    'epochs': 1,
    'optimizer': 'Adadelta',
    'loss_func': 'L1Loss'
})