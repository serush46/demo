import json
from jinja2 import Template

def generate_trivy_html(json_file, output_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    template = Template("""
    <html>
        <head>
            <title>Trivy Report</title>
        </head>
        <body>
            <h1>Trivy Scan Report</h1>
            <table border="1">
                <tr>
                    <th>Target</th>
                    <th>Vulnerability ID</th>
                    <th>Pkg Name</th>
                    <th>Severity</th>
                    <th>Description</th>
                </tr>
                {% for result in results %}
                    {% for vuln in result.Vulnerabilities %}
                    <tr>
                        <td>{{ result.Target }}</td>
                        <td>{{ vuln.VulnerabilityID }}</td>
                        <td>{{ vuln.PkgName }}</td>
                        <td>{{ vuln.Severity }}</td>
                        <td>{{ vuln.Description }}</td>
                    </tr>
                    {% endfor %}
                {% endfor %}
            </table>
        </body>
    </html>
    """)

    html_content = template.render(results=data["Results"])
    with open(output_file, 'w') as file:
        file.write(html_content)

if __name__ == "__main__":
    generate_trivy_html("trivy.json", "trivy_report.html")
