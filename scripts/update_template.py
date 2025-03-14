import re
import os

def update_template(template_path, output_path, values):
    # Read the template file
    with open(template_path, 'r') as file:
        template = file.read()

    # Replace placeholders with actual values
    for key, value in values.items():
        template = re.sub(f"{{{{{key}}}}}", value, template)

    # Write the updated content to the output file
    with open(output_path, 'w') as file:
        file.write(template)

# Define the paths to the template and output files
template_path = '/Users/kv56174/Documents/GitHub/tw-vv-automation-test/templates/software-verification-plan.md'
output_path = '/Users/kv56174/Documents/GitHub/tw-vv-automation-test/docs/updated_document.md'

# Define the values to replace in the template
values = {
    'DOC_NUMBER': 'PLN-1001442',
    'VERSION': '2.8.0.10211',
    'REVISION': '001',
    'REFERENCE_1': 'Design Control Change Plan',
    'REFERENCE_2': 'Test Protocol Review Records'
}

# Update the template with the values
update_template(template_path, output_path, values)
