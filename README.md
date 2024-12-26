# 🎹 Chat Piano Tool Server

This repository hosts the Chat Piano API server, providing an efficient and scalable solution for managing and expanding tool-based services. Chat Piano leverages advanced AI models to interpret voice commands and convert them into MIDI files, facilitating seamless interactions between users and digital music creation platforms.

## 🌟 Features

- **Modular Tool Integration:** Easily add new tools to the system while maintaining high scalability and performance.
- **Scalability:** Designed to handle growth with minimal effort, ensuring consistent performance as more tools are added.
- **Package Management:** Simplifies installation and updates via pip tools. Publishing to PyPI is planned for the future.
- **Standard OpenAI Tool Definition:** Utilizes OpenAI's standardized tool definition formats, ensuring compatibility and ease of integration into AI workflows.

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- Docker (optional for containerized deployment)
- [uv](https://uv.tools/) (optional for advanced synchronization and management)

### Choices

<details>
<summary>Local Installation - Set up directly on your machine</summary>

This section provides detailed steps to install the project locally. Ideal for developers or testers who wish to modify and run the tool on their machines.

1. Clone the repository recursively to include all submodules:
   ```bash
   git clone git@github.com:yhbcode000/ChatPiano.git
   cd ChatPiano
   ```

2. Install the package in editable mode to allow changes:
   ```bash
   pip install -e .
   ```

3. Start the Chat Piano tool server:
   ```bash
   start-chatpiano
   ```
   After this, the server will start and provide a URL for API interaction.
</details>

<details>
<summary>Using uv - Enhanced project synchronization and management</summary>

The `uv` tool provides a streamlined way to manage synchronization and ensure optimal configurations for running the project.

1. Sync the project to ensure all dependencies and configurations are up-to-date:
   ```bash
   uv sync
   ```

2. Run the server with the `uv` management tool:
   ```bash
   uv run python -m chat_piano
   ```
   This command ensures the application is running with the best possible setup provided by `uv`.
</details>

<details>
<summary>Docker Setup - Containerized deployment for isolated environments</summary>

Use Docker to encapsulate the project and its dependencies for an isolated and consistent environment. This is the recommended approach for production use.

1. Build the Docker container locally:
   ```bash
   docker build -t chat-piano .
   ```

2. Run the container in detached mode:
   ```bash
   docker run -d --name chat-piano-instance chat-piano
   ```

> 📝 **Note:** The Docker image includes all dependencies, ensuring a consistent and isolated environment. For production use, consider pulling the pre-built image to save time.
</details>

<details>
<summary>Pull Pre-Built Docker Image - Quick setup using a pre-built image</summary>

For quicker setup and deployment, use a pre-built Docker image hosted on Docker Hub.

1. Pull the image directly from Docker Hub:
   ```bash
   docker pull TODO-TO-BE-ANNOUNCED
   ```

2. Create a container from the pulled image:
   ```bash
   docker run -d --name chat-piano-instance TODO-TO-BE-ANNOUNCED
   ```

3. Optionally, set up the Docker service for managed deployment:
   ```bash
   docker service create --name chat-piano-service TODO-TO-BE-ANNOUNCED
   ```
   This approach is ideal for scaling and orchestrating multiple instances efficiently.
</details>

## 📖 Usage

Once the server starts, you can access the API documentation via the provided link in the console output. Use the documentation to explore and interact with the APIs.

### Example

1. Start the server locally or via Docker.
2. Visit `http://localhost:5000` (or the server's actual address) to access the interactive API documentation.
3. Test endpoints directly from the documentation or integrate the APIs into your application.

## 🤝 Contributing

We welcome contributions from the community. Here are some ways you can contribute:

- Report bugs or suggest features by opening issues.
- Submit pull requests for fixes or new tools.
- Share feedback and ideas for improvement.

<details>
<summary>Adding Tools to the Repository - Extend the functionality with new tools</summary>

To add a new tool to the Chat Piano system, follow these steps:

1. **Configure the Tool in `__init__.py`:**
   Add your tool configuration to `chat_piano/tools/__init__.py` to register it in the system.

2. **Create the Tool's Python File:**
   Place your Python file in the `chat_piano/tools` folder. This file should define the tool's functionality and follow these guidelines:
   - Always return a string to ensure the AI agent receives feedback from the tool.
   - Use a non-blocking thread for any long-running algorithms to avoid stalling the main process.

3. **Implement Status and Results Handling:**
   - Provide a method for checking the tool's status.
   - Include a method for retrieving results after the tool completes its task.

4. **Refer to an Example:**
   For guidance, refer to `chat_piano/tools/generateMidiTool.py`, which includes a clear implementation of these principles.

5. **Test the Tool:**
   Ensure the new tool integrates seamlessly with the server and behaves as expected during interaction.

</details>

For further details, contact the project author or refer to the contribution guidelines.

## 📜 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgments

- **Music X Lab:** Developed under the guidance and support of [Music X Lab](http://www.musicxlab.com/).
- **Contributors:** Thanks to contributors from the [Music X Lab GitHub organization](https://github.com/music-x-lab) for their invaluable support.
- **Community:** Gratitude to all developers, musicians, and community members who have enhanced this project.
- **Open-Source Tools:** Special thanks to the developers and communities supporting the open-source tools and libraries utilized in this project.

---
