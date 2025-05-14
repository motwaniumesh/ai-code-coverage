import os
import sys
import xml.etree.ElementTree as ET
import openai
from pathlib import Path

def get_coverage_percentage():
    tree = ET.parse('coverage.xml')
    root = tree.getroot()
    return float(root.attrib['line-rate']) * 100

def generate_tests(source_code):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    prompt = f"""
    Given the following Python code, generate comprehensive unit tests:
    
    {source_code}
    
    Generate pytest-style unit tests that achieve high coverage.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
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
        
        # Create a new branch and commit changes
        # os.system('git config --global user.email "umesh.motwani@slalom.com"')
        # os.system('git config --global user.name "AI Test Generator"')
        # os.system('git checkout -b feature/add-tests')
        # os.system('git add tests/test_calculator.py')
        # os.system('git commit -m "Add generated tests to improve coverage"')
        # os.system('git push origin feature/add-tests')
        
    else:
        print(f"Current coverage: {coverage}%. No additional tests needed.")

if __name__ == "__main__":
    main()