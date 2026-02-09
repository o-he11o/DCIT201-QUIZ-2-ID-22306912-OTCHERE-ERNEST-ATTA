#!/usr/bin/env python3
import urllib.request
import urllib.error
import json
import sys
import os

def create_pull_request():
    token = os.environ.get('GITHUB_TOKEN', '')
    if not token:
        print("Error: GITHUB_TOKEN not set")
        print("Please provide a GitHub Personal Access Token.")
        print("\nTo create a token: https://github.com/settings/tokens")
        print("Then run: export GITHUB_TOKEN=your_token")
        return False
    url = "https://api.github.com/repos/o-he11o/DCIT201-QUIZ-2-ID-22306912-OTCHERE-ERNEST-ATTA/pulls"
    
    data = json.dumps({
        "title": "Add Java classes for class average calculation and student grading",
        "head": "blackboxai/add-java-class-average-grading",
        "base": "main",
        "body": "This PR adds Java classes for:\n\n- **ClassAverageCalculation.java**: Calculates class averages with overloaded methods (2 scores, 3 scores, and array of scores)\n- **StudentGrading.java**: Validates scores and calculates letter grades (A-F) with grade boundaries\n- **Main.java**: Test class to run both programs with sample data\n- **run_output.sh**: Shell script that simulates the Java program output (since Java runtime is not available on the system)\n\n## Expected Output\n```\n=== ClassAverageCalculation Tests ===\nAverage of 2 scores (85.5, 92.0): 88.75\nAverage of 3 scores (75.0, 82.5, 90.0): 82.5\nAverage of array [70.0, 85.0, 90.0, 95.0, 80.0]: 84.0\n\n=== StudentGrading Tests ===\nScore: 95.0 -> A\nScore: 82.5 -> B\nScore: 72.0 -> B\nScore: 65.0 -> C\nScore: 55.0 -> D\nScore: 48.0 -> E\nScore: 42.0 -> F\nScore: -5.0 -> Invalid Score\n```"
    }).encode('utf-8')
    
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json",
        "Authorization": f"token {token}"
    }
    
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            print("Pull Request created successfully!")
            print(f"PR URL: {result.get('html_url', 'N/A')}")
            print(f"PR Number: {result.get('number', 'N/A')}")
            return True
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8') if e.read else ""
        print(f"HTTP Error {e.code}: {e.reason}")
        print(f"Response: {error_body}")
        if e.code == 401:
            print("\nTo create the PR, you need to authenticate.")
            print("Please provide a GitHub Personal Access Token.")
            print("\nYou can create one at: https://github.com/settings/tokens")
            print("Then run:")
            print(f'curl -X POST -H "Authorization: token YOUR_TOKEN" \\')
            print(f'  -H "Accept: application/vnd.github.v3+json" \\')
            print(f'  -d \'{{"title":"Add Java classes for class average calculation and student grading","head":"blackboxai/add-java-class-average-grading","base":"main","body":"This PR adds Java classes..."}}\' \\')
            print(f'  "{url}"')
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    create_pull_request()

