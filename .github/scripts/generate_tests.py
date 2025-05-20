import os
import xml.etree.ElementTree as ET
from pathlib import Path
from openai import OpenAI
from datetime import datetime

def get_low_coverage_files(min_coverage=80):
    """Return files with coverage below threshold with their coverage percentages"""
    tree = ET.parse('coverage.xml')
    root = tree.getroot()
    
    low_coverage = {}
    
    # Parse coverage data for each file
    for package in root.findall('packages/package'):
        for cls in package.findall('classes/class'):
            filename = cls.attrib['filename']
            line_rate = float(cls.attrib['line-rate']) * 100
            if line_rate < min_coverage:
                # Convert relative path to src path
                src_path = str(Path('src') / filename).replace('.py', '')
                low_coverage[src_path] = line_rate
                
    return low_coverage

def generate_tests(source_code, filename):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    prompt = f"""
    Given the following Python code from {filename}, generate comprehensive pytest unit tests.
    Requirements:
    - Return ONLY the test code
    - Use pytest conventions
    - Test class should match filename (test_<original>.py)
    - Include proper imports
    - Cover edge cases and error handling
    
    Code:
    {source_code}
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Python testing expert. Provide only valid Python test code."},
            {"role": "user", "content": prompt}
        ]
    )
    
    generated_tests = response.choices[0].message.content.strip()
    
    # Clean markdown and ensure proper test file structure
    if generated_tests.startswith("```python"):
        generated_tests = generated_tests[9:-3].strip()
    
    return generated_tests

def push_changes(test_files):
    pat_token = os.getenv('PAT_TOKEN')
    repo_url = os.getenv('GITHUB_REPOSITORY')
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    os.system('git config --global user.email "ai-agent@example.com"')
    os.system('git config --global user.name "AI Test Generator"')
    
    branch_name = f"tests/auto-tests-{timestamp}"
    os.system(f'git checkout -b {branch_name}')
    
    # Add all modified test files
    for test_file in test_files:
        os.system(f'git add {test_file}')
    
    os.system(f'git commit -m "Auto-generated tests for {", ".join(test_files)}"')
    
    push_url = f"https://x-access-token:{pat_token}@github.com/{repo_url}.git"
    os.system(f'git push {push_url} {branch_name}')

def process_file(src_path, coverage_percent):
    """Handle test generation for a single source file"""
    print(f"Processing {src_path} (coverage: {coverage_percent:.1f}%)")
    
    # Read source code
    with open(f'{src_path}.py', 'r') as f:
        source_code = f.read()
    
    # Generate new tests
    new_tests = generate_tests(source_code, src_path)
    
    # Determine test file path
    test_filename = f"test_{Path(src_path).name}.py"
    test_path = Path('tests') / test_filename
    
    # Ensure test directory exists
    test_path.parent.mkdir(exist_ok=True)
    
    # Write/append tests
    with open(test_path, 'a' if test_path.exists() else 'w') as f:
        if not test_path.exists():
            f.write(f"# Tests for {src_path}.py\n\n")
        f.write(f"\n\n# Auto-generated tests ({datetime.now().isoformat()})\n")
        f.write(new_tests)
    
    return str(test_path)

def main():
    low_coverage = get_low_coverage_files(min_coverage=80)
    
    if not low_coverage:
        print("All files meet coverage requirements")
        return
    
    processed_files = []
    
    for src_path, coverage in low_coverage.items():
        try:
            test_file = process_file(src_path, coverage)
            processed_files.append(test_file)
        except Exception as e:
            print(f"Failed processing {src_path}: {str(e)}")
    
    if processed_files:
        push_changes(processed_files)
        print(f"Generated tests for: {', '.join(processed_files)}")
    else:
        print("No tests generated due to errors")

if __name__ == "__main__":
    main()