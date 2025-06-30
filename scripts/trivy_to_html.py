import json
from jinja2 import Template

def generate_trivy_html(json_file, output_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

        # Handle missing "Results" gracefully
        if "Results" not in data:
            raise ValueError(f"Missing 'Results' in {json_file}")

        # Jinja2 template for HTML rendering
        template = Template("""
        <html>
            <head>
                <title>Trivy Scan Report</title>
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
                        {% if result.Vulnerabilities %}
                            {% for vuln in result.Vulnerabilities %}
                            <tr>
                                <td>{{ result.Target }}</td>
                                <td>{{ vuln.VulnerabilityID }}</td>
                                <td>{{ vuln.PkgName }}</td>
                                <td>{{ vuln.Severity }}</td>
                                <td>{{ vuln.Description }}</td>
                            </tr>
                            {% endfor %}
                        {% else %}
                            <tr>
                                <td colspan="5">No vulnerabilities found in {{ result.Target }}</td>
                            </tr>
                        {% endif %}
                    {% endfor %}
                </table>
            </body>
        </html>
        """)

        # Generate the HTML content using the template
        html_content = template.render(results=data["Results"])

        # Write the HTML to the output file
        with open(output_file, 'w') as file:
            file.write(html_content)

        print(f"HTML report generated successfully: {output_file}")

    except Exception as e:
        print(f"Error generating report: {e}")

if __name__ == "__main__":
    # Example usage with Trivy's JSON file
    generate_trivy_html("trivy.json", "trivy_report.html")
