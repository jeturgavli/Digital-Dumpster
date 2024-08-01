import os
import requests

def fetch_repos():
    username = "jeturgavli"  # Replace with your GitHub username
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        # Filter out forked repos and include only public ones
        return [repo for repo in response.json() if not repo['fork'] and repo['private'] == False]
    else:
        print(f"Error fetching repos: {response.status_code}")
        print(response.text)
        return []

def generate_markdown_table(repos):
    markdown_table = "| Name | Description | URL |\n|------|-------------|-----|\n"
    for repo in repos:
        markdown_table += f"| {repo['name']} | {repo['description'] or 'No description'} | [Link]({repo['html_url']}) |\n"
    return markdown_table

def update_readme(table):
    readme_path = "Py_Scripts/Repos_Table/REPO_TABLE.md"
    try:
        # Read the current content of the file with UTF-8 encoding
        with open(readme_path, "r", encoding="utf-8") as file:
            readme = file.readlines()

        # Find the start and end markers for the table
        start_index = next((i for i, line in enumerate(readme) if line.strip() == "<!-- REPOS-START -->"), None)
        end_index = next((i for i, line in enumerate(readme) if line.strip() == "<!-- REPOS-END -->"), None)

        if start_index is None:
            # Add the start marker if not found
            readme.append("<!-- REPOS-START -->\n")
            start_index = len(readme) - 1
        if end_index is None:
            # Add the end marker if not found
            readme.append("<!-- REPOS-END -->\n")
            end_index = len(readme) - 1
        
        # Update the content between the markers
        new_readme = readme[:start_index + 1] + [table] + readme[end_index:]

        # Write the updated content back to the file with UTF-8 encoding
        with open(readme_path, "w", encoding="utf-8") as file:
            file.writelines(new_readme)
        
        print("Generated Markdown Table:")
        print(table)
        print("REPO_TABLE.md updated successfully.")
    except Exception as e:
        print(f"Error updating REPO_TABLE.md: {e}")

if __name__ == "__main__":
    repos = fetch_repos()
    if repos:
        markdown_table = generate_markdown_table(repos)
        update_readme(markdown_table)
    else:
        print("No repositories found or failed to fetch repositories.")
