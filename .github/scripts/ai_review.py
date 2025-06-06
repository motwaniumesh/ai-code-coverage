import os
from openai import OpenAI
from github import Github

def get_ai_review(diff):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    prompt = f"""Act as a senior code reviewer. Analyze this code diff and provide:
    1. Potential issues
    2. Security concerns
    3. Code quality improvements
    4. Alternative approaches
    5. Documentation suggestions
    
    Format response in Markdown. Be concise but thorough.
    
    Diff:
    {diff[:7500]}  # Truncate to avoid token limits
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].message.content

def post_comment(comment):
    g = Github(os.environ['GITHUB_TOKEN'])
    repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
    pr = repo.get_pull(int(os.environ['PR_NUMBER']))
    try:
        pr.create_issue_comment(f"## 🤖 AI Code Review\n\n{comment}")
    except Exception as e:
        print(f"Failed to post comment: {str(e)}")
        raise

if __name__ == "__main__":
    diff = os.getenv('DIFF', '')
    if not diff:
        with open('diff.patch', 'r') as f:
            diff = f.read()
    
 
    review = get_ai_review(diff)
    post_comment(review)