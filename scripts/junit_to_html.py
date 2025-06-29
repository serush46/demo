# scripts/junit_to_html.py
import os
import sys
import xml.etree.ElementTree as ET

input_dir = "target/surefire-reports"
output_file = "junit-report.html"

if not os.path.exists(input_dir):
    print(f"[ERROR] Directory not found: {input_dir}")
    sys.exit(1)

def convert(xml_path, html_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    with open(html_path, "w") as f:
        f.write("<html><head><title>JUnit Report</title></head><body>")
        f.write("<h1>JUnit Test Report</h1>")
        for testcase in root.iter("testcase"):
            f.write(f"<div><strong>{testcase.attrib['classname']} - {testcase.attrib['name']}</strong></div>")
            for failure in testcase.findall("failure"):
                f.write(f"<pre style='color:red'>{failure.text}</pre>")
        f.write("</body></html>")

# Convert all XMLs
for file in os.listdir(input_dir):
    if file.startswith("TEST-") and file.endswith(".xml"):
        convert(os.path.join(input_dir, file), output_file)
        break  # just use the first test file for simplicity
