#README: Create Read me

# Artifactory CLI

This command-line tool interacts with JFrog Artifactory to perform common administrative tasks such as checking system status, retrieving version information, creating users, listing repositories, and viewing storage details.

## Features
- **Ping Artifactory**: Verify if the Artifactory instance is online.
- **Retrieve Version**: Get the version of the Artifactory system.
- **Create Users**: Add new users with specified credentials.
- **Get Storage Information**: View storage details of the Artifactory instance.
- **List Repositories**: List all repositories in Artifactory.

## Prerequisites

- Python 3.7 or above


## Usage

Run the script using the following format:
```bash
python main.py <base_url> <username> <password> <command> [command arguments]
```

### Commands

#### Ping
Check if the Artifactory instance is online.
```bash
python main.py <base_url> <username> <password> ping
```

#### Version
Retrieve the version information of the Artifactory system.
```bash
python main.py <base_url> <username> <password> version
```

#### Create User
Create a new user with specified username, password, and email.
```bash
python main.py <base_url> <username> <password> create-user <new_username> <new_password> <email>
```

Example:
```bash
python main.py https://example.jfrog.io/artifactory admin admin123 create-user new_user new_password user@example.com
```

#### Storage Info
Get storage details of the Artifactory instance.
```bash
python main.py <base_url> <username> <password> storage-info
```

#### List Repositories
List all repositories available in the Artifactory instance.
```bash
python main.py <base_url> <username> <password> list-repos
```

### Example Usage

1. **Ping Artifactory**:
   ```bash
   python main.py https://example.jfrog.io/artifactory admin admin123 ping
   ```

2. **Retrieve Version**:
   ```bash
   python main.py https://example.jfrog.io/artifactory admin admin123 version
   ```

3. **Create a User**:
   ```bash
   python main.py https://example.jfrog.io/artifactory admin admin123 create-user john_doe password123 john@example.com
   ```

4. **Get Storage Info**:
   ```bash
   python main.py https://example.jfrog.io/artifactory admin admin123 storage-info
   ```

5. **List Repositories**:
   ```bash
   python main.py https://example.jfrog.io/artifactory admin admin123 list-repos
   ```

## Sources
This project was built using the following resources:
- [JFrog Artifactory REST API Documentation](https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API)
- [pyartifactory GitHub Repository](https://github.com/anancarv/python-artifactory)
- Example CLI project for JFrog Artifactory: [jfrog-cli](https://github.com/jfrog/jfrog-cli)
- [Real Python: Interacting With REST APIs in Python](https://realpython.com/api-integration-in-python/)