# SDK Installation and Test

This guide will walk you through the steps to install the AI Refinery SDK wheel package for your project, and test the installation, account, and API key.

### Prerequisites

- <span style="color:red; font-weight:bold;">Python 3.12</span>
- Account
- API Key
- File airefinery_sdk-1.1.1-py3-none-any.whl

## Preliminary Steps

Open a terminal (or command prompt on Windows) and create a folder named gardening for this project.

```bash
mkdir gardening
```

Switch to the new directory:

```bash
cd gardening
```

Now, ensure the SDK wheel file (.whl) corresponding to version <span style="color:red; font-weight:bold;">1.1.1</span> in available and copy it to the current directory


Create a virtual environment by running the following command. On macOS, use `python3` or `python3.12` instead of `python`, if available:

```sh
python -m venv .venv
```

Then, activate the virtual environment:
#### Windows
In Command Prompt or PowerShell, run:
```sh
.venv\Scripts\activate
```
#### macOS
In Terminal, run:
```sh
source .venv/bin/activate
```


## SDK Installation


Run the following command to install the SDK and other requirements:
```sh
pip install airefinery_sdk-1.1.1-py3-none-any.whl python-dotenv websockets==12.0
```


---

## Testing the Account and Installation
After completing the SDK installation, you can check if the setup works correctly and that you can log in to AI Refinery.

For this purpose, you'll create a simple test script (`main.py`) and a configuration file (`config.yaml`) by following the instructions below. At this stage, focus on running the script rather than on its details.

### 1. Environment Configuration
Create a file named `.env` in the root directory of your project. This file should contain the following variables:
- **`ACCOUNT`**: Your account identifier.
- **`API_KEY`**: Your API key for authentication.

#### **Example `.env` File:**
```env
ACCOUNT=your_account_identifier
API_KEY=your_api_key
```

> ⚠️ **Note:** Ensure the `.env` file is not included in version control as it contains sensitive information.

Here’s how you can structure the sections for the `README.md` file to include instructions for the `config.yaml` file and the `main.py` script:

---

### 2. Configuration File (`config.yaml`)

Create a file named `config.yaml` in the root directory of your project with the following content:

```yaml
utility_agents:
  - agent_class: SearchAgent
    agent_name: "Garden Scout"
    agent_description:
      The Garden Scout can search the Web for relevant gardening information
      such as how often plants should be watered, the best watering methods, and
      how deep and far apart should seeds be planted
    config:
      output_style: "conversational"
      contexts:
        - "chat_history"

orchestrator:
  agent_list:
    - agent_name: "Garden Scout"
```

---

### 3. Python Script (`main.py`)

Create a file named `main.py` in your project directory with the following content:

```python
from dotenv import load_dotenv
from air import login, DistillerClient
import os

load_dotenv()  # This loads your ACCOUNT and API_KEY from your local '.env' file

account = os.environ["ACCOUNT"]
api_key = os.environ["API_KEY"]
user_id = account.replace("-", "_") + "test"  # Replace 'test' by your Accenture ID
project = "gardening_project"
config_path = "config.yaml"

login(account, api_key)

distiller_client = DistillerClient()

distiller_client.create_project(
    config_path=config_path,
    project=project
)

response = distiller_client.interactive(
    project=project,
    uuid=user_id,
)
```

> ⚠️ **Note:** In the line that generates a `user_id` using the account information, replace "test" with a unique identifier. You can use only letters, numbers, and underscores (_)

---

### 5. Testing the Code

Ensure `.env`, `config.yaml`, and `main.py` are all in the project's root directory, and that your virtual environment is activated.

Run the python script:

```bash
python main.py
```

If the installation is successful and your credentials are correct, you'll be prompted to send a query to the single-agent system described in the `config.yaml` file.

