from jinja2 import Template

# Define the data dictionary
data = {
    "layers": [],
    "misc_params": {
        "width": 1,
        "height": 1,
        "channels": 1,
        "batch_size": 1,
        "num_epochs": 1,
        "optimizer": {
            "type": "ASGD",
            "params": {
                "lr": 0.0,
                # "lambd": 0.0,
                # "alpha": 0.0,
                # "t0": 0.0,
                "weight_decay": 1,
                "foreach": True,
                "maximize": True,
                "differentiable": True,
            },
        },
    },
}

# Define the Jinja2 template code as a string
template_str = """
# Static parameters
width: {{ misc_params.width }}
height: {{ misc_params.height }}
channels: {{ misc_params.channels }}
batch_size: {{ misc_params.batch_size }}
num_epochs: {{ misc_params.num_epochs }}

# Layers
{% for layer in layers %}
Layer: {{ layer }}
{% endfor %}

# Dynamic optimizer parameters
optimizer_type: {{ misc_params.optimizer.type }}
{% for param, value in misc_params.optimizer.params.items() %}
{{ param }}: {{ value }}
{% endfor %}
"""

# Create a Jinja2 template object
template = Template(template_str)

# Render the template with the data
result_file = template.render(layers=data["layers"], misc_params=data["misc_params"])

# Output the rendered result
print(result_file)
