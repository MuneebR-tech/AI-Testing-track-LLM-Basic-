import os
import subprocess
import sys

def run_command(cmd):
    try:
        res = subprocess.run(cmd, shell=True, check=True, text=True, capture_output=True)
        return True, res.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip()

def setup_git():
    print("=" * 60)
    print("GITHUB UPLOAD AND GIT SETUP TOOL")
    print("=" * 60)

    success, ver = run_command("git --version")
    if not success:
        print("Error: Git is not installed or not found in system PATH.")
        print("Please install Git from https://git-scm.com/ and try again.")
        sys.exit(1)
        
    print(f"Detected: {ver}")

    gitignore_content = """# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Python Cache
__pycache__/
*.py[cod]
*$py.class

# IDEs
.idea/
.vscode/
*.suo
*.ntvs*
*.njsproj
*.sln
*.swp

# Reports & Artifacts
# report.html
# report.pdf
"""
    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content)
    print("Created .gitignore file.")

    if not os.path.exists(".git"):
        success, out = run_command("git init")
        if success:
            print("Initialized local Git repository.")
        else:
            print(f"Failed to init Git: {out}")
            sys.exit(1)
    else:
        print("Git repository already initialized.")

    run_command("git add .")
    print("Staged all project files.")

    success, out = run_command('git commit -m "feat: complete AI testing track framework implementation"')
    if success:
        print("Created initial commit successfully.")
    else:
        if "nothing to commit" in out.lower():
            print("No new changes to commit.")
        else:
            print(f"Failed to commit: {out}")

    print("\n" + "-" * 50)
    repo_url = input("Enter your GitHub repository URL (e.g. https://github.com/user/repo.git): ").strip()
    if not repo_url:
        print("No URL provided. You can manually link your remote later using:")
        print("git remote add origin <YOUR_REPO_URL>")
        print("git push -u origin main")
        sys.exit(0)

    run_command("git remote remove origin")
    success, out = run_command(f"git remote add origin {repo_url}")
    if success:
        print(f"Linked remote origin to: {repo_url}")
    else:
        print(f"Failed to add remote: {out}")
        sys.exit(1)

    run_command("git branch -M main")

    print("\n" + "=" * 60)
    print("GIT REPOSITORY SETUP COMPLETE")
    print("=" * 60)
    print("To upload your files to GitHub, run the following command in your terminal:")
    print("git push -u origin main")
    print("=" * 60 + "\n")

    push_now = input("Would you like to try pushing now? (y/n): ").strip().lower()
    if push_now == "y":
        print("Attempting to push... (This may open an authentication prompt)")
        success, out = run_command("git push -u origin main")
        if success:
            print("Successfully pushed to GitHub!")
        else:
            print("\nPush failed. This is usually due to authentication requirements.")
            print("Please open your terminal inside this directory and run:")
            print("git push -u origin main")
            print("And sign in when prompted by Git.")

if __name__ == "__main__":
    setup_git()
