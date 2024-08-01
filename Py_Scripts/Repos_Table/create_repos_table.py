import requests

def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    return response.json()

def generate_markdown_table(repos):
    table = "| Repository Name | Description | Stars | Forks |\n"
    table += "|-----------------|-------------|-------|-------|\n"
    
    for repo in repos:
        name = repo['name']
        description = repo['description'] or "No description"
        stars = repo['stargazers_count']
        forks = repo['forks_count']
        repo_url = repo['html_url']
        
        table += f"| [{name}]({repo_url}) | {description} | ![Stars](https://img.shields.io/github/stars/{username}/{name}) | ![Forks](https://img.shields.io/github/forks/{username}/{name}) |\n"
    
    return table

username = "jeturgavli"
repos = fetch_repos(username)
markdown_table = generate_markdown_table(repos)

with open("REPO_TABLE.md", "r", encoding="utf-8") as file:
    lines = file.readlines()

start_index = lines.index("<!-- repos start -->\n") + 1
end_index = lines.index("<!-- repos end -->\n")

new_lines = lines[:start_index] + [markdown_table] + lines[end_index:]

with open("REPO_TABLE.md", "w", encoding="utf-8") as file:
    file.writelines(new_lines)
