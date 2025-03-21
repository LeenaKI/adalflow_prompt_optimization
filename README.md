# AI Prompt Optimization App

This repository contains a Streamlit-based web application designed to optimize AI prompts for better clarity, structure, and effectiveness. It leverages the **AdalFlow** library and **Gemini API** to streamline the prompt optimization process.

---

## Features

- Interactive user interface for prompt optimization.
- Leverages AdalFlow to apply advanced optimization techniques.
- Supports customizable Gemini models (e.g., `gemini-1.5-flash` used here).
- Secure API key management.
- Detailed and structured outputs tailored to the user's input.

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/LeenaKI/adalflow_prompt_optimization.git
   cd adalflow_prompt_optimization
   ```

2. **Install Dependencies**
   Ensure you have Python installed (>=3.8), then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Key**
   You can provide your Gemini API key in one of two ways:
   - **Via Streamlit Input**: Enter the key directly in the app when prompted.
   - **Environment Variable**: Set an environment variable for better security:
     ```bash
     export GEMINI_API_KEY="your-api-key-here"
     ```

---

## Usage

1. Run the app using Streamlit:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at [http://localhost:8501](http://localhost:8501).

3. Enter your Gemini API key if prompted.

4. Input your custom prompt in the text area and click **Optimize Prompt** to receive an optimized version.

---

## Examples

### `Input Prompt:`
> Write a summary of the benefits of renewable energy.

### `Optimized Output Prompt:`
> Provide a detailed summary of the benefits of renewable energy. Address the following aspects:
> 1. Environmental benefits, such as reduced greenhouse gas emissions.
> 2. Economic advantages, including job creation and cost savings.
> 3. Social impacts, such as energy independence and improved public health.
> Ensure the summary is concise yet comprehensive, written for a general audience.

---

## Security

To ensure your API key remains private:
- Do not hardcode API keys in your scripts.
- Use Streamlit's secure input or environment variables.

---

## Technologies Used

- **Python**: Programming language.
- **Streamlit**: Framework for creating the web interface.
- **AdalFlow**: For prompt optimization pipelines.
- **Gemini API**: Backend for natural language processing.

