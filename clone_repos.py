import os

repo_file = "templates-repos.txt"

clone_dir = "community-templates"

with open(repo_file, 'r') as file:
    repos = [line.strip() for line in file if line.strip()]

print("***************************************************")
print("Nuclei Template Cloning Script")
print("GitHub: Shubham-rooter")
print("***************************************************")

print("Script by Shubham-rooter")

for repo in repos:
    os.system(f"git clone {repo} {clone_dir}/{os.path.basename(repo)}")
