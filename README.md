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
<div>
<p>This section provides detailed steps to install the project locally. Ideal for developers or testers who wish to modify and run the tool on their machines.</p>

<ol>
  <li>Clone the repository recursively to include all submodules:
    <pre><code>git clone git@github.com:yhbcode000/ChatPiano.git
cd ChatPiano</code></pre>
  </li>
  <li>Install the package in editable mode to allow changes:
    <pre><code>pip install -e .</code></pre>
  </li>
  <li>Start the Chat Piano tool server:
    <pre><code>start-chatpiano</code></pre>
    After this, the server will start and provide a URL for API interaction.
  </li>
</ol>
</div>
</details>

<details>
<summary>Using uv - Enhanced project synchronization and management</summary>
<div>
<p>The `uv` tool provides a streamlined way to manage synchronization and ensure optimal configurations for running the project.</p>

<ol>
  <li>Sync the project to ensure all dependencies and configurations are up-to-date:
    <pre><code>uv sync</code></pre>
  </li>
  <li>Run the server with the `uv` management tool:
    <pre><code>uv run python -m chat_piano</code></pre>
    This command ensures the application is running with the best possible setup provided by `uv`.
  </li>
</ol>
</div>
</details>

<details>
<summary>Docker Setup - Containerized deployment for isolated environments</summary>
<div>
<p>Use Docker to encapsulate the project and its dependencies for an isolated and consistent environment. This is the recommended approach for production use.</p>

<ol>
  <li>Build the Docker container locally:
    <pre><code>docker build -t chat-piano .</code></pre>
  </li>
  <li>Run the container in detached mode:
    <pre><code>docker run -d --name chat-piano-instance chat-piano</code></pre>
  </li>
</ol>

<p><strong>Note:</strong> The Docker image includes all dependencies, ensuring a consistent and isolated environment. For production use, consider pulling the pre-built image to save time.</p>
</div>
</details>

<details>
<summary>Pull Pre-Built Docker Image - Quick setup using a pre-built image</summary>
<div>
<p>For quicker setup and deployment, use a pre-built Docker image hosted on Docker Hub.</p>

<ol>
  <li>Pull the image directly from Docker Hub:
    <pre><code>docker pull TODO-TO-BE-ANNOUNCED</code></pre>
  </li>
  <li>Create a container from the pulled image:
    <pre><code>docker run -d --name chat-piano-instance TODO-TO-BE-ANNOUNCED</code></pre>
  </li>
  <li>Optionally, set up the Docker service for managed deployment:
    <pre><code>docker service create --name chat-piano-service TODO-TO-BE-ANNOUNCED</code></pre>
    This approach is ideal for scaling and orchestrating multiple instances efficiently.
  </li>
</ol>
</div>
</details>

## 📖 Usage

Once the server starts, you can access the API documentation via the provided link in the console output. Use the documentation to explore and interact with the APIs.

### Example

<ol>
  <li>Start the server locally or via Docker.</li>
  <li>Visit <code>http://localhost:5000</code> (or the server's actual address) to access the interactive API documentation.</li>
  <li>Test endpoints directly from the documentation or integrate the APIs into your application.</li>
</ol>

## 🤝 Contributing

We welcome contributions from the community. Here are some ways you can contribute:

<ul>
  <li>Report bugs or suggest features by opening issues.</li>
  <li>Submit pull requests for fixes or new tools.</li>
  <li>Share feedback and ideas for improvement.</li>
</ul>

<details>
<summary>Adding Tools to the Repository - Extend the functionality with new tools</summary>
<div>
<p>To add a new tool to the Chat Piano system, follow these steps:</p>

<ol>
  <li><strong>Configure the Tool in <code>__init__.py</code>:</strong>
    Add your tool configuration to <code>chat_piano/tools/__init__.py</code> to register it in the system.
  </li>
  <li><strong>Create the Tool's Python File:</strong>
    Place your Python file in the <code>chat_piano/tools</code> folder. This file should define the tool's functionality and follow these guidelines:
    <ul>
      <li>Always return a string to ensure the AI agent receives feedback from the tool.</li>
      <li>Use a non-blocking thread for any long-running algorithms to avoid stalling the main process.</li>
    </ul>
  </li>
  <li><strong>Implement Status and Results Handling:</strong>
    <ul>
      <li>Provide a method for checking the tool's status.</li>
      <li>Include a method for retrieving results after the tool completes its task.</li>
    </ul>
  </li>
  <li><strong>Refer to an Example:</strong>
    For guidance, refer to <code>chat_piano/tools/generateMidiTool.py</code>, which includes a clear implementation of these principles.
  </li>
  <li><strong>Test the Tool:</strong>
    Ensure the new tool integrates seamlessly with the server and behaves as expected during interaction.
  </li>
</ol>
</div>
</details>

For further details, contact the project author or refer to the contribution guidelines.

## 📜 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgments

<ul>
  <li><strong>Music X Lab:</strong> Developed under the guidance and support of <a href="http://www.musicxlab.com/">Music X Lab</a>.</li>
  <li><strong>Contributors:</strong> Thanks to contributors from the <a href="https://github.com/music-x-lab">Music X Lab GitHub organization</a> for their invaluable support.</li>
  <li><strong>Community:</strong> Gratitude to all developers, musicians, and community members who have enhanced this project.</li>
  <li><strong>Open-Source Tools:</strong> Special thanks to the developers and communities supporting the open-source tools and libraries utilized in this project.</li>
</ul>

---
