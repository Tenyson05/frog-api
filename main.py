import requests
import argparse

class ArtifactoryCLI:
    #TODO: add authentication
    def __init__(self, base_url, username, password):
        self.base_url = base_url.rstrip('/')
        self.auth = (username, password)

    #TODO: add ping functionality
    def system_ping(self):
        """Ping the Artifactory system."""
        try:
            url = f"{self.base_url}/api/system/ping"
            response = requests.get(url, auth=self.auth)
            if response.status_code == 200 and response.text == "OK":
                print("Artifactory is alive.")
            else:
                print(f"Ping failed with status {response.status_code}: {response.text}")
        except Exception as e:
            print(f"Ping failed: {e}")

    #TODO: add system version
    def system_version(self):
        """Get the Artifactory system version."""
        try:
            url = f"{self.base_url}/api/system/version"
            response = requests.get(url, auth=self.auth)
            if response.status_code == 200:
                print("System Version:", response.json())
            else:
                print(f"Failed to get version with status {response.status_code}: {response.text}")
        except Exception as e:
            print(f"Failed to get version: {e}")

    #TODO: add create user
    def create_user(self, username, password, email):
        """Create a new user."""
        try:
            url = f"{self.base_url}/api/security/users/{username}"
            payload = {
                "email": email,
                "password": password,
                "admin": False
            }
            response = requests.put(url, json=payload, auth=self.auth)
            if response.status_code == 201:
                print(f"User {username} created successfully.")
            else:
                print(f"Failed to create user with status {response.status_code}: {response.text}")
        except Exception as e:
            print(f"Failed to create user: {e}")

    #TODO: add storage info
    def get_storage_info(self):
        """Retrieve storage information."""
        try:
            url = f"{self.base_url}/api/storageinfo"
            response = requests.get(url, auth=self.auth)
            if response.status_code == 200:
                print("Storage Info:", response.json())
            else:
                print(f"Failed to get storage info with status {response.status_code}: {response.text}")
        except Exception as e:
            print(f"Failed to get storage info: {e}")

    #TODO: add list repository
    def list_repositories(self):
        """List all repositories in the Artifactory instance."""
        try:
            url = f"{self.base_url}/api/repositories"
            response = requests.get(url, auth=self.auth)
            if response.status_code == 200:
                repositories = response.json()
                print("Repositories:")
                for repo in repositories:
                    print(f"- {repo['key']}: {repo['type']}")
            else:
                print(f"Failed to list repositories with status {response.status_code}: {response.text}")
        except Exception as e:
            print(f"Failed to list repositories: {e}")

#TODO: add mian function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Artifactory CLI")
    parser.add_argument("base_url", help="Base URL of the Artifactory instance")
    parser.add_argument("username", help="Artifactory username")
    parser.add_argument("password", help="Artifactory password")

    subparsers = parser.add_subparsers(dest="command")

    # Ping command
    subparsers.add_parser("ping")

    # Version command
    subparsers.add_parser("version")

    # Create user command
    create_user_parser = subparsers.add_parser("create-user")
    create_user_parser.add_argument("username", help="Username of the new user")
    create_user_parser.add_argument("password", help="Password for the new user")
    create_user_parser.add_argument("email", help="Email for the new user")

    # Storage info command
    subparsers.add_parser("storage-info")

    # List repositories command
    subparsers.add_parser("list-repos")

    args = parser.parse_args()

    cli = ArtifactoryCLI(args.base_url, args.username, args.password)

    if args.command == "ping":
        cli.system_ping()
    elif args.command == "version":
        cli.system_version()
    elif args.command == "create-user":
        cli.create_user(args.username, args.password, args.email)
    elif args.command == "storage-info":
        cli.get_storage_info()
    elif args.command == "list-repos":
        cli.list_repositories()
    else:
        print("Unknown command.")