import json
from jinja2 import Template

def generate_pipeline_html(status_file, output_file):
    with open(status_file, 'r') as file:
        status = json.load(file)

    template = Template("""
    <html>
        <head>
            <title>Pipeline Status Report</title>
        </head>
        <body>
            <h1>Pipeline Execution Report</h1>
            <table border="1">
                <tr>
                    <th>Step</th>
                    <th>Status</th>
                </tr>
                {% for step, result in status.items() %}
                <tr>
                    <td>{{ step }}</td>
                    <td>{{ result }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
    </html>
    """)

    html_content = template.render(status=status)
    with open(output_file, 'w') as file:
        file.write(html_content)

if __name__ == "__main__":
    generate_pipeline_html("status.json", "pipeline_report.html")
