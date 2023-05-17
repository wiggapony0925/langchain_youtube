# YouTube LLM with OpenAI

This project utilizes the LangChain library and OpenAI to generate YouTube video titles and descriptions.

## Overview

The YouTube LLM (Language Model) project aims to assist content creators in generating creative and engaging titles and descriptions for their YouTube videos. By leveraging the power of OpenAI's language model, the project generates compelling prompts and outputs that can be used as a starting point for video production.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
pip install -r requirements.txt
```



2. Open your web browser and navigate to the provided local URL (e.g., `http://localhost:8501`).

3. Enter your desired prompt in the text input.

4. The application will generate YouTube video titles and descriptions based on the provided prompt.

## Configuration

- `llms.py`: Contains the LangChain integration with OpenAI and the LLMChain definition.
- `prompts.py`: Defines the PromptTemplates used to generate titles and descriptions.
- `main.py`: Streamlit application code for user interaction and output display.
- `apikey.py`: File to store your OpenAI API key (excluded from version control using .gitignore).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

