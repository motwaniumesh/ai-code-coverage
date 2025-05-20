import os
import sys
import glob
import xml.etree.ElementTree as ET
from pathlib import Path
from openai import OpenAI
import ast

class TestGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.src_dir = 'src'
        self.tests_dir = 'tests'

    def get_coverage_percentage(self) -> float:
        """Get the overall coverage percentage from coverage.xml"""
        tree = ET.parse('coverage.xml')
        root = tree.getroot()
        return float(root.attrib['line-rate']) * 100

    def get_file_coverage(self) -> dict:
        """Get coverage percentage for each source file"""
        tree = ET.parse('coverage.xml')
        root = tree.getroot()
        coverage_data = {}
        
        for class_node in root.findall(".//class"):
            filename = class_node.attrib['filename']
            if filename.startswith('src/'):
                line_rate = float(class_node.attrib['line-rate']) * 100
                coverage_data[filename] = line_rate
        
        return coverage_data

    def generate_tests_for_file(self, source_path: str) -> str:
        """Generate tests for a specific source file"""
        with open(source_path, 'r') as f:
            source_code = f.read()
        
        prompt = f"""
        Generate pytest unit tests for the following Python code.
        Return ONLY the test code, no explanations.
        Each test function should start with 'def test_' and use proper pytest assertions.
        Include tests for edge cases and error conditions.
        
        Source code:
        {source_code}
        """
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Python testing expert. Provide only valid Python test code."},
                {"role": "user", "content": prompt}
            ]
        )
        
        generated_tests = response.choices[0].message.content.strip()
        
        # Clean up the response
        if generated_tests.startswith("```python"):
            generated_tests = generated_tests.replace("```python", "").replace("```", "")
        
        return generated_tests.strip()

    def validate_python_code(self, code: str) -> bool:
        """Validate if the generated code is valid Python"""
        try:
            ast.parse(code)
            return True
        except SyntaxError:
            return False

    def update_test_file(self, source_path: str, generated_tests: str):
        """Update or create test file for a source file"""
        source_filename = os.path.basename(source_path)
        test_filename = f"test_{source_filename}"
        test_path = os.path.join(self.tests_dir, test_filename)
        
        # Create test file if it doesn't exist
        if not os.path.exists(test_path):
            with open(test_path, 'w') as f:
                f.write(f"import pytest\nfrom {self.src_dir}.{source_filename[:-3]} import *\n\n")
        
        # Append new tests
        with open(test_path, 'a') as f:
            f.write("\n# Auto-generated tests\n")
            f.write(generated_tests)
            f.write("\n")

    def push_changes(self):
        """Push changes to GitHub"""
        pat_token = os.getenv('PAT_TOKEN')
        repo_url = os.getenv('GITHUB_REPOSITORY')
        branch_name = f"feature/add-tests-{os.getenv('GITHUB_SHA', '')[:7]}"
        
        os.system('git config --global user.email "ai-agent@example.com"')
        os.system('git config --global user.name "AI Test Generator"')
        os.system(f'git checkout -b {branch_name}')
        os.system('git add tests/')
        os.system('git commit -m "Add generated tests to improve coverage"')
        
        push_url = f"https://x-access-token:{pat_token}@github.com/{repo_url}.git"
        os.system(f'git push {push_url} {branch_name}')

    def run(self):
        """Main execution method"""
        overall_coverage = self.get_coverage_percentage()
        file_coverage = self.get_file_coverage()
        
        if overall_coverage >= 80:
            print(f"Overall coverage is {overall_coverage}%. No additional tests needed.")
            return
        
        print(f"Current coverage: {overall_coverage}%. Generating additional tests...")
        
        # Process each source file with low coverage
        for source_file, coverage in file_coverage.items():
            if coverage < 80:
                print(f"Generating tests for {source_file} (coverage: {coverage}%)")
                source_path = source_file
                generated_tests = self.generate_tests_for_file(source_path)
                
                if self.validate_python_code(generated_tests):
                    self.update_test_file(source_path, generated_tests)
                else:
                    print(f"Generated tests for {source_file} contain syntax errors")
        
        self.push_changes()

def main():
    generator = TestGenerator()
    generator.run()

if __name__ == "__main__":
    main()