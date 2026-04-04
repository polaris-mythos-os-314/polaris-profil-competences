import os

# Function to configure repositories using GitHub CLI

def configure_repositories(repos):
    for repo in repos:
        os.system(f'gh repo clone {repo}')  # Clone the repository
        os.system(f'cd {repo} && git checkout -b new-config')  # Create new config branch
        # Additional configuration commands can be added here

if __name__ == '__main__':
    repositories = [
        'user/repo1',  # Replace with actual repository names
        'user/repo2',
        'user/repo3'
    ]
    configure_repositories(repositories)