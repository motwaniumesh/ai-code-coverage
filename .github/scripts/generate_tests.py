import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from openai import OpenAI

def get_coverage_percentage():
    tree = ET.parse('coverage.xml')
    root = tree.getroot()
    return float(root.attrib['line-rate']) * 100

def generate_tests(source_code):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    prompt = f"""
    Given the following Python code, generate comprehensive unit tests:
    
    {source_code}
    
    Generate pytest-style unit tests that achieve high coverage.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Python testing expert."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def main():
    coverage = get_coverage_percentage()
    
    if coverage < 80:
        print(f"Current coverage: {coverage}%. Generating additional tests...")
        
        # Read source code
        with open('src/calculator.py', 'r') as f:
            source_code = f.read()
        
        # Generate new tests
        new_tests = generate_tests(source_code)
        
        # Append new tests to existing test file
        test_file = Path('tests/test_calculator.py')
        with open(test_file, 'a') as f:
            f.write('\n\n# Auto-generated tests\n')
            f.write(new_tests)
        
        print("New tests have been generated and added to test_calculator.py")
        
    else:
        print(f"Current coverage: {coverage}%. No additional tests needed.")

if __name__ == "__main__":
    main()