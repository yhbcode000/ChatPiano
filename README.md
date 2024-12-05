# 🎹 Chat Piano
<!-- 
Chat Piano leverages advanced AI models to interpret voice commands and convert them into MIDI files, facilitating a seamless interaction between users and digital music creation. This project integrates various microservices to manage data, improve functionality, and streamline the user experience.

## 🌟 Features

- **🎶 Voice to MIDI Conversion:** Converts voice commands directly into MIDI files using state-of-the-art AI models.
- **⚙️ Tools Support and Configuration:** A modular system that integrates various tools to enhance functionality.
- ~~**🏗️ Modular Architecture:** Utilizes a series of microservices for scalable and maintainable codebase.~~
- **🛠️ Customizable Workflows:** Users can define and customize their music creation workflows.
- **🔄 Continuous Integration:** Automated testing and deployment pipelines to ensure reliability and performance.
- **🎹 Embodied Intelligence:** Integrates sensory inputs (microphones or keyboard devices) with AI planning logic (LLM and music models) to control actuators (physical or electronic pianos). This end-to-end process encapsulates the perception-planning-control loop of embodied AI, enabling a dynamic and responsive music creation experience.


## 🛠️ Technical Stack

- **📦 Microservices:** Includes services:
  - ~~**📚 [knowledge-database-management-service](https://github.com/yhbcode000/knowledge-database-management-service):** Manages AI knowledge in a way that allows for human control and sophisticated data management.~~
  - **🎵 [musecoco-text2midi-service](https://github.com/yhbcode000/musecoco-text2midi-service):** Refactors MuseCoco into a deployable service module, ensuring adaptability and detailed implementation abstraction.
  - ~~**💬 [llm-text2text-service](https://github.com/yhbcode000/llm-text2text-service):** Integrates third-party open-source LLM services for modular deployment and API interaction from leading models.~~
  - ~~**🤖 [multi-modal-ai-bot-template](https://github.com/yhbcode000/multi-modal-ai-bot-template):** Provides a template for multimodal AI interactions, integrating various AI workflows.~~
- **🐳 Docker & Kubernetes:** For containerization and orchestration to manage and scale the application seamlessly. 

## ⚙️ Installation
-->
To set up the Chat Piano project on your local machine, follow these steps:

```bash
# Clone the repository recursively to include all submodules
git clone git@github.com:yhbcode000/ChatPiano.git
cd ChatPiano
pip install -e .

# start the chatpiano tool server
start-chatpiano
```
<!-- 
```bash
# Build the Docker container
docker build -t chat-piano .

# Run the Docker container
docker run -d --name chat-piano-instance chat-piano
```

> 📝 **Note:** The Docker image for Chat Piano is quite large due to its comprehensive set of dependencies. To simplify installation and avoid lengthy build times, we recommend pulling the image directly from our cloud repository.

For a quicker setup using Docker, follow these steps:

```bash
# Pull the image from Docker Hub
docker pull TODO-TO-BE-ANNOUNCED

# Create a container from the image
docker run -d --name chat-piano-instance TODO-TO-BE-ANNOUNCED

# Initialize the Docker service (if necessary)
docker service create --name chat-piano-service TODO-TO-BE-ANNOUNCED
``` -->
<!-- 
## 📖 Usage

Start by sending voice commands to the system. The AI will process these commands and generate corresponding MIDI files. Detailed documentation on specific commands and customization will be provided in further updates (TODO-UPDATE-DOCUMENT).

## 🤝 Contributing

We encourage contributions from the community. Whether you are a developer, musician, or enthusiast, your insights are valuable to us. Please refer to `CONTRIBUTING.md` (TODO-CONTRIBUTION) for more information on how to contribute.

## 📜 License

This project is licensed under Apache License 2.0 - see the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgments

- This project is developed under the guidance and support of [Music X Lab](http://www.musicxlab.com/). 
- Special thanks to the contributors from the [Music X Lab GitHub organization](https://github.com/music-x-lab) for their invaluable support and resources.
- Thanks to all the developers, musicians, and community members who have contributed their time and effort to enhance the Chat Piano project.
- Additional thanks to the developers and communities supporting the open-source tools and libraries utilized in this project.

## Helpful Link

- https://www.onlineconverter.com/midi-to-mp3 -->
