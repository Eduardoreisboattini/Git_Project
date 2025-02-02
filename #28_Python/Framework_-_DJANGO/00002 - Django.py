# Import necessary libraries
from django.template import Template, Context
from django.conf import settings

# Set the path to the custom template
settings.configure(TEMPLATE_DIRS=('/path/to/your/templates',))

# Load the custom template
template = Template("Hello, {{ name }}!")

# Create a context with the name variable
context = Context({'name': 'John'})

# Render the template with the context
rendered_template = template.render(context)

# Print the rendered template
print(rendered_template)
