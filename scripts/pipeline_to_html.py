import json
import os

def generate_pipeline_html(status_file, output_file):
    if not os.path.exists(status_file):
        print(f"Error: {status_file} does not exist.")
        return

    with open(status_file, 'r') as file:
        data = json.load(file)

    html_content = """<html>
    <head>
        <title>Pipeline Status Report</title>
        <style>
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
            th { background-color: #f2f2f2; }
            .success { background-color: #d4edda; }
            .failure { background-color: #f8d7da; }
            body { font-family: Arial, sans-serif; margin: 20px; }
        </style>
    </head>
    <body>
        <h1>Pipeline Status Report</h1>
        <table>
            <tr><th>Step Name</th><th>Status</th></tr>
    """

    for step in data["steps"]:
        status_class = "success" if step["status"] == "success" else "failure"
        html_content += f"<tr class='{status_class}'><td>{step['name']}</td><td>{step['status']}</td></tr>"

    html_content += "</table></body></html>"

    with open(output_file, 'w') as file:
        file.write(html_content)

status_file = os.getenv('STATUS_FILE', 'status.json')
output_file = os.getenv('HTML_REPORT', 'pipeline_report.html')
generate_pipeline_html(status_file, output_file)
