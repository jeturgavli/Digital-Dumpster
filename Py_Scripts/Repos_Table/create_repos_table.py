import requests
import os

def fetch_repos():
    username = "jeturgavli"
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching repos: {response.status_code}")
        print(response.text)
        return []

def generate_markdown_table(repos):
    markdown_table = "| Name | Description | URL |\n|------|-------------|-----|\n"
    for repo in repos:
        markdown_table += f"| {repo['name']} | {repo['description']} | {repo['html_url']} |\n"
    return markdown_table

def update_readme(table):
    try:
        with open("README.md", "r") as file:
            readme = file.readlines()

        start_index = readme.index("<!-- REPOS-START -->\n")
        end_index = readme.index("<!-- REPOS-END -->\n")

        new_readme = readme[:start_index + 1] + [table] + readme[end_index:]

        with open("README.md", "w") as file:
            file.writelines(new_readme)
        print("README.md updated successfully.")
    except Exception as e:
        print(f"Error updating README.md: {e}")

if __name__ == "__main__":
    repos = fetch_repos()
    if repos:
        markdown_table = generate_markdown_table(repos)
        update_readme(markdown_table)
    else:
        print("No repositories found or failed to fetch repositories.")
