
# Step-by-Step Guide: Setting Up DeepSeek-R1 with Ollama on Your VPS 🌐🤖

## Introduction

DeepSeek-R1 has been making waves in the AI community 🚀. Developed by the Chinese company DeepSeek 🇨🇳, this open-source model offers performance on par with top AI models, and the best part is you can run it locally on your machine 🖥️. In this guide, we'll walk you through the process of setting up DeepSeek-R1 on your VPS using Ollama 🛠️, a powerful platform designed to simplify running AI models locally.

## Why Choose DeepSeek-R1? 🤔

DeepSeek-R1 is an open-source AI model 🔓 that’s gaining traction due to its high performance and versatility. It can be used for a wide range of tasks such as natural language processing 🧠 and machine learning 📊. By choosing DeepSeek-R1, you gain access to cutting-edge AI capabilities without the restrictions of proprietary platforms 💼.

## What is Ollama?

Ollama is a user-friendly platform designed to simplify running AI models on your machine. Unlike cloud-based solutions, Ollama enables you to download and execute models directly on your system, offering more control, privacy, and flexibility 🛠️. It supports various AI models, including DeepSeek-R1, making it an excellent choice for running and experimenting with powerful machine learning models locally.

## Prerequisites

Before you begin, make sure your VPS is set up with:

- A Linux-based operating system (Ubuntu, CentOS, etc.).
- Python and pip installed. If not, follow the instructions below.
- Access to the command line interface with `sudo` privileges.

## Step 1: Install Ollama

1. Visit the [Ollama website](https://ollama.com) and download the installer for your operating system (Windows, macOS, or Linux).
2. Follow the installation instructions to install Ollama on your machine.

## Step 2: Download DeepSeek-R1 Model

Once Ollama is installed, you can download the DeepSeek-R1 model:

1. Choose a model version from [Ollama's library](https://ollama.com/library/deepseek-r1:7b). For this guide, we will use the 7b version, which is a balanced choice between performance and resource requirements.

2. Run the following command to download the model:

    ```bash
    ollama run deepseek-r1
    ```

    This will download the DeepSeek-R1 model to your system.

## Step 3: Verify Installation

To verify that the model has been installed correctly, run:

```bash
ollama list
```

This will display the list of installed models.

## Step 4: Run DeepSeek-R1

To start using DeepSeek-R1, simply run:

```bash
ollama run deepseek-r1
```

This will launch the DeepSeek-R1 model and make it ready for use.

## Step 5: Set Up the User Interface for Testing

After the model is running, you can test it and interact with it using Ollama's built-in user interface.

1. Ensure that Python and pip are installed on your VPS. To check the versions of Python and pip, run:

    ```bash
    python --version
    pip --version
    ```

2. Install the necessary dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

3. Clone the repository that contains the DeepSeek-R1 user interface:

    ```bash
    git clone https://github.com/prashant1879/Step-by-Step-Guide-Setting-Up-DeepSeek-R1-with-Ollama-on-Your-VPS
    ```

4. Navigate to the repository folder:

    ```bash
    cd Step-by-Step-Guide-Setting-Up-DeepSeek-R1-with-Ollama-on-Your-VPS
    ```

5. Start the server using Gunicorn (replace `XX.XX.XX.XX` with your VPS’s public IP address):

    ```bash
    gunicorn --workers 3 --bind XX.XX.XX.XX:8000 app:app
    ```

6. You can now access the DeepSeek-R1 user interface at:

    ```
    http://XX.XX.XX.XX:8000
    ```

    This interface allows you to input prompts, adjust settings, and test the model's capabilities.

## Conclusion

By following this guide, you’ve set up DeepSeek-R1 with Ollama on your VPS. Now you can experiment with this powerful AI model locally without relying on cloud-based services. Whether you’re a developer, researcher, or AI enthusiast, this setup provides a great way to interact with cutting-edge AI technology 🚀.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Want to Learn More? 🤓

If you're interested in diving deeper into Node.js, DevOps, and other tech topics, follow me on Medium for more insightful articles and guides! ✨

👉 [Follow me on Medium!](https://prashant1879.medium.com/) 📚

Stay tuned and keep coding! 👨‍💻👩‍💻
```
